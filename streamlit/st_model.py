import streamlit as st

"""
## Modelling

### Testing several models

During this project several Machine and Deep Learning models were evaluated.

**Machine Learning:**
* Logistic Regression
* Random Forest
* Support Vector Machines
* XGBoost
* MLP Classifier

**Deep Learning:**
* Self-build CNN
* EfficientNet
* InceptionV3
* DenseNet121
* VGG16
* Ensemble Model

### Used model: pretrained VGG16 with fine-tuning

One of the best models we tested was a VGG16 model with pretrained weights. This model has already been trained on another image dataset. We added a suitable classification head to get predictions for the 4 classes of our dataset. While fine tuning the last 8 layers were unfreezed to being trained again.

"""
"""
### Model architecture
"""
st.image('images/vgg16_architecture.png')


# show source of image
url = "https://www.kaggle.com/code/blurredmachine/vggnet-16-architecture-a-complete-guide"
st.write("image source [https://www.kaggle.com/code/blurredmachine/vggnet-16-architecture-a-complete-guide](%s)" % url)


st.image('images/model_vgg16_classification_head.png', caption = "Classification head used")

git 
"""
### Training the model
"""
st.image('images/vgg16_accuracy.png', caption="Accuracy and loss during training")

"""
### Results: Testing the model

"""

st.image('images/vgg16_classification_report.png', caption="Classification Report")

st.image('images/vgg16_confusion_matrix.png', caption="Confusion Matrix")

