import streamlit as st 
import time
from streamlit_autorefresh import st_autorefresh
from src.predict import predict_trend

st.set_page_config(page_title="Nifty Regime Detector")
st.title("Nifty Regime Detector")
placeholder = st.empty()
st_autorefresh(interval = 6000, key= "refresh")

regime = predict_trend()

with placeholder.container():
    if regime == "Upward":
        st.success("Market Structure: UPWARD TREND")

    elif regime == "Downward":
        st.error("Market Structure: DOWNWARD TREND")

    else:
        st.warning("Market Structure: SIDEWAYS / CONSOLIDATION")

    st.caption("Auto refresh in 15 sec")