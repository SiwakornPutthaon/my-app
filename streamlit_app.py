import streamlit as st
  
st.title('Siwakorn Putthanon, BDA')
st.info('Business Data Analyst with KPI development, dashboard design, and customer behavior analysis')
st.write('Hello world!')

# Replace with your actual LinkedIn profile URL
linkedin_url = "https://www.linkedin.com/in/siwakorn-putthanon"

if st.button("LinkedIn Profile"):
    # JavaScript to open the URL in a new tab
    js = f"window.open('{linkedin_url}', '_blank');"
    # Inject the JavaScript code into the app
    html = f"<script>{js}</script>"
    st.markdown(html, unsafe_allow_html=True) 
