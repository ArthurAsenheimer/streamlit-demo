import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")



df = pd.read_csv("AAPL_TRADES_1MIN.csv", index_col=False).loc[:,['date', 'close']].set_index('date') #.iloc[-10_000:]
st.line_chart(df)

