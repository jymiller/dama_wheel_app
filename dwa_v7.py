import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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

# Function to create the radar chart
def create_radar_chart(angles, values):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))  # Adjusted figure size for sidebar layout
    ax.set_theta_offset(np.pi / 2)  # Set the start to the top
    ax.set_theta_direction(-1)  # Set the direction to clockwise

    # Draw and fill the chart
    ax.fill(angles, values, 'teal', alpha=0.25)
    ax.plot(angles, values, 'o-', linewidth=2)

    # Set the labels for the knowledge areas
    ax.set_thetagrids(np.degrees(angles[:-1]), knowledge_areas)

    return fig

# Set up the layout with sliders on the left and the radar chart on the right
col1, col2 = st.columns([3, 5])  # Adjust the column widths as needed

# Initialize the maturity levels with a default value
maturity_levels = {area: 3 for area in knowledge_areas}

# Create sliders for each of the 11 knowledge areas
with col1:
    for area in knowledge_areas:
        maturity_levels[area] = st.slider(f"Select your maturity level for {area}:", 0, 5, 3)

# Convert the maturity levels to a list and append the first value to close the radar chart loop
values = list(maturity_levels.values()) + [list(maturity_levels.values())[0]]

# Create the radar chart with the updated values
with col2:
    chart = create_radar_chart(angles, values)
    st.pyplot(chart)
