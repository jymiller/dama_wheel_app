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

# Create a placeholder for the radar chart at the top of the page
chart_placeholder = st.empty()

# Calculate the angle for each knowledge area and adjust to start with Data Governance at the top
angles = np.linspace(0, 2 * np.pi, len(knowledge_areas), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Use Streamlit's session state to store and cache the maturity levels
if 'maturity_levels' not in st.session_state:
    st.session_state.maturity_levels = {area: 3 for area in knowledge_areas}

# Function to create the radar chart
def create_radar_chart(angles, values):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)  # Set the start to the top
    ax.set_theta_direction(-1)  # Set the direction to clockwise

    # Draw and fill the chart
    ax.fill(angles, values, 'teal', alpha=0.25)
    ax.plot(angles, values, 'o-', linewidth=2)

    # Set the labels for the knowledge areas
    ax.set_thetagrids(np.degrees(angles[:-1]), knowledge_areas)

    return fig

# Draw the initial radar chart
initial_values = list(st.session_state.maturity_levels.values()) + [list(st.session_state.maturity_levels.values())[0]]
initial_chart = create_radar_chart(angles, initial_values)
chart_placeholder.pyplot(initial_chart)

# Create sliders for each of the 11 knowledge areas and update the chart accordingly
for area in knowledge_areas:
    new_level = st.slider(f"Select your maturity level for {area}:", 0, 5, st.session_state.maturity_levels[area])
    if new_level != st.session_state.maturity_levels[area]:
        st.session_state.maturity_levels[area] = new_level
        # Update the chart only if there's a change in the slider value
        updated_values = list(st.session_state.maturity_levels.values()) + [list(st.session_state.maturity_levels.values())[0]]
        updated_chart = create_radar_chart(angles, updated_values)
        chart_placeholder.pyplot(updated_chart)
