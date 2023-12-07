import streamlit as st
from PIL import Image
import pickle
import pandas as pd

model = open('SA_File.pkl', 'rb')
classifier = pickle.load(model)

st.markdown("""
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  """, unsafe_allow_html= True)

titre = st.title('This is a sentiment analysis web application')
image = Image.open('sa_image.png')

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(image, caption='sentiment analysis')

with col3:
    st.write(' ')

sentiment = st.text_input('enter a sentence', '')
result =' '

button1 = """
  <div class="text-center mx-auto">
     <button type="submit" class="btn btn-primary">Predict</button>
  </div>
"""
st.markdown(button1, unsafe_allow_html=True)

df_test = pd.DataFrame([[sentiment]], columns= ['sentiment'])

def prediction(df_test):
    prediction = classifier.predict(df_test)
    print(prediction)
    return prediction
        
if st.button(button1):
     result = prediction(df_test)
     if result == 1 :
         print('positive')
     elif result == -1:
         print('negative')
     else:
         print('neutral')
