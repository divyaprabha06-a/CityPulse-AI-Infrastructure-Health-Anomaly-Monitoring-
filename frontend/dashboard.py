import streamlit as st
import pandas as pd

st.set_page_config(page_title="CityPulse AI Dashboard", layout="wide")

st.title("🏙️ CityPulse AI – Infrastructure Health Dashboard")

df = pd.read_csv("data/processed/health_report.csv")

st.subheader("Infrastructure Health Data")
st.dataframe(df)

st.subheader("Health Status Summary")
st.bar_chart(df["health_status"].value_counts())

for asset in df["asset_id"].unique():
    asset_df = df[df["asset_id"] == asset]
    latest = asset_df.iloc[-1]

    st.markdown(f"""
    ### Asset {asset}
    - Health Score: {latest['health_score']}
    - Status: {latest['health_status']}
    - Issues: {latest['issues']}
    """)
