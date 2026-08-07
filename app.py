import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("../MODELS/house_price_model.pkl", "rb"))

st.title("🏠 House Price Prediction")

area = st.number_input("Area", min_value=500)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)
stories = st.number_input("Stories", min_value=1)

mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])

parking = st.number_input("Parking", min_value=0)

prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["Furnished", "Semi-furnished", "Unfurnished"]
)

# Convert values exactly like LabelEncoder
mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

if furnishingstatus == "Furnished":
    furnishingstatus = 0
elif furnishingstatus == "Semi-furnished":
    furnishingstatus = 1
else:
    furnishingstatus = 2

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, stories,
                          mainroad, guestroom, basement,
                          hotwaterheating, airconditioning,
                          parking, prefarea, furnishingstatus]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")