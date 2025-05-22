import streamlit as st
from MRDS.main import run_mrds
import pandas as pd

st.title("📊 MRDS - Market Research Data Synthesizer")
topic = st.text_input("Enter product/topic:", "Samsung Galaxy S24")

if st.button("Analyze"):
    with st.spinner("Running agents..."):
        sentiments, insights = run_mrds(topic)
        df = pd.DataFrame(sentiments)
        st.subheader("Sentiment Breakdown")
        st.bar_chart(pd.Series(insights))

        st.subheader("Detailed Tweets and Sentiment")
        st.dataframe(df)
