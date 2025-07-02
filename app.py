import streamlit as st
from bitvavo import Bitvavo

# Vul je eigen API key en secret in via Streamlit Secrets (zie stap 5)
bitvavo = Bitvavo({
    'APIKEY': st.secrets["bitvavo_api_key"],
    'APISECRET': st.secrets["bitvavo_api_secret"],
})

st.title("Bitvavo prijs check")

ticker = bitvavo.tickerPrice({"market": "BTC-EUR"})
st.write("BTC-EUR prijs:", ticker['price'])
