import numpy as np
from keras.preprocessing.image import img_to_array, load_img
from keras.applications import imagenet_utils
from PIL import Image
from io import BytesIO
import base64
import sys
import time
import requests

def base64_encode_image(a):
	# base64 encode the input NumPy array
	return base64.b64encode(a).decode("utf-8")

def base64_decode_image(a, dtype, shape):
	# if this is Python 3, we need the extra step of encoding the
	# serialized NumPy string as a byte object
	if sys.version_info.major == 3:
		a = bytes(a, encoding="utf-8")

	# convert the encode string to a NumPy array using the supplied data
	# type and target shape
	a = np.frombuffer(base64.decodestring(a), dtype=dtype)
	a = a.reshape((1,224,224,3))
	# return the decoded image
	return a

def prepare_image(image, target):
	#get image from url and open as PIL
	response = requests.get(image)
	image = Image.open(BytesIO(response.content))

	# resize the input image and preprocess it
	image = image.resize((224,224))
	image = img_to_array(image)
	image = image/255
	image = np.expand_dims(image, axis=0)

	# return the processed image
	return image
