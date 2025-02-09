import streamlit as st
  
st.title('Siwakorn Putthanon, BDA')
st.info('Business Data Analyst with KPI development, dashboard design, and customer behavior analysis')
st.write('Hello world!')

linkedin_url = "https://www.linkedin.com/in/siwakorn-putthanon/"

# สร้างกรอบด้วย HTML และ CSS
st.markdown(
    f"""
    <div style="
        border: 2px solid #0077b5; 
        border-radius: 10px; 
        padding: 20px; 
        margin: 20px 0; 
        background-color: #f9f9f9; 
        text-align: center;">
        <a href="{linkedin_url}" target="_blank" 
           style="font-size: 20px; text-decoration: none; color: #0077b5;">
           LinkedIn Profile
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
