import streamlit as st
from util import *

# Page title of the application
page_title = "Loss Lens"
page_icon = "🔍"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Application Title and description
st.title(f'{page_title}{page_icon}')
st.write('***:blue[Visualize, Compare, Optimize! 🚀]***')
st.write("""
*Loss Lens is an interactive web app that helps you visualize and compare popular machine learning loss functions like 
MSE, MAE, and Huber Loss in real-time. Perfect for students, researchers, and ML practitioners to understand how 
different loss functions behave with outliers and noisy data! 🎯📊*
""")
# Display footer in the sidebar
display_footer()

st.subheader('Configuration:')
# Add interactive controls
delta = st.slider("Huber Loss delta parameter:", 0.1, 3.0, 1.0)

plot_loss_functions(delta)






