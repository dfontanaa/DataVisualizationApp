# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:19:23 2022

@author: danilo
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
dt = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

# page config
st.set_page_config(page_title='Data Visualization App', 
                   page_icon=':bar_chart:',
                   layout="wide",
                   initial_sidebar_state='expanded')
hide_data = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_data, unsafe_allow_html=True)

plot_options = ['scatter', 'line', 'area', 'bar', 'funnel', 'timeline', 'pie', 'sunburst', 'treemap', 'icicle', 'funnel_area', 'histogram', 'box', 'violin', 'strip', 'ecdf', 'density_heatmap', 'density_contour', 'scatter_3d', 'line_3d', 'scatter_matrix', 'parallel_coordinates', 'parallel_categories', 'scatter_mapbox', 'line_mapbox', 'choropleth_mapbox', 'density_mapbox', 'scatter_geo', 'line_geo', 'choropleth', 'scatter_polar', 'line_polar', 'bar_polar', 'scatter_ternary', 'line_ternary']

# read data and convert to df
@st.cache
def read_df(filepath):
    filename = filepath.name
    if filename.endswith('csv'):
        df = pd.read_csv(filepath)
    elif filename.endswith('xlsx'):
        df = pd.read_excel(filepath)
    else:
        st.write('Not a recognized file....')
        df = pd.read_csv(filepath)
    return df

# dataframe view page
def page_df():
    st.header('Preview DataFrame', anchor='PreviewDF')
    datacolumns = st.multiselect('Select columns to export', (df.columns))
    
    if len(datacolumns) < 1:  
        st.dataframe(df)
    else:
        ndf = df[datacolumns]
        st.dataframe(ndf)
        
        # Save filtered data
        csv = convert_df(ndf)
        st.download_button(
             label="Download filtered data as CSV",
             data=csv,
             file_name='FilteredData_%s.csv'%dt,
             mime='text/csv')
    
    # Investigate data
    st.write('---')
    raw_data = st.text_input('Filter data with expression')
    if len(raw_data) == 0:
        pass
    else:
        st.write(eval(raw_data))
    

# convert file for export
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# plot page - 3 canvas
def page_plot():
    st.header('Plot Data', anchor='PlotData')
    
    # canvas 1
    c1, c2, c3 = st.columns(3)
    plt_option = c1.selectbox('Select plot option', plot_options, index=1, key='p1')
    xvalue = c2.selectbox('Select data for x axis', (df.columns), key='p2')
    yvalue = c3.multiselect('Select data for y axis', (df.columns), default = df.columns[0], key='p3')
    
    if len(yvalue) == 1:
        yvalue = yvalue[0]
    elif len(yvalue) == 0:
        yvalue = xvalue
    else:
        pass
    
    if 'scatter' in plt_option:
        mplt = px.scatter(data_frame=df, x=xvalue, y=yvalue)
    elif 'line' in plt_option:
        mplt = px.line(data_frame=df, x=xvalue, y=yvalue)
    elif 'area' in plt_option:
        mplt = px.area(data_frame=df, x=xvalue, y=yvalue)
    elif 'bar' in plt_option:
        mplt = px.bar(data_frame=df, x=xvalue, y=yvalue)
    else:
        st.write('plot format not available yet...')
        mplt = px.scatter(data_frame=df, x=xvalue, y=yvalue)
    
    st.plotly_chart(mplt, use_container_width=True)
    
    # canvas 2
    c4, c5, c6 = st.columns(3)
    plt_option2 = c4.selectbox('Select plot option', plot_options, index=1, key='p4')
    xvalue2 = c5.selectbox('Select data for x axis', (df.columns), key='p5')
    yvalue2 = c6.multiselect('Select data for y axis', (df.columns), default = df.columns[0], key='p6')
    
    if len(yvalue2) == 1:
        yvalue2 = yvalue2[0]
    elif len(yvalue2) == 0:
        yvalue2 = xvalue2
    else:
        pass
    
    if 'scatter' in plt_option2:
        mplt2 = px.scatter(data_frame=df, x=xvalue2, y=yvalue2)
    elif 'line' in plt_option2:
        mplt2 = px.line(data_frame=df, x=xvalue2, y=yvalue2)
    elif 'area' in plt_option2:
        mplt2 = px.area(data_frame=df, x=xvalue2, y=yvalue2)
    elif 'bar' in plt_option2:
        mplt2 = px.bar(data_frame=df, x=xvalue2, y=yvalue2)
    else:
        st.write('plot format not available yet...')
        mplt2 = px.scatter(data_frame=df, x=xvalue2, y=yvalue2)
    
    st.plotly_chart(mplt2, use_container_width=True)
    
    # canvas 3
    c7, c8, c9 = st.columns(3)
    plt_option3 = c7.selectbox('Select plot option', plot_options, index=1, key='p7')
    xvalue3 = c8.selectbox('Select data for x axis', (df.columns), key='p8')
    yvalue3 = c9.multiselect('Select data for y axis', (df.columns), default = df.columns[0], key='p9')
    
    if len(yvalue3) == 1:
        yvalue3 = yvalue3[0]
    elif len(yvalue3) == 0:
        yvalue3 = xvalue3
    else:
        pass
    
    if 'scatter' in plt_option3:
        mplt3 = px.scatter(data_frame=df, x=xvalue3, y=yvalue3)
    elif 'line' in plt_option3:
        mplt3 = px.line(data_frame=df, x=xvalue3, y=yvalue3)
    elif 'area' in plt_option3:
        mplt3 = px.area(data_frame=df, x=xvalue3, y=yvalue3)
    elif 'bar' in plt_option3:
        mplt3 = px.bar(data_frame=df, x=xvalue3, y=yvalue3)
    else:
        st.write('plot format not available yet...')
        mplt3 = px.scatter(data_frame=df, x=xvalue3, y=yvalue3)
    
    st.plotly_chart(mplt3, use_container_width=True)
    

################################################################################################################################################
# Main Window
st.title('Data Visualization App')

# Sidebar
file_sel = None
with st.sidebar:
    st.title('Data Loader Section')
    # File loader
    uploaded_files = st.file_uploader("Select file(s)", type=['csv','xlsx'], accept_multiple_files=True, key='FileLoader')
    if uploaded_files is not None:
        allfiles = {}
        for uploaded_file in uploaded_files:
            allfiles[uploaded_file.name] = uploaded_file
            
        # File Selection
        file_sel = st.selectbox('Select File for analysis', (allfiles.keys()))
        
    else:
        st.stop()
        
    # Enable loading
    load_flag = st.checkbox('Load Data')
    if file_sel is not None:
        if load_flag:
            # Read data
            df = read_df(allfiles[file_sel])            
            
            # plot pages
            pages = {'Preview data': page_df,
                     'Plot data': page_plot}
            
            # select page
            selected_page = st.selectbox('Choose page', pages.keys())
            
            if 'Plot data' in selected_page:
                n1, n2 = st.columns(2)
                add_canvas = n1.button('Add Canvas')
                remove_canvas = n2.button('Remove Canvas')
                
               
# Main page        
if file_sel is not None:
    if load_flag:
        pages[selected_page]()
        