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

# Kullanıcıdan şema ve tablo ismini alın
schema = st.text_input('Lütfen şema ismini giriniz:')
table = st.text_input('Lütfen tablo ismini giriniz:')

if schema and table:
    # Veritabanından verileri çekmek için SQL sorgusu
    query = f'SELECT * FROM {schema}.{table} LIMIT 10'

    # Sorguyu çalıştırın ve sonuçları bir pandas DataFrame'ine aktarın
    df = pd.read_sql(query, engine)
    df.to_excel('selam.xlsx')

    # Streamlit kullanarak dataframe'i görüntüleyin
    st.write(df)