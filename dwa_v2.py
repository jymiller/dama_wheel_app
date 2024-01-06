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

# Initialize an empty dictionary to hold the maturity levels
maturity_levels = {area: 3 for area in knowledge_areas}  # Default level is set to 3

# Calculate the angle for each knowledge area and adjust to start with Data Governance at the top
angles = np.linspace(0, 2 * np.pi, len(knowledge_areas), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Set up the radar chart (polar plot) with Data Governance at the top
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)  # Set the start to the top
ax.set_theta_direction(-1)  # Set the direction to clockwise

# Draw the initial plot (will be updated with user input)
values = [3] * len(knowledge_areas)  # Default values
values += values[:1]  # Complete the loop
ax.fill(angles, values, 'teal', alpha=0.25)
ax.plot(angles, values, 'o-', linewidth=2)
ax.set_thetagrids(np.degrees(angles[:-1]), knowledge_areas)

# Display the radar chart in the Streamlit app
st.pyplot(fig)

# Create sliders for each of the 11 knowledge areas and update the chart accordingly
for area in knowledge_areas:
    maturity_levels[area] = st.slider(f"Select your maturity level for {area}:", 0, 5, 3)

# Update the values for the radar chart with the input from the sliders
values = list(maturity_levels.values()) + [list(maturity_levels.values())[0]]
ax.clear()  # Clear the previous plot
ax.fill(angles, values, 'teal', alpha=0.25)
ax.plot(angles, values, 'o-', linewidth=2)
ax.set_thetagrids(np.degrees(angles[:-1]), knowledge_areas)

# Redisplay the updated radar chart in the Streamlit app
st.pyplot(fig)
