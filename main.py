import streamlit as st
import time
import base64

st.set_page_config(page_title="SALWA", layout="wide")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(r'aaa.png')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer {

	visibility: hidden;

	}
footer:after {
	content:'Made by Blnd'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("""
<style>
.big-font {
    font-size: 60px !important;
    color: black !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🥳 Happy birthday 🥳</p>', unsafe_allow_html=True)


st.balloons()
st.balloons()
st.balloons()

original_title = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 20px;">On this special day, I find myself compelled to express the warmth and joy that your presence brings into my life. As the calendar marks another year of your existence, I want to take a moment to celebrate the incredible person that you are. Your laughter is like a melody that brightens even the dullest days, and your kindness is a beacon of light in a world that sometimes feels overwhelming. From the sparkle in your eyes to the sincerity in your smile, every aspect of you radiates a unique charm that captivates my heart. Birthdays are not just a celebration of the passing of time; they are an opportunity to reflect on the beautiful soul that graces this world with its presence You dear are that beautiful soul. Your passion, resilience, and genuine nature inspire me daily I appreciate the way you navigate through life with grace, facing challenges with courage, and embracing joy with an open heart. Your dreams are like constellations in the night sky, guiding you towards a future filled with promise and possibility </p>'

st.markdown(original_title, unsafe_allow_html=True)

original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 50px;">👇</p>'
st.markdown(original_title1, unsafe_allow_html=True)


st.audio(r"bb.mp3", format="audio/*")

original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 30px;">shayani zor lawash zyatri ❤️</p>'
st.markdown(original_title1, unsafe_allow_html=True)
