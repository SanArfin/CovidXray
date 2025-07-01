import streamlit as st
import pandas as pd
import numpy as np
import warnings
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

"""
## The Dataset

The dataset employed in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database) and comprises a collection of chest X-ray images categorized into four diagnostic classes: **Normal**, **Lung Opacity**, **COVID**, and **Viral Pneumonia**.  
The dataset contains the X-ray images and for each image a corresponding attention mask. An example of each class with its corresponding attention mask is shown below.
"""

# show example x-ray images with correspondig attention masks:
st.image('images/xray_mask.png', caption = "Example of X-ray image of each class with its corresponding attention mask")

"""
A notable characteristic of this dataset is the class imbalance. In practice, some classes—particularly *COVID* and *Viral Pneumonia*—are under-represented relative to *Normal* and *Lung Opacity*. This uneven distribution can lead to biased model training where predictive performance is skewed towards the majority classes. We need to address this issue before we use this dataset for modeling.

"""

# show pie chart of class distribution to demonstrate the class imbalance
st.image('images/data_distribution.png', width=600, caption = "Class distribution in our dataset")

"""

Furthermore, the dataset aggregates images from different sources. The diversity of sources introduces variability in imaging protocols, equipment calibration, resolution, and patient demographics. These factors may lead to systematic biases that could affect the generalizability of the trained models. 
"""

st.image('images/class_distrbution_by_source_url.png')

"""
The analysis of the mean pixel intensity and standard deviation showed that there are differences between the images from different sources. The following graphs show the distribution of mean pixel intensity (A) and the standard deviation (B) by sources. The chosen colours for the different sources are the same as in the above diagram. This plots show that the mean pixel intensity and the standard deviation of the images from the www.kaggle.com/* sources (pink and gray) are different. The above diagram showed that from these sources all the "Lung Opacity" images and nearly all the "Normal" images come from this two sources. This could influence the classification.

"""

st.image(['images/pixel_intensity_by_spurce_raw.png', 'images/pixel_intensity_by_spurce_postNormal.png'], width= 350)
#st.image('images/pixel_intensity_legend.png')

"""
These circumstances need to be addressed when preprocessing the data for training of models.
"""

# # example to work "online" with data
df = pd.read_csv("data/processed/df_xray_processed_normed_enc.csv")
st.dataframe(df.head(10))

fig = plt.figure()
sns.countplot(x = 'label', data = df)
st.pyplot(fig)

