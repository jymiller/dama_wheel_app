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

# Calculate the angle for each knowledge area
angles = np.linspace(0, 2 * np.pi, len(knowledge_areas), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Function to create the radar chart
def create_radar_chart(angles, current_values, desired_values):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Set the axes limit
    ax.set_ylim(0, 5.5)

    # Plot current and desired values
    ax.plot(angles, current_values, 'o-b', linewidth=2, label='Current Maturity')
    ax.fill(angles, current_values, 'blue', alpha=0.1)
    ax.plot(angles, desired_values, 'o-r', linewidth=2, label='Desired Maturity')
    ax.fill(angles, desired_values, 'red', alpha=0.1)

    # Adjusted and multiline labels
    adjusted_labels = [
        "Data\nGovernance", "Data Modeling\n& Design", "Data Storage\n& Operations",
        "Data\nSecurity", "Data Integration\n& Interoperability", "Document & Content\nManagement",
        "Reference &\nMaster Data", "Data Warehousing\n& Business Intelligence",
        "Metadata", "Data\nQuality", "Data\nArchitecture"
    ]

    # Calculate positions for each label based on the angle and a specified radius
    label_radius = 6.5  # Radius to position labels (should be greater than the chart's max value)
    for i, label in enumerate(adjusted_labels):
        angle_rad = angles[i]
        ax.text(np.radians(np.degrees(angle_rad)), label_radius, label,
                horizontalalignment='center', size=10, color='black', weight='bold')

    # Remove original axis labels
    ax.set_xticks([])

    # Position the legend below the chart
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

    return fig




# Set up the columns layout
col1, space1, col2, space2, col3 = st.columns([3, 1, 3, 1, 6])

# Initialize the current and desired maturity levels with default values
current_maturity = {area: 3 for area in knowledge_areas}
desired_maturity = {area: 4 for area in knowledge_areas}

# Create sliders for current maturity
with col1:
    st.markdown("### Current Maturity")
    for area in knowledge_areas:
        current_maturity[area] = st.slider(f"Current maturity for {area}:", 0, 5, 3)

# Create sliders for desired maturity
with col2:
    st.markdown("### Desired Maturity")
    for area in knowledge_areas:
        desired_maturity[area] = st.slider(f"Desired maturity for {area}:", 0, 5, 4)

# Convert the maturity levels to lists and append the first values to close the radar chart loop
current_values = list(current_maturity.values()) + [list(current_maturity.values())[0]]
desired_values = list(desired_maturity.values()) + [list(desired_maturity.values())[0]]

# Create the radar chart in the right column
with col3:
    chart = create_radar_chart(angles, current_values, desired_values)
    st.pyplot(chart)
