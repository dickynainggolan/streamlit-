import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Dashboard Elektro – Analisis Daya Listrik")


st.header("Perhitungan dan Visualisasi Daya Listrik")


st.subheader("Data Peralatan Elektronik Rumah Tangga")

=
st.text(
    "Aplikasi ini digunakan untuk menampilkan data beberapa "
    "peralatan elektronik beserta tegangan, arus, dan daya listriknya. "
    "Daya listrik dihitung menggunakan rumus P = V × I."
)


st.caption("Bidang Elektro – Kelistrikan Dasar")


data = {
    "Peralatan": ["Lampu", "Kipas Angin", "Televisi", "Rice Cooker", "Setrika"],
    "Tegangan (V)": [220, 220, 220, 220, 220],
    "Arus (A)": [0.3, 0.5, 0.8, 1.5, 2.0]
}

df = pd.DataFrame(data)


df["Daya (Watt)"] = df["Tegangan (V)"] * df["Arus (A)"]


st.subheader("Tabel Data Listrik")
st.dataframe(df)


st.subheader("Rumus Perhitungan Daya Listrik")
st.code("""
# Rumus daya listrik
P = V * I

# Contoh perhitungan
tegangan = 220  # Volt
arus = 0.5      # Ampere
daya = tegangan * arus
print(daya)
""", language="python")


st.subheader("Grafik Daya Listrik Peralatan")

fig, ax = plt.subplots()
ax.bar(df["Peralatan"], df["Daya (Watt)"])
ax.set_xlabel("Peralatan")
ax.set_ylabel("Daya (Watt)")
ax.set_title("Perbandingan Daya Listrik")

st.pyplot(fig)


