# Gerekli kütüphaneleri import edin
import os
from dotenv import load_dotenv
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

# .env dosyasını yükleyin
load_dotenv()

# Veritabanı bağlantı bilgilerini çevre değişkenlerinden alın
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_DATABASE")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
PORT = os.getenv("DB_PORT")

# Kullanıcıdan bir schema ve tablo seçmesini isteyin
schemas = ['cimri', 'akakce', 'twitch']  # Buraya schema isimlerini ekleyin
selected_schema = st.selectbox("Pick a schema", schemas)

tables = ['product_metric', 'product_metric', 'streamer_chat']  # Buraya tablo isimlerini ekleyin
selected_table = st.selectbox("Pick a table", tables)

# Veritabanı bağlantısını oluşturun
database_connection_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
engine = create_engine(database_connection_string)

# Seçilen schema ve tablodan verileri çekmek için SQL sorgusu
query = f'SELECT * FROM {selected_schema}.{selected_table} LIMIT 10'

# Sorguyu çalıştırın ve sonuçları bir pandas DataFrame'ine aktarın
df = pd.read_sql(query, engine)

# Streamlit kullanarak dataframe'i görüntüleyin
st.write(df)


chart = alt.Chart(df).mark_line().encode(
    x='product_price',
    y='scrape_date'
)
st.altair_chart(chart)

plt.hist(df['product_price'], bins=20)
plt.title('Histogram')
st.pyplot()