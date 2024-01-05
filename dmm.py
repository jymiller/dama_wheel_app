#
# Purpose: This is a Streamlit app that displays a DMM Assessment Chart
# Re-written by: John Y Miller
#
# Date: 2024-01-04


# Import the required libraries
import streamlit as st
import plotly.express as px
import pandas as pd

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



# Divide the page into three columns with custom relative widths
col1, col2, col3 = st.columns([4,1,1])

# Content for the Current Values 
with col2:
   
    st.markdown("<h3 style='font-size: 18px;margin-top: 0px;'>Current Rank</h3>", unsafe_allow_html=True)
   
    # Initialize a list to store current rank slider values
    #current_rank_values = []
    current_rank_values = [1,1,1,1,1,1,1,1,1,1,1]

    # Create sliders dynamically for each theta for Current Rank
    # for i, theta in enumerate(
    #        ['Data Governance', 'Data Architecture', 'Data Modeling & Design', 'Data Storage & Operations', 'Data Security', 'Data Integration & Interoperability', 'Document & Content Management', 'Reference & Master Data', 'Data Warehousing & Business Intelligence', 'Metadata', 'Data Quality']):
           
    #     col_slider, col_label = st.columns([3, 1])  # Adjust the ratio based on your preference
        
    #     current_rank = col_slider.slider(f'{theta}', 1, 5, 1, label_visibility="visible")#
        
    #     current_rank_values.append(current_rank)

# Content for the Desired Values
with col3:
    
    st.markdown("<h3 style='font-size: 18px;margin-top: 0px;'>Desired Rank</h3>", unsafe_allow_html=True)

    # Initialize a list to store desired rank slider values
    desired_rank_values = []

    # Create sliders dynamically for each theta for Desired Rank
    for i, theta in enumerate(
        
     #   ['Data Gov', 'Data Arch', 'Data Model', 'Storage', 'Security', 'Integration', 'Content Mgmt', 'Master Data', 'DW/BI', 'Metadata', 'DQ']):
        ['Data Governance', 'Data Architecture', 'Data Modeling & Design', 'Data Storage & Operations', 'Data Security', 'Data Integration & Interoperability', 'Document & Content Management', 'Reference & Master Data', 'Data Warehousing & Business Intelligence', 'Metadata', 'Data Quality']):

        col_slider, col_label = st.columns([3, 1])  # Adjust the ratio based on your preference
        desired_rank = col_slider.slider(f'{theta}', 1, 5, 5, label_visibility="visible")#,  label_visibility="collapsed"
        
        #col_label.markdown("")  # Empty column for the label to align with the slider
        desired_rank_values.append(desired_rank)


 
# Content for the middle Chart
with col1:
   
    # Create DataFrames using the slider values
    df_current_rank = pd.DataFrame(dict(
        r=current_rank_values,
        theta=['Data Governance', 'Data Architecture', 'Data Modeling & Design', 'Data Storage & Operations', 'Data Security', 'Data Integration & Interoperability', 'Document & Content Management', 'Reference & Master Data', 'Data Warehousing & Business Intelligence', 'Metadata', 'Data Quality'],
        color=['Current'] * 11
    ))

    df_desired_rank = pd.DataFrame(dict(
        r=desired_rank_values,
        theta=['Data Governance', 'Data Architecture', 'Data Modeling & Design', 'Data Storage & Operations', 'Data Security', 'Data Integration & Interoperability', 'Document & Content Management', 'Reference & Master Data', 'Data Warehousing & Business Intelligence', 'Metadata', 'Data Quality'],
        color=['Future'] * 11
    ))

    df_combined = pd.concat([df_current_rank, df_desired_rank], ignore_index=True)
    
   # st.write(df_combined)
    
    st.markdown("<h3 style='font-size: 18px; text-align: center;'>DMM Assessment Chart</h3>", unsafe_allow_html=True)

    fig = px.line_polar(
        df_combined, 
        r='r', 
        theta='theta', 
        #width=, height=450, 
        line_close=True, 
        color='color', 
        color_discrete_map={'Current': 'orange', 'Future': 'blue'})
        
    # Customize the layout to move the legend on top and center
    fig.update_layout(
        legend=dict(
            orientation="h",  # Set the orientation to horizontal
            yanchor="bottom",
            y=-0.25,  # Adjust the y-coordinate to move the legend up
            xanchor="center",  # Center the legend horizontally
            x=0.5  # Center the legend horizontally
            
        )
    )

    # Make the plot responsive - doesn't actually work with streamlit!
    # fig.update_layout(autosize=True)
   # fig.update_layout(angularaxis_visible=False)

    # Display the chart with the legend centered on top
    st.plotly_chart(fig, use_container_width=True,config={"staticPlot": True})
  
  

    levels_description = """
    Level 0: Absence of capability\n
    Level 1: Initial or \tAd Hoc\f
    Level 2: Repeatable\n
    Level 3: Defined\n
    Level 4: Managed\n
    Level 5: Optimized
    """

    st.write(levels_description)
    
  
    st.markdown("<h3 style='text-align: left'>Level 0: Absence of capability</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right'>Level 1: Initial or Ad Hoc</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center'>Level 2: Repeatable</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center'>Level 3: Defined</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center'>Level 4: Managed</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center'>Level 5: Optimized</h3>", unsafe_allow_html=True)
  
