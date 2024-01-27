# Gerekli kütüphaneleri import edin
import streamlit as st
import pandas as pd

# Kullanıcıdan bir dosya yüklemesini isteyin
uploaded_file = st.file_uploader("Pick a file")

if uploaded_file is not None:
    # Dosyayı bir pandas DataFrame'ine okuyun
    df = pd.read_excel(uploaded_file)
    print(df.columns)
    print(df.head())

    # İlk 10 satırı görüntüleyin
    st.write(df.head(10))