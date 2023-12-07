import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("""<h1 style="text-align: center;">Image Editor</h1> """, unsafe_allow_html=True)
st.markdown(""" --- """)

upload_img = st.file_uploader("upload your image", type=['jpg', 'png'])
st.markdown(""" --- """)
info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if upload_img is not None:
    img = Image.open(upload_img)
    info.markdown("""<h1 style="text-align: center;">Informations</h1> """, unsafe_allow_html=True)
    size.markdown(f"<h6>size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>mode: {img.mode}</h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6>format: {img.format}</h6>", unsafe_allow_html=True)
    st.markdown("""<h1 style="text-align: center;">Resizing</h1> """, unsafe_allow_html=True)
    st.markdown(""" --- """)
    width = st.number_input("image width", value = img.width)
    height = st.number_input("image height", value = img.height) 
    st.markdown("""<h1 style="text-align: center;">Rotation</h1> """, unsafe_allow_html=True)
    st.markdown(""" --- """)
    rotation = st.number_input("degree")
    filters = st.selectbox("filters", options=['None', 'Blur', 'Detail', 'Emboss', 'Smooth'])
    btn_s = st.button("submit")
    if btn_s:
        edited = img.resize((width, height)).rotate(rotation)
        filtered = edited
        if filters != "None":
            if filters == "Blur":
                filtered = edited.filter(BLUR)
            elif filters == "Detail":
                filtered = edited.filter(DETAIL)
            elif filters == "Emboss":
                filtered = edited.filter(EMBOSS)
            else:
                filtered = edited.filter(SMOOTH)
        st.image(filtered)
            


