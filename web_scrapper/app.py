import streamlit as st
from bs4 import BeautifulSoup
import requests
import webbrowser

st.markdown("""<h1 style='text-align: center; '>Web Scrapper</h1> """, unsafe_allow_html=True)

with st.form('Search'):
    keyword = st.text_input('enter your text')
    search = st.form_submit_button('Search')

placeholder = st.empty
if keyword :
    page = requests.get(f"https://unsplash.com/fr/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_="ripi6")
    col1, col2 = st.columns(2)
    print(len(rows))
    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img", class_="tB6UZ a5VGX")
            list = img["srcset"].split("?")
            anchor = figures[i].find("a", class_="rEAWd")
            print(anchor['href'])
            if i == 0:
                col1.image(list[0])
                btn = col1.button("download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])
            else:
                col2.image(list[0])
                btn = col2.button("download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])