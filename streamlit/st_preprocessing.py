import streamlit as st

"""
## Preprocessing

For Machine Learnng models and the Deep Learning models we tried several pre-processing workflows. For ML more preprocessing was necessary than for deep learning. We applied filters like "CLAHE" and "Gaussian Blur" and normalized the pixel intensity.

### Split data
In a first step the data has been split into a train (85%) and test (15%) data set. This test set is used after the model training to test how relieble the models predictions are. 
Then the train data set has been split again into the final train data set (80%) and a validation data set (20%). Both dataset are used during the training process of the model. 
"""

st.image('images/Train-Test-Split.png', caption = "Split data into train, validation and test set")

"""
### Workflow for VGG16
The following workflow diagram describes the preprocessing we have done to receive the input data for our VGG16 model. All steps of pipeline have been appied to the train, validation and test data set. Only the data augmentation was ommited for the test data set.

"""

st.image('images/VGG16_preprocessing.png', caption = "VGG16 preprocessing")

"""
### Data augmentation

To deal with the class imbalance the augmentation technique was been applied. The images of the minority classes (COVID, Lung Opacity and Viral Pneumonia) have been augmented. This means modified versions of the X-ray images have been created. The following modifications have been applied: 
* Horizontal Flip
* Rotation by an angle between -15 and +15 degrees 
* Shift the image horizontally and vertically 
* Scale the image

"""
st.image('images/aug_example_covid.png', caption = "example of data augmentation: X-ray images plus masks")

import cv2
import numpy as np


# **ToDo:** This page needs further work. Maybe we should not write too much here. Just describe in detail the preprocessing of iamges we have done to for our final model. e.g. apply preprocessing function which belongs to the pretrained model, ... So I think some parts of the following text can be deleted.

# * **Input format**  
# Multiple image formats are used in the dataset. All images need to be loaded as RGB24 `(width, height, 3)` format.

# * **Contrast correction**  
# To harmonize the average brightness and contrast representation across the dataset we OpenVC's [CLAHE](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html) is applied to each image.

# * **Noise/Artefact suppression**  
# To minimize the influence of specific noise patterns from the different sources a Gaussian blur filter is applied to each image

# * **Normalization**  
# All input of the model needs to be normalized. So the images are divided by 255 to the range `[0..1]`

# TODO: add a demo plot (before vs after) as "hstack" image (side-by-side comparison)?
