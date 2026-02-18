import streamlit as st 
import sys
import os
from src.predict import predict_trend

st.set_page_config(page_title="Nifty Regime Detector")
st.title("Nifty Regime Detector")
st.write("Click below for current trend")

if st.button("Check Current Regime"):

    regime = predict_trend()

    st.subheader("Prediction Result")

    if regime == "Upward":
        st.success("Market Structure: UPWARD TREND")

    elif regime == "Downward":
        st.error("Market Structure: DOWNWARD TREND")

    else:
        st.warning("Market Structure: SIDEWAYS / CONSOLIDATION")