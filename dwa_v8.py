import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set the page to wide mode
st.set_page_config(layout="wide")

# Define the knowledge areas in clockwise order starting with Data Governance at the top
knowledge_areas = [
    "Data Governance", "Data Modeling & Design", "Data Storage & Operations",
    "Data Security", "Data Integration & Interoperability", "Document & Content Management",
    "Reference & Master Data", "Data Warehousing & Business Intelligence",
    "Metadata", "Data Quality", "Data Architecture"
]

# Initialize the Streamlit app
st.title("DAMA Wheel Maturity Level Assessment")

# Calculate the angle for each knowledge area and adjust to start with Data Governance at the top
angles = np.linspace(0, 2 * np.pi, len(knowledge_areas), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Function to create the radar chart with fixed axis limit and adjusted labels
def create_radar_chart(angles, values):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))  # Increased figure size
    ax.set_theta_offset(np.pi / 2)  # Set the start to the top
    ax.set_theta_direction(-1)  # Set the direction to clockwise

    # Set the axes limit
    ax.set_ylim(0, 5.5)

    # Draw and fill the chart
    ax.fill(angles, values, 'teal', alpha=0.25)
    ax.plot(angles, values, 'o-', linewidth=2)

    # Set the labels for the knowledge areas with adjusted position and font size
    # and remove the angle annotations (numeric values)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(knowledge_areas, horizontalalignment='center', size=10, color='black', weight='bold')

    return fig

# Initialize the maturity levels with a default value
maturity_levels = {area: 3 for area in knowledge_areas}

# Using Streamlit's columns to create a layout with some space between the sliders and the chart
left_column_width = 4
middle_space_width = 1
right_column_width = 5

col1, col2, col3 = st.columns([left_column_width, middle_space_width, right_column_width])

# Create sliders in the left column
with col1:
    for area in knowledge_areas:
        maturity_levels[area] = st.slider(f"Select your maturity level for {area}:", 0, 5, 3)

# The middle column will be used as spacing
with col2:
    st.write("")  # This is just to enable the space column

# Convert the maturity levels to a list and append the first value to close the radar chart loop
values = list(maturity_levels.values()) + [list(maturity_levels.values())[0]]

# Create the radar chart in the right column
with col3:
    chart = create_radar_chart(angles, values)
    st.pyplot(chart)
