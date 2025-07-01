import streamlit as st
st.set_page_config(layout="wide")

st.title("Chest-X-Ray Analysis")

# Define the pages
st_about = st.Page("st_about.py", title="About", icon="🎈")
st_dataset = st.Page("st_dataset.py", title="Dataset", icon="🗂️")
st_preprocessing = st.Page("st_preprocessing.py", title="Preprocessing", icon="🛠️")

# I think it makes no sense for us to have this page?! Anything shoudl be explained in "dataset" and "preprocessing" pages
#st_eda = st.Page("st_eda.py", title="Exploratory Data Analysis (EDA)", icon="🔍") 

st_model = st.Page("st_model.py", title="Used model", icon="⚙️")
st_run_model = st.Page("st_run_model.py", title="Try the result!", icon="🎉")

# Set up navigation, add "st_eda" again if we need it
pg = st.navigation([st_about, st_dataset, st_preprocessing, st_model, st_run_model])

# Run the selected page
pg.run()

