import streamlit as st

st.set_page_config(layout="wide")
st.title("Chest-X-Ray Analysis")

# Define your pages as functions
def about():
    st.write("About page content")

def dataset():
    st.write("Dataset page content")

def preprocessing():
    st.write("Preprocessing page content")

def model():
    st.write("Model page content")

def run_model():
    st.write("Run model page content")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Choose a page",
    ["About", "Dataset", "Preprocessing", "Model", "Run Model"]
)

if page == "About":
    about()
elif page == "Dataset":
    dataset()
elif page == "Preprocessing":
    preprocessing()
elif page == "Model":
    model()
elif page == "Run Model":
    run_model()
