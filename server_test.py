# USAGE
# Start the server:
# 	python run_keras_server.py
# r = requests.post('http://ec2-13-58-68-35.us-east-2.compute.amazonaws.com/predict', data={'image':url}).json()

# import the necessary packages
from threading import Thread
import urllib
import numpy as np
import flask
import sys
import io

from process_image import *
from classify import *

# initialize our Flask application, Redis server, and Keras model
app = flask.Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the view
	data = {"success": False}

	# ensure an image url was properly uploaded to our endpoint
	if flask.request.method == "POST":
		if flask.request.get_data("image"):
			#get image url and pass to prepare_image
			image = flask.request.get_data("image")
			image = image.decode('utf-8')
			image = urllib.parse.unquote(image)

			image = prepare_image(image[6:], (IMAGE_WIDTH, IMAGE_HEIGHT))

			# generate an ID for the classification then add the
			# classification ID + image to the queue
			k = str(uuid.uuid4())
			d = {"id": k, "image": base64_encode_image(image)}

			db.rpush(IMAGE_QUEUE, json.dumps(d))

			# keep looping until our model server returns the output predictions
			while True:
				# attempt to grab the output predictions
				output = db.get(k)

				# check to see if our model has classified the input image
				if output is not None:
 					# add the output predictions to our data
 					# dictionary so we can return it to the client
					output = output.decode("utf-8")
					data["predictions"] = json.loads(output)
					# delete the result from the database and break
					# from the polling loop
					db.delete(k)
					break

				# sleep for a small amount to give the model a chance
				# to classify the input image
				time.sleep(CLIENT_SLEEP)

			# indicate that the request was a success
			data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	# load the function used to classify input images in a *separate*
	# thread than the one used for main classification
	print("* Starting model service...")
	t = Thread(target=classify_process, args=())
	t.daemon = True
	t.start()

	# start the web server
	print("* Starting web service...")
	app.run(host='0.0.0.0', port=80)

#to run on ec2
#connect to ec2 instance
#git clone repo to instance
#pip install requirements.txt (pip3 install flask keras tensorflow numpy PIL redis
#launch redis with redis-server (check with redis-cli ping)
#launch server with sudo python3 server_test.py or nohup python3 server_test.py &
