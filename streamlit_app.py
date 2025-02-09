import streamlit as st
from PIL import Image

try:
    img = Image.open("images/S__90898435.jpg")
    st.image(img)
except Exception as e:
    st.error(f"Error loading image: {e}")
  
st.title('🎈 Siwakorn Putthanon, BDA')
st.info('Business Data Analyst with KPI development, dashboard design, and customer behavior analysis', icon="ℹ️")
st.write('Hello world!')
