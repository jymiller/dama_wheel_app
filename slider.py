#
# Purpose: This is a Streamlit app operates a slide!
# Re-written by: John Y Miller
#
# Date: 2024-01-04


# Import the required libraries
import streamlit as st

st.set_page_config(
    page_title="DMM Assessment Chart",
    page_icon=":star:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.bbinsight.com',
      # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# DMM v1"
    }
)

# Title of the app
st.title('Simple Slider App')


# st.markdown("<h3 style='font-size: 18px;margin-top: 0px;'>Current Rank</h3>", unsafe_allow_html=True)

# Inject custom CSS with markdown
# st.markdown("""
#     <style>
#     .stSlider > div[role="slider"] {
#         background-color: #AA4B4B; /* Customize the slider color here */
#     }
#     </style>
#     """, unsafe_allow_html=True)

# Your custom CSS
custom_css = """
<style>
.stSlider .slider-thumb {
    background-color: blue;
}
.stSlider .slider-track {
    background-color: lightblue;
}
</style>
"""

# Creating a slider
slider_value = st.slider("Choose a number", 1, 5)

# Display the current value of the slider
st.write(f"You selected: {slider_value}")

   