import streamlit as st
import streamlit.components.v1 as components

st.set_page_config( 
     page_title="EmissioNavi", 
     page_icon="💚", 
     layout="wide", 
     initial_sidebar_state="expanded", 
 ) 
hide_default_format = """ 
        <style> 
        #MainMenu {visibility: show; } 
        footer {visibility: hidden;} 
        </style> 
        """ 
st.markdown(hide_default_format, unsafe_allow_html=True) 

def gradient_text(text, color1, color2):
    gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 42px;
    """
    return f'<span style="{gradient_css}">{text}</span>'

color1 = "#0d3270"
color2 = "#0fab7b"
text = "EmissioNavi"
  
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("images/logo.png", width=250)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)
  
st.markdown(""" 
 #### Welcome to EmissioNavi - Where Transportation Meets Environmental Responsibility

1. **Commute Insight**: Calculate and reduce your carbon footprint for your daily commute using simple machine learning algorithms.
              
2. **Trans Sustain**: Log and manage your environmental impact while shipping and commuting using Machine learning algorithms: Logistic Regression and Decision Tree Classifier.
   
3. **Carbon Graph**: Illuminating global carbon footprints through interactive data visualizations.
 """)

footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/harshavardhan-bajoria/" target="_blank">Harshavardhan Bajoria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
