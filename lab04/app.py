
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Airbnb Price Predictor", page_icon="🏠", layout="centered")
@st.cache_resource
def load_model():
    return joblib.load("models/airbnb_price_pipeline.joblib")
model=load_model()

st.title("🏠 Airbnb Nightly Price Predictor")
st.write("Estimate the nightly price of a New York City Airbnb listing.")
st.caption("Model trained on the Kaggle NYC Airbnb Open Data (2019).")

col1,col2=st.columns(2)
with col1:
    borough=st.selectbox("Borough",["Manhattan","Brooklyn","Queens","Bronx","Staten Island"])
    neighbourhood=st.text_input("Neighbourhood","Midtown")
    room_type=st.selectbox("Room Type",["Entire home/apt","Private room","Shared room"])
    latitude=st.number_input("Latitude",40.50,40.95,40.75,format="%.5f")
    longitude=st.number_input("Longitude",-74.30,-73.65,-73.98,format="%.5f")
    minimum_nights=st.number_input("Minimum Nights",1,365,2)
with col2:
    number_of_reviews=st.number_input("Number of Reviews",0,1000,20)
    reviews_per_month=st.number_input("Reviews per Month",0.0,50.0,1.0,step=0.1)
    host_listings=st.number_input("Host Listings Count",1,1000,1)
    availability=st.number_input("Availability (days/year)",0,365,200)
    recency=st.number_input("Days Since Last Review",0,5000,60)
    has_reviews=st.selectbox("Has Reviews?",["Yes","No"])=="Yes"

if st.button("Predict Nightly Price", type="primary"):
    row=pd.DataFrame([{
        "neighbourhood_group":borough,"neighbourhood":neighbourhood,
        "latitude":latitude,"longitude":longitude,"room_type":room_type,
        "minimum_nights":minimum_nights,"number_of_reviews":number_of_reviews,
        "reviews_per_month":reviews_per_month,
        "calculated_host_listings_count":host_listings,
        "availability_365":availability,"review_recency_days":recency,
        "has_reviews":int(has_reviews)
    }])
    prediction=float(model.predict(row)[0])
    st.success(f"Estimated nightly price: ${prediction:,.0f}")
    st.info("This is an estimate, not a guaranteed market price.")
st.divider()
st.markdown("**Limitations:** The dataset is from 2019; prices, neighbourhood conditions, regulations, and demand can change over time.")
