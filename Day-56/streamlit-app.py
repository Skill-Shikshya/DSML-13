import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

txt = st.text_area(
    "Text to analyze"
)
st.write(f"You wrote {len(txt)} characters.")
