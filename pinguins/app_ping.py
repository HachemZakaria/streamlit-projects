import streamlit as st
import numpy as np
import pandas as pd
import pickle 
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguins predictions app
         
This app predict the **Palmer Penguins** species

data obtained from the [PlmerPenguins library](https://github.com/allisonhorst/palmerpenguins) in R by allison horst
""")

st.sidebar.header('User input features')

st.sidebar.markdown("""
[Example csv input file]()
""")

upload_file = st.sidebar.file_uploader('Upload your csv file', type=['csv'])
if upload_file is not None:
    input_df = pd.read_csv(upload_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
        sex = st.sidebar.selectbox('Sex', ('male', 'female'))
        bill_length_mm = st.sidebar.slider('bill length (mm)', 32.1, 59.6, 43.9)
        bill_depth_mm = st.sidebar.slider('bill depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider('flipper length (mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.sidebar.slider('body mass (mm)', 2700.0, 6300.0, 4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1]

st.subheader('User Input features')

if upload_file is not None:
    st.write(df)
else:
    st.write('awaiting csv file to be uploaded')
    st.write(df)


load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)