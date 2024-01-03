#
# Purpose: This is a Streamlit app that displays a DMM Assessment Chart
# Re-written by: John Y Miller
#
# Date: 2021-09-01


# Import the required libraries
import streamlit as st
import plotly.express as px
import pandas as pd

# st.set_page_config(layout="wide")

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



# Divide the page into Five columns with custom widths
col1_width = 0.50
col2_width = 0.20
col3_width = 0.15
col4_width = 0.15
col1, col2, col3, col4 = st.columns([col1_width, col2_width, col3_width, col4_width])

# col1_width = 0.45
# col2_width = 0.50
# col3_width = 0.20
# col4_width = 0.15
# col5_width = 0.15
# col1, col2, col3, col4, col5 = st.columns([col1_width, col2_width, col3_width, col4_width, col5_width])


local_image_path = "data_wheel_image_2017.png"  # Replace with the URL of your image
    # Initialize a list to store desired rank slider values
desired_rank_values = []
   # Initialize a list to store current rank slider values
current_rank_values = []




# Content for the third column
with col3:
    #st.header("Current Rank")
    st.markdown("<h3 style='font-size: 18px;margin-top: 0px;'>Current Rank</h3>", unsafe_allow_html=True)
    # Initialize a list to store current rank slider values
    current_rank_values = []
    
    # Create sliders dynamically for each theta for Current Rank
    for i, theta in enumerate(['Data Gov', 'Data Arch', 'Data Model', 'Storage', 'Security', 'Integration', 'Content Mgmt', 'Master Data', 'DW/BI', 'Metadata', 'DQ']):
        col_slider, col_label = st.columns([3, 1])  # Adjust the ratio based on your preference
        current_rank = col_slider.slider(f'{theta}', 1, 5, 2, label_visibility="collapsed")#
        #col_label.markdown("")  # Empty column for the label to align with the slider
        current_rank_values.append(current_rank)

# Content for the fourth column
with col4:
    #st.header("Desired Rank")
    st.markdown("<h3 style='font-size: 18px;margin-top: 0px;'>Desired Rank</h3>", unsafe_allow_html=True)


    # Initialize a list to store desired rank slider values
    desired_rank_values = []

    # Create sliders dynamically for each theta for Desired Rank
    for i, theta in enumerate(['Data Gov', 'Data Arch', 'Data Model', 'Storage', 'Security', 'Integration', 'Content Mgmt', 'Master Data', 'DW/BI', 'Metadata', 'DQ']):
        col_slider, col_label = st.columns([3, 1])  # Adjust the ratio based on your preference
        desired_rank = col_slider.slider(f'{theta}', 1, 5, 5, label_visibility="collapsed")#,  label_visibility="collapsed"
        
        #col_label.markdown("")  # Empty column for the label to align with the slider
        desired_rank_values.append(desired_rank)



with col2:
    table_data = {
        "": ['Data Governance','', 'Data Architecture','', 'Data Modeling & Design','', 'Data Storage & Operations','', 'Data Security','', 'Data Integration & Interoperability','', 'Document & Content Management','', 'Reference & Master Data','', 'Data Warehousing & Business Intelligence','', 'Metadata','', 'Data Quality'],
    }
    
    df_table = pd.DataFrame(table_data)
    # Display the table with the given information
   
    # st.table(df_table.style.set_table_styles([
    # {'selector': 'td', 'props': [('font-size', '7pt')]}
    # ]).format({"Current Rank": "{:.1f}", "Desired Rank": "{:.1f}"}))
    st.markdown("<h3 style='font-size: 18px;margin-top: -20px;'></h3>", unsafe_allow_html=True)

    st.data_editor(df_table,hide_index=True,width=1150,height=800)
# Content for the first column
with col1:
 #   st.image('blank.jpg', width=30)
    
 #   st.image(local_image_path, width=300)  # Load data wheel image

   
    # Create DataFrames using the slider values
    df_current_rank = pd.DataFrame(dict(
        r=current_rank_values,
        theta=['Data Governance', 'Data Architecture', 'Data Modeling & Design', 'Data Storage & Operations', 'Data Security', 'Data Integration & Interoperability', 'Document & Content Management', 'Reference & Master Data', 'Data Warehousing & Business Intelligence', 'Metadata', 'Data Quality'],
        color=['CR'] * 11
    ))

    df_desired_rank = pd.DataFrame(dict(
        r=desired_rank_values,
        theta=['Data Governance', 'Data Architecture', 'Data Modeling & Design', 'Data Storage & Operations', 'Data Security', 'Data Integration & Interoperability', 'Document & Content Management', 'Reference & Master Data', 'Data Warehousing & Business Intelligence', 'Metadata', 'Data Quality'],
        color=['DR'] * 11
    ))

    df_combined = pd.concat([df_current_rank, df_desired_rank], ignore_index=True)
    fig = px.line_polar(df_combined, r='r', theta='theta', width=450, height=450, line_close=True, color='color', color_discrete_map={'CR': 'orange', 'DR': 'blue'})
    st.markdown("<h3 style='font-size: 18px; text-align: center;'>DMM Assessment Chart</h3>", unsafe_allow_html=True)
    # Customize the layout to move the legend on top and center
    fig.update_layout(
        legend=dict(
            orientation="h",  # Set the orientation to horizontal
            yanchor="bottom",
            y=1.15,  # Adjust the y-coordinate to move the legend up
            xanchor="center",  # Center the legend horizontally
            x=0.5  # Center the legend horizontally
        )
    )

    # Display the chart with the legend centered on top
    st.plotly_chart(fig, use_container_width=True)
  
    levels_description = """
    -  Level 0: Absence of capability
    -  Level 1: Initial or Ad Hoc
    -  Level 2: Repeatable
    -  Level 3: Defined
    - Level 4: Managed
    - Level 5: Optimized
    """

    st.write(levels_description)
  
