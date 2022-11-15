import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

st.title (":hibiscus: Hình ảnh cửa hàng")
st.write ('Vui lòng chọn cửa hàng')

tab1, tab2, tab3 =  st.tabs(["CHANNEL", "DIOR", "GUCCI"])

with tab1:
   def header(url):
      st.markdown(f'<p style="background-color:#FDFEFE ;color:#4A235A;font-size:42px;border-radius:0%;">{url}</p>', unsafe_allow_html=True)
   header('CHANNEL') 
   
   Channel_pic = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Test2\\channel.jpg')
   st.image(Channel_pic, width=700)

#st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)

with tab2:
   DIOR = '<p style="font-family:sans-serif; color:#909497; font-size: 36px;">DIOR</p>'
   st.markdown(DIOR, unsafe_allow_html=True)
   
   Dior_pic = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Test2\\Dior.jpg')
   st.image(Dior_pic, width=700)
   

with tab3:
   GUCCI = '<p style="font-family:sans-serif; color:#F1C40F; font-size: 36px;">GUCCI</p>'
   st.markdown(GUCCI, unsafe_allow_html=True)
   
   Gucci_pic = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Test2\\Gucci.jpg')
   st.image(Gucci_pic, width=700)
   


#def title (url):
#    st.markdown(f'<p style="background-color:#E5E4E2;color:#A0522D;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
#title('chọn cửa hàng')

#def header(url):
#      st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)

#st.markdown(f'<h1 style="color:#33ff33;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)




