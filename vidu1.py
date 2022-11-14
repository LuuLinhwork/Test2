import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import numpy as np 
import plotly.express as px  # pip install plotly-express
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

st.title (":hibiscus: Hình ảnh cửa hàng")
st.write ('Vui lòng chọn cửa hàng')

tab1, tab2, tab3 =  st.tabs(["CHANNEL", "DIOR", "GUCCI"])

with tab1:
   st.header("CHANNEL") 
   Channel_pic = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Test2\\channel.jpg')
   st.image(Channel_pic, width=700)

with tab2:
   st.header("DIOR") 
   Dior_pic = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Test2\\Dior.jpg')
   st.image(Dior_pic, width=700)

with tab3:
   st.header("GUCCI") 
   Gucci_pic = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Test2\\Gucci.jpg')
   st.image(Gucci_pic, width=700)



def title (url):
    st.markdown(f'<p style="background-color:#E5E4E2;color:#A0522D;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
title('chọn cửa hàng')






