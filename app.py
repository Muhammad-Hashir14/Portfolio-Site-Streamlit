import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_icon=":sparkles:",page_title="MyApp")


if "page" not in st.session_state:
    st.session_state["page"] = "about"

def about():
    st.markdown("""
    <h1 style='text-align: center; color: white;'> 
    <b>I'm </b><span style='color: #009688;'>Muhammad Hashir</span>
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("<h4 style = 'text-align: center; color: white; margin-top:-20px'> Data Scientist | AI Developer </h4>", unsafe_allow_html=True)
    st.write("------------------------------------------------------")
    
    # Adjust the relative widths of the columns to reduce the gap
    col1, col2 = st.columns([1, 1.5])  # First column is smaller, second is slightly larger
    col1.image("images/myimage.png")
    
    col2.markdown("""<p>Hi, I’m Muhammad Hashir, a passionate <span style="color: #009688;"><b>Data Scientist</b></span> and <span style="color: #009688;"><b>AI Developer</b></span> from Pakistan, 
                    currently pursuing a Bachelor's degree in Computer Science at <span style="color: #009688;"><b>Sindh Madressatul Islam Univesity</b></span>. 
                    Alongside my academic journey, I have successfully completed a 2-year certification in Artificial 
                    Intelligence from the Presidential Initiative for Artificial Intelligence & Computing (PIAIC), 
                    which has equipped me with a strong foundation in AI and data science.</p>""", unsafe_allow_html=True)
                    
    col2.markdown("""<p>In addition to my studies, I’m actively involved in freelancing, offering services on <span style="color: #009688;"><b>Fiverr</b></span>, 
                    where I’ve achieved the<span style="color: #009688;"><b> Level 1</b></span> Seller status. My work spans across Video Editing and AI-related 
                    services, with over 30+ satisfied international clients. This experience has allowed me to develop 
                    a versatile skill set and gain exposure to projects from all over the world.</p>""", unsafe_allow_html=True)
                    
    col2.markdown("""<p>Furthermore, I’ve had the opportunity to work as a Machine Learning Engineering Intern at <span style="color: #009688;"><b>Ecomile Monitor</b></span>, a reputable startup, where I contributed to the development of a fuel prediction model. 
                    This internship allowed me to apply my AI and machine learning knowledge to real-world challenges, 
                    further solidifying my expertise in the field.</p>""", unsafe_allow_html=True)
                    
    col2.markdown("""<p>I am constantly looking for opportunities to grow, expand my skill set, and make a meaningful 
                    impact through technology.</p>""", unsafe_allow_html=True)
    
def journey():

    st.markdown("<h1 style='text-align: center; color: #009688;'>My Journey</h1>", unsafe_allow_html=True)

    st.write("-------------------------------------------------------------------------------------")
    # Entry 5

    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.write("- Sep 2023")
    st.markdown("<h3 style = 'color: #009688; margin-top:-20px'>Joined Ecomile Monitor as ML Intern </h3>", unsafe_allow_html=True)
    st.write("During my internship at Ecomile Monitor, a startup under NEP NIC Karachi, I efficiently sourced and synthesized diverse data for comprehensive analysis. I executed meticulous data preprocessing to ensure data integrity and gained insights for contextual significance. Additionally, I applied advanced predictive modeling techniques to optimize fuel consumption forecasts, enhancing the startup's operational efficiency.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("--------------------------------------------------------------------------------------")

    
    # Entry 4
    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.write("- Feb 2022")
    st.markdown("<h3 style = 'color: #009688; margin-top:-20px'>Won GDSC Data Science Competition </h3>", unsafe_allow_html=True)
    st.write("I proudly won the GDSC Data Science Competition held at Sindh Madressatul Islam University during the Code Jam event. This experience was not only a significant learning opportunity but also a confidence booster, allowing me to apply my skills in a competitive environment and collaborate with talented peers.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("--------------------------------------------------------------------------------------")

    # Entry 3
    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.write("- March 2023")
    st.markdown("<h3 style = 'color: #009688; margin-top:-20px'>Joined Bytewise Limited Virtual Internship Program </h3>", unsafe_allow_html=True)
    st.write("Engaged in a virtual internship focused on data science, where I learned and implemented various tasks while creating projects based on the provided resources. This experience enhanced my practical skills in data analysis and problem-solving, preparing me for real-world challenges in the field.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("--------------------------------------------------------------------------------------")

    # Entry 4
    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.write("- June 2022")
    st.markdown("<h3 style = 'color: #009688; margin-top:-20px'>Joined PIAIC AI Certification Program </h3>", unsafe_allow_html=True)
    st.write("Participated in the PIAIC AI Certification program, where I gained hands-on experience in Python, data science, deep learning, and computer vision. This intensive program equipped me with the skills to analyze complex data, develop predictive models, and implement innovative AI solutions.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("--------------------------------------------------------------------------------------")

    # Entry 5
    st.markdown('<div class="timeline-entry">', unsafe_allow_html=True)
    st.write("- Feb 2022")
    st.markdown("<h3 style = 'color: #009688; margin-top:-20px'>Started BS Computer Science </h3>", unsafe_allow_html=True)
    st.write("Embarked on an exciting academic journey at Sindh Madressatul Islam University, where I developed a passion for technology and programming, fueling my interest in data science and artificial intelligence.")
    st.markdown('</div>', unsafe_allow_html=True)


with st.sidebar:
    st.markdown(
    """
    <div style='border: 2px solid #009688; border-radius: 10px; padding: 20px; background-color: #1a1a1a;'>
        <h1 style='text-align: center; color: #009688;'>Muhammad Hashir's</h1>
        <h4 style='text-align: right; color: white; margin-top: -20px; margin-right: 20px; font-style: italic'>Portfolio</h4>
    </div>
    """,
    unsafe_allow_html=True
)
    st.write("-------------------------------------------------------------------------")

    
    col1, col2 = st.columns([1, 1.5])  
    with col1:
        if st.button("About Me"):
            st.session_state["page"] = "about"

    with col2:
        if st.button("My Journey"):
            st.session_state["page"] = "journey"

if st.session_state["page"] == "about":
    about()

if st.session_state["page"] == "journey":
    journey()