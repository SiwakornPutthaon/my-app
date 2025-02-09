import streamlit as st
  
st.title('Siwakorn Putthanon, BDA')
st.info('Business Data Analyst with KPI development, dashboard design, and customer behavior analysis')
st.write('Hello world!')

linkedin_url = "https://www.linkedin.com/in/siwakorn-putthanon"

st.write("Link Profile and Caption Bio: LinkedIn")

if st.button("LinkedIn Profile"):
    js = f"window.open('{linkedin_url}', '_blank');"
    html = f"<script>{js}</script>"
    st.markdown(html, unsafe_allow_html=True)
