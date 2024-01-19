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

original_title = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 20px;">SALWAAA rozhe la daykbunt peroz be mashallaa buya 17 sal bas heshta per but pewa dyar nia, inshallah 17 salit zor la salakani de xoshtr dabe u hamu sht ba dle xot dabe u dur dabe la nafare xrap, salwa atu zor sht buy lo mn la zor sht yarmatimt da  ka brasti kas naykrd u shanazit pewa dakam u atu taka kchi ka bradarmi chunka kas nia wchi tu awha jey siqa bi, qat nabua qsaki bkam laknt u ley pashiman bbmawa chunka har ba jde zor jey siqay, 7azm krd awjara ba shewaki jyawaz pet blem loya aw websitem drust krd hewadarm ba dlt be, ba zor drezhay pe nadam ba nusin AI bram tawaw daka ❤️❤️ </p>'

st.markdown(original_title, unsafe_allow_html=True)

original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 50px;">👇</p>'
st.markdown(original_title1, unsafe_allow_html=True)


st.audio(r"bb.mp3")

original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 30px;">shayani zor lawash zyatri ❤️</p>'
st.markdown(original_title1, unsafe_allow_html=True)
