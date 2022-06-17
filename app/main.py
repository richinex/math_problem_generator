import streamlit as st
from utils import read_data, head, body, set_bg

st.set_page_config(
    page_title='Math Problem Generator',
    page_icon='assets/icon.png'
)

set_bg('assets/background1.jpg')

head()

if st.button('Bring it on!'):
    df =  read_data('data/olympiad_problems.csv')
    choice = df.sample(1)
    body(choice)