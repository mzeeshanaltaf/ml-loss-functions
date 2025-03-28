import streamlit as st
from util import *

# Page configuration options
page_title = "FAQs"
page_icon = "💬"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide", initial_sidebar_state="expanded")

st.title('FAQs')

expand_all = st.toggle("Expand all", value=True)

# Display footer in the sidebar
display_footer()

faq_data = {
        'What this Application is about?':
            '<p>This web app helps you to visualize and compare popular machine learning loss functions .</p>',
        'Which Loss functions are supported by this application?':
            """This app supports visualizing the following loss functions:
            <ul>
              <li>MSE</li>
              <li>MAE</li>
              <li>Huber Loss</li>
            </ul>
            """
            ,
        'I want to make modification in the application. Can I get the application source code?':
            '<p>Yes, Source code of this application is available at: '
            '<a href="https://github.com/mzeeshanaltaf/ml-loss-functions">GitHub</a></p>',

    }

# Display expandable boxes for each question-answer pair
for question, answer in faq_data.items():
    with st.expander(r"$\textbf{\textsf{" + question + r"}}$", expanded=expand_all):  # Use LaTeX for bold label
        st.markdown(f'<div style="text-align: justify;"> {answer} </div>', unsafe_allow_html=True)