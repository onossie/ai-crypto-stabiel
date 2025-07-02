import streamlit as st
from bitvavo import Bitvavo

st.title("AI Crypto Trading App - Bitvavo")

api_key = st.text_input("API Key")
api_secret = st.text_input("API Secret", type="password")

if api_key and api_secret:
    bitvavo = Bitvavo({
        'APIKEY': api_key,
        'APISECRET': api_secret,
        'RESTURL': 'https://api.bitvavo.com/v2',
        'WSURL': 'wss://ws.bitvavo.com/v2/',
        'DEBUGGING': False
    })
    try:
        balance = bitvavo.balance()
        st.write("Balance:")
        st.write(balance)
    except Exception as e:
        st.error(f"API error: {e}")
else:
    st.info("Voer je API Key en Secret in om te beginnen.")