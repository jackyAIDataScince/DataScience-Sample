import streamlit as st
import pandas as pd

df = pd.read_csv("https://github.com/MaartenGr/boardgame/raw/master/files/boardgame_new.csv").head()
st.write(df)
