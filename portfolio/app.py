from pathlib import Path
import streamlit as st
from PIL import Image

# """ path settings """

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV(1).pdf"
profile_pic = current_dir / "assets" / "profile_photo.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Zaamouche Zakaria Hachem"
PAGE_ICON = ":wave:"
NAME = "Zaamouche Zakaria Hachem"
DESCRIPTION = """
Data Scientist and Machine Learning Engineer.
"""
EMAIL = "hachemzaamouche99@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/hachem-zaamouche-060784255",
    "Github": "https://github.com/HachemZakaria"
}
PROJECTS = {
    "🏆 Use of Machine Learning and Natural Language Processing techniques for sentiment analysis in tweets",
    "🏆 Exploration and collection of website data using Web Scraping",
    "🏆 Creating Wine Prediction application using streamlit",
    "🏆 Creating a tourism website interface for a tunisian tourist guide",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic).rotate(-90)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250, use_column_width='auto')

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 Years experience in machine learning and data science
- ✔️ Strong hands on experience and knowledge in Python and Excel and word
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Java, JavaScript, Python (Scikit-learn, Pandas, Numpy,...), SQL
- 📊 Data Visulization: Matplotlib, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decition trees, RandomForest, K-means
- 🗄️ Databases: MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Extracting Data using web scraping | Bachelor degree project**")
st.write("06/2020")
st.write(
    """
- ► Explorating websites and collecting their data using Web Scraping tools and libraries such as : BeautifulSoup
"""
)
st.write("---")
# --- JOB 2
st.write("🚧", "**Sentiments Analysis Project | Master degree project**")
st.write("06/2022")
st.write(
    """
- ► Carry out a project that consists of collecting tweets from a university community on Twitter and classifying them according to their emotions (positive, negative, neutral), using Machine Learning and Deep Learning techniques, and displaying these classifications through an application website
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")