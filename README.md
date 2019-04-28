# Hot Dog Or Not Hot Dog

### What is it? 
This is an image classifier that can be used to identify whether an image is a hot dog or not. I have also included code and instructions for building an API endpoint for the classifier that can be hosted on the cloud. 

### Inspiration 
This started as a group project while I was a student at the Flatiron School Data Science Bootcamp. My partner, [Jaime Cheng](http://github.com/softserveslayer) and I got our inspiration from the [HBO series Silicon Valley](https://www.youtube.com/watch?v=ACmydtFDTGs). After a few days of learning the ins and out of neural networks, we were able to successfully train a convolutional neural network to recognize whether an image was a hot dog or not. After graduation, I was interested in turning this project into a full fledged application that would take an image and return a prediction. My first step was to build and host a REST API for model and am currently working on a frontend for the application in React. 

### Training Process

Our training process is available in [base_model.ipynb](https://github.com/vishalpatel2890/hotdog-or-not/blob/master/base_model.ipynb). 

We began the process by training a simple densely connected network to establish a base level of performance. Next, we assembled a simple convolutional neural network with the following architecture: 

| Layer (type)  |      Output Shape    | Param #   |
|----------|:-------------:|------|
dense_17 (Dense)       |      (None, 128)       |        19267712  
dense_18 (Dense)    |         (None, 64)         |       8256      
dense_19 (Dense)      |       (None, 1)       |          65        

Total params: 19,276,033
Trainable params: 19,276,033
Non-trainable params: 0
_________________________________________________________________

Next we assembled a simple convolutional neural network: 

                              
| Layer (type)  |      Output Shape    | Param #   |
|----------|:-------------:|------|
conv2d_1 (Conv2D)    |        (None, 222, 222, 64)  |    1792      
max_pooling2d_1 (MaxPooling2) | (None, 111, 111, 64) |     0         
conv2d_2 (Conv2D)       |     (None, 109, 109, 32)  |    18464     
max_pooling2d_2 (MaxPooling2) | (None, 54, 54, 32)    |    0         
flatten_1 (Flatten)  |        (None, 93312)   |          0         
dense_4 (Dense)     |         (None, 32)      |          2986016   
dense_5 (Dense)    |          (None, 1)        |         33 

Total params: 3,006,305
Trainable params: 3,006,305
Non-trainable params: 0
_________________________________________________________________

We also tested this model with a dropout layer after the flatten layer. 

Last we made use of several transfer learning models. We used Inception V3, ResNet50, and VGG16 with Inception V3 giving us the best results (measured by testing accucary and F1 score). 

The following arcitechture was our final model. 


#### Training Results
| Neural Network   | Traing Accuracy     | Testing Accuracy     | F1 Score     |
| -----            | ----                | -----                | -----        |
| Densely Connected| ----                | -----                | -----        |
| CNN              | ----                | -----                | -----        |
| CNN W/ Dropout   | ----                | -----                | -----        |
| Inception V3     | ----                | -----                | -----        |
| ResNet50         | ----                | -----                | -----        |
| VGG16            | ----                | -----                | -----        |

#### Training Next Steps


 
