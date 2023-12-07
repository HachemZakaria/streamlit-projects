import streamlit as st
import pickle
import pandas as pd

st.write('this is melb_app')

df = pd.read_csv('melb_data.csv')
df.head()

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

html_temp = """
    <div style ="background-color:yellow;padding:13px;">
    <h1 style ="color:black;text-align:center; font-size:35px;">Application for melbourne's houses prices</h1>
    </div>
    """

st.markdown(html_temp, unsafe_allow_html = True)

col1, col2, col3 = st.columns(3)

type = col1.text_input('type')
method = col1.text_input('method')
region = col1.text_input('regionname')
rooms = col1.number_input('rooms')
distance = col1.number_input('distance')
postcode = col2.number_input('postcode')
bedroom2 = col2.number_input('bedroom2')
bathroom = col2.number_input('bathroom')
car = col2.number_input('car')
landsize = col2.number_input('landsize')
buildingarea = col3.number_input('buildingarea')
yearbuilt = col3.number_input('yearbuilt')
latittude = col3.number_input('latittude')
longtitude = col3.number_input('longtitude')
propertycount = col3.number_input('propertycount')
result =''

df_test = pd.DataFrame([[type, method, region, rooms, distance, postcode, bedroom2, bathroom, car, landsize, buildingarea, yearbuilt, latittude, longtitude, propertycount]],

columns= ['Type', 'Method', 'Regionname', 'Rooms', 	'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car', 	'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude', 'Propertycount'])

def prediction(df_test):
    prediction = classifier.predict(df_test)
    print(prediction)
    return prediction

if st.button("Predict"):
        result = prediction(df_test)
st.success('The output is {}'.format(result))