import streamlit as st
import pandas as pd

st.title("Network Monitoring Dashboard")

data = pd.read_csv("data/network_logs.csv")

st.dataframe(data.head())

st.line_chart(data["Latency"])

st.line_chart(data["Throughput"])

st.bar_chart(data["Label"].value_counts())
