import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu



st.set_page_config(page_title='Dashboard', page_icon='💹', layout='wide')
st.subheader('Elsaeed Company - **P&L - ( 30 June )** :money_with_wings:')
st.markdown('##')

df = pd.read_excel('P&L-30-06.xlsx')
df.index =df['Type']

#site_list = df['المشروع'].unique()


st.sidebar.image('data/logo.png', caption='Online Analytics')
#st.sidebar.header('Filter')

st.write(df)


#gross_contracting = df[df['Type'] == {'Revenues (Net)' or 'Cost of sales'}]
gross_contracting = df.loc['Revenues (Net)']
st.write('this is Revenue' ,gross_contracting)
