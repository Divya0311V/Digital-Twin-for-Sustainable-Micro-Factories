import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="Digital Twin Dashboard", layout="wide")

st.title("Real-Time Digital Twin Monitoring System")

mode="static"

def load_data(file):
    if os.path.exists(file):
        try:
            return pd.read_csv(file)
        except:
            return pd.DataFrame()
    return pd.DataFrame()

alerts = load_data("live_alerts.csv")
sustainability = load_data("live_sustainability.csv")
energy_stats = load_data("live_energy_stats.csv")

st.subheader("Energy Statistics")

if not energy_stats.empty:
    st.dataframe(energy_stats, use_container_width=True)
else:
    st.warning("Waiting for live energy data...")

st.subheader("Machine Alerts")

if not alerts.empty:
    st.dataframe(alerts, use_container_width=True)
else:
    st.success("No alerts detected.")

st.subheader("Sustainability Score")

if not sustainability.empty:
    st.dataframe(sustainability, use_container_width=True)
else:
    st.warning("Waiting for sustainability data...")

st.rerun()
