# Gerekli kütüphaneleri import edin
import os
from dotenv import load_dotenv
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# .env dosyasını yükleyin
load_dotenv()

# Veritabanı bağlantı bilgilerini çevre değişkenlerinden alın
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_DATABASE")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
PORT = os.getenv("DB_PORT")

# Veritabanı bağlantısını oluşturun
database_connection_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
engine = create_engine(database_connection_string)

# Kullanıcıdan SQL sorgusunu alın
query = st.text_area('Lütfen SQL sorgunuzu giriniz:')

if query:
    # Sorguyu çalıştırın ve sonuçları bir pandas DataFrame'ine aktarın
    df = pd.read_sql(query, engine)

    # Streamlit kullanarak dataframe'i görüntüleyin
    st.write(df)