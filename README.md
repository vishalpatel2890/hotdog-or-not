# Hot Dog Or Not Hot Dog

### What is it? 
This is an image classifier that can be used to identify whether an image is a hot dog or not. I have also included code and instructions for building an API endpoint for the classifier that can be hosted on the cloud. 

### Inspiration 
This started as a group project while I was a student at the Flatiron School Data Science Bootcamp. My partner, [Jaime Cheng](http://github.com/softserveslayer) and I got our inspiration from the [HBO series Silicon Valley](https://www.youtube.com/watch?v=ACmydtFDTGs). After a few days of learning the ins and out of neural networks, we were able to successfully train a convolutional neural network to recognize whether an image was a hot dog or not. After graduation, I was interested in turning this project into a full fledged application that would take an image and return a prediction. My first step was to build and host a REST API for model and am currently working on a frontend for the application in React. 

### Training Process
Our training process is available in [base_model.ipynb](https://github.com/vishalpatel2890/hotdog-or-not/blob/master/base_model.ipynb). 

We began the process by training a simple denseley connected network to establish a base level of performance. Next, we assembled a simple convultional neural network with the following aritechture: 

1. Conv2D -------> activation: 'relu' 
2. MaxPooling2D -> window: (2, 2)
3. Conv2D -------> nodes: 32, filter: (3, 3), activation:'relu'
4. MaxPooling2D -> window:(2, 2)
5. Flatten
6. Dense --------> nodes: 32, activation:'relu'
7. Dense --------> nodes: 1, activation:'sigmoid'

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


 
