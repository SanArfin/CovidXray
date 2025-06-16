git import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# === Load model once ===
@st.cache_resource
def st_load_model():
    from tensorflow.keras.models import load_model
    return load_model('best_model_vgg16_finetuned_gradcam.keras')


# === Preprocess grayscale image for VGG16 ===
def preprocess_image(img_gray):
    # Convert grayscale to 3 channels by stacking
    img_3ch = np.stack([img_gray]*3, axis=-1)
    img_3ch = img_3ch.astype(np.float32) / 255.0
    # Add batch dimension
    return np.expand_dims(img_3ch, axis=0)


# === Grad-CAM heatmap for multi-input model ===
@st.cache_data
def get_gradcam_heatmap(model, img_array, last_conv_layer_name="block5_conv3", pred_index=None):
    grad_model = tf.keras.models.Model(
        inputs=model.input,
        outputs=[model.get_layer(last_conv_layer_name).output, model.output[1]]
    )
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = tf.reduce_sum(conv_outputs * pooled_grads, axis=-1)
    heatmap = tf.maximum(heatmap, 0)
    heatmap /= (tf.reduce_max(heatmap) + 1e-10)
    return heatmap.numpy(), predictions[0].numpy()



# === Overlay heatmap on image ===
@st.cache_data
def overlay_heatmap(img, heatmap, alpha=0.4, colormap=cv2.COLORMAP_JET):
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap_color = cv2.applyColorMap(heatmap, colormap)

    # Convert grayscale to BGR if needed
    if len(img.shape) == 2 or img.shape[2] == 1:
        img_bgr = cv2.cvtColor(np.uint8(255 * img), cv2.COLOR_GRAY2BGR)
    else:
        img_bgr = np.uint8(255 * img) if img.dtype != np.uint8 else img

    overlayed = cv2.addWeighted(heatmap_color, alpha, img_bgr, 1 - alpha, 0)
    return overlayed


# === Plot prediction bar chart ===
def plot_prediction_bar(predictions):
    class_names = ['Normal', 'COVID', 'Lung_Opacity', 'Viral Pneumonia']
    predictions = np.array(predictions)

    # If predictions are logits, convert to probabilities
    if predictions.max() > 1:
        exp_preds = np.exp(predictions)
        predictions = exp_preds / np.sum(exp_preds)

    fig = go.Figure(go.Bar(
        y=class_names,
        x=predictions,
        text=[f"{p*100:.1f}%" for p in predictions],
        textposition="auto",
        marker_color=["blue", "green", "red", "orange"],
        orientation="h"
    ))
    fig.update_layout(
        title="Predictions for Each Class",
        yaxis_title="Class Name",
        xaxis_title="Prediction Probability",
        xaxis=dict(range=[0, 1]),
        template="plotly_white"
    )
    st.plotly_chart(fig)


# === Combined Grad-CAM and prediction plotting ===
def gradcam_and_predict_plot(img, model, last_conv_layer_name="block5_conv3"):
    img_input = np.expand_dims(img, axis=0)
    heatmap, predictions = get_gradcam_heatmap(model, img_input, last_conv_layer_name)

    class_names = ['Normal', 'COVID', 'Lung_Opacity', 'Viral Pneumonia']
    top_idx = np.argmax(predictions)
    st.success(f"**Predicted Class:** {class_names[top_idx]} ({predictions[top_idx]*100:.2f}%)")

    overlayed_img = overlay_heatmap(img, heatmap)  # Fixed line

    # Plot overlayed image
    st.markdown("#### Grad-CAM Overlay")
    # Resize the overlayed image before displaying
    resized_overlay = cv2.resize(overlayed_img, (300, 300))  # or (256, 256) for even smaller

    # Display the resized image using Streamlit
    st.image(resized_overlay[..., ::-1], caption="Grad-CAM Overlay", use_container_width=False)



    # Plot prediction bar chart
    plot_prediction_bar(predictions)



# === Streamlit UI ===
st.markdown("""
### Evaluate your chest x-ray!

#### How to
Upload your chest x-ray and corresponding mask to see model predictions and Grad-CAM visualization.
""")

uploaded_file = st.file_uploader("Upload Chest X-ray (224x224)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes_img = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_original = cv2.imdecode(file_bytes_img, cv2.IMREAD_GRAYSCALE)

    if img_original is None:
        st.error("Failed to decode the uploaded image. Please upload a valid image.")
    else:
        # Resize to 224x224
        img_resized = cv2.resize(img_original, (224, 224))

        # Optional CLAHE preprocessing (toggle as needed)
        do_corrections = False
        if do_corrections:
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            img_corrections = clahe.apply(img_resized)
            img_corrections = cv2.blur(img_corrections, (3, 3))
        else:
            img_corrections = img_resized

        # Load model
        model = st_load_model()

        # Preprocess image (expand channels and normalize)
        img_preprocessed = preprocess_image(img_corrections)  # shape: (1, 224, 224, 3)

        # Run Grad-CAM + show predictions
        gradcam_and_predict_plot(
            img_preprocessed[0],  # shape: (224, 224, 3)
            model
        )
