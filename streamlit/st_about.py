import streamlit as st

import streamlit as st

st.title("About the Project")

st.markdown("### Background and Motivation")

with st.container():
    st.markdown("""
    Chest X-rays play a critical role in diagnosing respiratory diseases like **COVID-19**, **pneumonia**, and **lung opacity**. However, manual interpretation by radiologists is often:
    - Time-consuming
    - Subject to inter-observer variability
    - Prone to human error

    **Artificial Intelligence (AI)**, especially deep learning, offers a reliable and scalable way to automate this diagnosis process, making healthcare:
    - More efficient
    - More accurate
    - More accessible in under-resourced settings
    """)

st.markdown("### The Role of AI in Medical Imaging")
cols = st.columns(2)

with cols[0]:
    st.markdown("""
    **Convolutional Neural Networks (CNNs)** are used to:
    - Automatically extract deep features from X-rays
    - Learn subtle patterns beyond human perception
    - Enhance diagnostic accuracy and speed
    """)

with cols[1]:
    st.image('images/classification.png', caption="X-ray image classification pipeline")
    st.caption("Figure adapted from Khan et al. (2021), BDCNet [DOI: 10.1016/j.bspc.2021.102724]")

st.markdown("### Project Objectives")
with st.expander("Click to view project goals"):
    st.markdown("""
    - Build a reliable model for chest X-ray classification
    - Integrate Grad-CAM for visual explainability
    - Enable real-time prediction through a web interface
    - Facilitate AI-assisted diagnosis with custom mask inputs
    """)

st.markdown("### How It Works")
st.markdown("""
1. Upload a chest X-ray and its corresponding **segmentation mask**.
2. The model uses a **VGG16-based attention architecture** to process the image.
3. It classifies the X-ray into one of four categories:
   - Normal
   - COVID-19
   - Lung Opacity
   - Viral Pneumonia
4. A Grad-CAM heatmap highlights areas that influenced the model's decision.
""")

st.info("Want to try it? Head to the 'Try the result!' tab to upload your own image!")




