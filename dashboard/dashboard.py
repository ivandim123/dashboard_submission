import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Analisis Bisnis dari Dataset E-Commerce Olist")
st.markdown("Dashboard ini menampilkan visualisasi data pelanggan dan pesanan produk.")

# Membaca data dari file CSV
try:
    customers_df = pd.read_csv("dashboard/customer_data.csv")
    orders_df = pd.read_csv("dashboard/order_product_data.csv")
except FileNotFoundError:
    st.error("File CSV tidak ditemukan! Pastikan 'customers_data.csv' dan 'order_product_data.csv' ada di direktori yang sama.")
    st.stop()

# Sidebar dengan logo, sumber dataset, dan filter
st.sidebar.image("dashboard/olist.png", use_container_width=True)  # Logo di atas sidebar
st.sidebar.markdown("**Sumber Dataset:** [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")  # Sumber dataset

# Sidebar untuk filter (opsional)
st.sidebar.header("Filter Data")
top_n_cities = st.sidebar.slider("Jumlah Kota Teratas", min_value=5, max_value=50, value=20)
top_n_categories = st.sidebar.slider("Jumlah Kategori Produk Teratas", min_value=5, max_value=50, value=20)

# Chart 1: Jumlah Pelanggan per 20 Kota Teratas
st.subheader("Jumlah Pelanggan per Kota Teratas")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.countplot(
    data=customers_df, 
    x="customer_city", 
    order=customers_df["customer_city"].value_counts().index[:top_n_cities],
    palette="viridis",  # Palet warna menarik
    edgecolor="black",  # Garis tepi untuk definisi
    ax=ax1
)
plt.title(f"Jumlah Pelanggan per {top_n_cities} Kota Teratas", fontsize=14, pad=20)
plt.xlabel("Kota", fontsize=12)
plt.ylabel("Jumlah Pelanggan", fontsize=12)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.tight_layout()
st.pyplot(fig1)

# Gabungkan data kalau perlu (asumsi ada 'customer_id' untuk merge)
# Jika tidak ada relasi, kita langsung pakai orders_df
st.subheader("Kategori Produk Teratas Berdasarkan Pesanan")
fig2, ax2 = plt.subplots(figsize=(10, 8))
sns.barplot(
    x=orders_df["product_category_name"].value_counts().head(top_n_categories).values, 
    y=orders_df["product_category_name"].value_counts().head(top_n_categories).index,
    palette="magma",  # Palet warna yang lebih hidup
    edgecolor="black",  # Garis tepi untuk kontras
    ax=ax2
)
plt.title(f"{top_n_categories} Kategori Produk Teratas", fontsize=14, pad=20)
plt.xlabel("Jumlah Pemesanan", fontsize=12)
plt.ylabel("Kategori Produk", fontsize=12)
plt.tight_layout()
st.pyplot(fig2)

# Menampilkan Data Mentah (Opsional)
if st.checkbox("Tampilkan Data Mentah"):
    st.write("Data Pelanggan:")
    st.dataframe(customers_df)
    st.write("Data Pesanan Produk:")
    st.dataframe(orders_df)

# Footer
st.markdown("---")
st.markdown("Dibuat dengan menggunakan Streamlit")