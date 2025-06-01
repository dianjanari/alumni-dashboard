import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Alumni", layout="wide")
st.title("📋 Dashboard Data Alumni")

@st.cache_data
def load_data():
    data = {
        "Nama": ["Andi Pratama"],
        "Email": ["andi@example.com"],
        "No HP": ["081234567890"],
        "Domisili": ["Yogyakarta"],
        "Tanggal Lahir": ["1995-07-10"],
        "Program Studi": ["Teknik Industri"],
        "Tahun Lulus": [2018],
        "Pekerjaan": ["Quality Control Engineer"],
        "Instansi": ["PT Maju Sejahtera"],
        "Jabatan": ["QC Supervisor"],
        "Tahun Masuk Kerja": [2019],
        "Pengalaman Sebelumnya": ["Internship at PT XYZ"],
        "Klaster Minat": ["Industri, Kewirausahaan"]
    }
    df = pd.DataFrame(data)
    return df

alumni_df = load_data()

st.sidebar.header("🔍 Filter Data")
tahun = st.sidebar.multiselect("Tahun Lulus", options=alumni_df['Tahun Lulus'].unique())
kota = st.sidebar.multiselect("Domisili", options=alumni_df['Domisili'].unique())
prodi = st.sidebar.multiselect("Program Studi", options=alumni_df['Program Studi'].unique())

filtered_df = alumni_df.copy()
if tahun:
    filtered_df = filtered_df[filtered_df['Tahun Lulus'].isin(tahun)]
if kota:
    filtered_df = filtered_df[filtered_df['Domisili'].isin(kota)]
if prodi:
    filtered_df = filtered_df[filtered_df['Program Studi'].isin(prodi)]

st.markdown("### 📑 Data Alumni")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown("### 📊 Ringkasan")
st.write("Total Alumni Terdata:", alumni_df.shape[0])
