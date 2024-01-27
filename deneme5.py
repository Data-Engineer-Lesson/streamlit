# Gerekli kütüphaneleri import edin
import streamlit as st
import pandas as pd
import altair as alt

# Kullanıcıdan bir dosya yüklemesini isteyin
uploaded_file = st.file_uploader("Pick a file")

if uploaded_file is not None:
    # Dosyayı bir pandas DataFrame'ine okuyun
    df = pd.read_excel(uploaded_file)

    # İlk 10 satırı görüntüleyin
    st.write(df.head(10))

    # Kullanıcıdan bir evcil hayvan seçmesini isteyin
    pets = df['name'].unique().tolist()  # 'name' sütunundaki benzersiz değerleri alın
    pet = st.radio("Pick a pet", pets)

    # Seçilen evcil hayvanın verilerini filtreleyin
    pet_data = df[df['name'] == pet]

    # Altair ile bir grafik oluşturun
    chart = alt.Chart(pet_data).mark_bar().encode(
        x='scrape_date:T',
        y='regular_price:Q'
    )
    st.altair_chart(chart)

    # Kullanıcıdan bir renk seçmesini isteyin
    color = st.color_picker("Pick a color")

    # Kullanıcıdan bir tarih seçmesini isteyin
    scrape_date = st.date_input("Pick a scrape date")
    if scrape_date:
        # Seçilen tarihe ait verileri filtreleyin
        date_data = df[df['scrape_date'] == pd.to_datetime(scrape_date)]
        st.write(date_data)

    # Kullanıcıdan bir sayı aralığı seçmesini isteyin
    min_price, max_price = st.slider("Pick a price range", 0, 100, (25, 75))
    if min_price and max_price:
        # Seçilen fiyat aralığındaki verileri filtreleyin
        price_data = df[(df['regular_price'] >= min_price) & (df['regular_price'] <= max_price)]
        st.write(price_data.head(10))