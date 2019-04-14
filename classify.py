import redis
import uuid
import numpy as np
from keras.models import load_model
from process_image import *

db = redis.StrictRedis(host="localhost", port=6379, db=0)
model = None

# initialize constants used to control image spatial dimensions and
# data type
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "np.float32"

# initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 32
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25


def classify_process():
    # load pretrained model
    print("* Loading model...")

    model = load_model('inception_net_model')
    print("* Model loaded")

	# continually pool for new images to classify
    while True:
    	# attempt to grab a batch of images from the database, then
    	# initialize the image IDs and batch of images themselves
        queue = db.lrange(IMAGE_QUEUE, 0, BATCH_SIZE - 1)
        imageIDs = []
        batch = None

        # loop over the queue
        for q in queue:
            # deserialize the object and obtain the input image

            q = json.loads(q.decode())

            image = base64_decode_image(q["image"], np.float32,
                (1, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANS))

        	# check to see if the batch list is None
            if batch is None:
                batch = image

            # otherwise, stack the data
            else:
                batch = np.vstack([batch, image])

            # update the list of image IDs
            imageIDs.append(q["id"])

        # check to see if we need to process the batch
        if len(imageIDs) > 0:
        	# classify the batch
            print("* Batch size: {}".format(batch.shape))
            preds = model.predict(batch)
            # results = imagenet_utils.decode_predictions(preds)
            results = preds
        	# loop over the image IDs and their corresponding set of
        	# results from our model
            for (imageID, result) in zip(imageIDs, results):
        		# # initialize the list of output predictions
                print(imageID, result)
                label = 'hot dog' if result[0] > .5 else 'not_hot_dog'
                output = []
                r = {"label": label, "probability": float(result)}
                output.append(r)

                # store the output predictions in the database, using
                # the image ID as the key so we can fetch the results
                db.set(imageID, json.dumps(output))

                # remove the set of images from our queue
                db.ltrim(IMAGE_QUEUE, len(imageIDs), -1)

                # sleep for a small amount
                time.sleep(SERVER_SLEEP)
