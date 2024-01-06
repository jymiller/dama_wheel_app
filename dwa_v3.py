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

# Initialize the maturity levels with a default value
maturity_levels = {area: 3 for area in knowledge_areas}

# Calculate the angle for each knowledge area and adjust to start with Data Governance at the top
angles = np.linspace(0, 2 * np.pi, len(knowledge_areas), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Define the function to create the radar chart
def create_radar_chart(ax, angles, values):
    ax.set_theta_offset(np.pi / 2)  # Set the start to the top
    ax.set_theta_direction(-1)  # Set the direction to clockwise
    
    # Plot and fill the radar chart
    ax.fill(angles, values, 'teal', alpha=0.25)
    ax.plot(angles, values, 'o-', linewidth=2)
    
    # Set labels for the knowledge areas
    ax.set_thetagrids(np.degrees(angles[:-1]), knowledge_areas)

# Create sliders for each of the 11 knowledge areas
for area in knowledge_areas:
    maturity_levels[area] = st.slider(f"Select your maturity level for {area}:", 0, 5, maturity_levels[area])

# Convert the maturity levels to a list and append the first value to close the radar chart loop
values = list(maturity_levels.values()) + [list(maturity_levels.values())[0]]

# Set up the radar chart (polar plot) with Data Governance at the top
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Create the radar chart with the current values
create_radar_chart(ax, angles, values)

# Display the radar chart in the Streamlit app
st.pyplot(fig)
