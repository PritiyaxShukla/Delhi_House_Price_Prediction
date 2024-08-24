import streamlit as st
import pickle
model = pickle.load(open('random_forest_model.pkl','rb'))
import pandas as pd

st.title("DELHI HOUSE PRICE PREDICTOR BY PRITIYAX SHUKLA")


st.image('images (3).jpg')

data = pd.read_csv('Cleaned_delhi_data.csv')

Address_option = data['Address'].unique()
area_option = data['area'].unique()
Bathrooms_option = data['Bathrooms'].unique()
Status_option = data['Status'].unique()
neworold_option = data['neworold'].unique()
parking_option = data['parking'].unique()
type_of_building_option = data['type_of_building'].unique()
BHK_option = data['BHK'].unique()

Address = st.selectbox("Enter the Address", Address_option)
st.write("You have selected the address:", Address)

area = st.selectbox('Enter the Area (in square feet)', area_option)
st.write("You have selected the area:", area)

Bathrooms = st.selectbox("Enter the Number of Bathrooms", Bathrooms_option)
st.write("You have selected the number of bathrooms:", Bathrooms)

Status = st.selectbox("Select the Construction Status", Status_option)
st.write("You have selected the construction status:", Status)

neworold = st.selectbox("Select the Property Type", neworold_option)
st.write("You have selected the property type:", neworold)

parking = st.selectbox('Enter the Number of Parking Spaces', parking_option)
st.write("You have selected the number of parking spaces:", parking)

type_of_building = st.selectbox("Select the Type of Building", type_of_building_option)
st.write("You have selected the type of building:", type_of_building)

BHK = st.selectbox("Enter the Number of Bedrooms", BHK_option)
st.write("You have selected the number of bedrooms (BHK):", BHK)


feature_names = ['Address','area','Bathrooms','Status','neworold','parking','type_of_building','BHK']


input_data = [Address,area,Bathrooms,Status,neworold,parking,type_of_building,BHK]

input_df = pd.DataFrame([input_data],columns=feature_names)

# prediction




#Display
if st.button("Predict"):
    result = model.predict(input_df)
    st.write(f"Predicted House Price :{result[0]}")