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

original_title = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 20px;">Rozhe la dayk bunt peroz bi salwaaa, salwa xoshtrin rozhe mna chunka awro rozhe tua awro rozhe jwantrin u sweet trin kasa la hamu dniaa loya amn darem awro xoshtrin rozha la hamu dniaa, salwa ager bmawe wasfi bashi tu bkam qat natanm chunka awanda bashi awanda bashi nak bas yak website ba millonana websitesh natanm salwa, salwa xoshtrin waxtakani zhyanm lagal tu bua chunka taka sarchawe xoshi la zhyani mn u hamu jare darem alhamdullah ka atu la zhianmi u bajde zhyanm zor zor naxosh dabu be tu, har chrkak qsa krdn lagal tu lo mn handi 20 sal dl xoshi bua, bajde nazanm ku har supasisht bkam u padashtt bdamawa 😭😭, salwa ka datbinm pe dakani dlm zor zor pr dabe la xoshian jare wa haya grianm de la xoshian u atu ba pekanint hamu dnia runak dakay jare chawtt mashalla mashalla bajde zor zor jwana zoor briqadara wchi mang, u wa3dt pe dadam ka hamu hawli xom bdam har la xoshi btherm u qat qat naxoshi nabini u har shtaki naxosha hata peshman hawl dadam be away hastish pe bkay laydam la peshman u hamu hamu sht dakam bas ta ba pekanin btbinm, u salwa atu lo mn taybat trin kasi yakam sht labar away amn darem family > bradar u nafare de, amn atush ba yakak la family xom dadanem u dwam sht chunka amn atum halbzhardia wchi future wife, u inehallah inshalla aw shta dabta rasti, salwa amn atum halbzhard chunka dazanm bash dabe lom chunka dazanm malm runak dakaiawa chunka dazanm qat dlm nashkeni chunka dazanm qat xamm nadye chunka dazanm dakaki bash dabe lo mndalakanm u dazanm lagal tu bm mndalaknm xoshtrin zhyan dazhin chunka amn qat qat dlian nashkenm u be nazian nakam u chian bwe loyan dakam u dazanm atush awha dabe lagalian u amnish awam dawe, salwa loya ba kurti darem damawe pr ba dl damawe zhyanm hamu lagal tu bi u lagal tu bzhim u hamu tamanm lagal tu basar bbam u a3elak danem ka nmunay bashi u nmunay axlaq bi, u dazanm a3elaki awha bas lagal tu dakre bass chunka atu baxot way ❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤</p>'

st.markdown(original_title, unsafe_allow_html=True)

original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 50px;"> </p>'
st.markdown(original_title1, unsafe_allow_html=True)


st.audio(r"aa.mp3")

original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Black; font-size: 30px;">shayani zor lawash zyatri hamu dniam ❤️</p>'
st.markdown(original_title1, unsafe_allow_html=True)
original_title1 = '<p style="font-family: Arial, sans-serif; font-weight: bold; color: Red; font-size: 30px;">❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤</p>'
st.markdown(original_title1, unsafe_allow_html=True)
