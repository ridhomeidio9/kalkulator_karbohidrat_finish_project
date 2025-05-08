import streamlit as st

st.set_page_config(page_title="Kalkulator Karbohidrat", layout="centered")

st.title("Kalkulator Kebutuhan Karbohidrat Harian")

berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("Tingkat Aktivitas Fisik Anda:", ["Ringan", "Sedang", "Berat"])

# Kalori per kg berdasarkan aktivitas
if aktivitas == "Ringan":
    kalori_per_kg = 25
elif aktivitas == "Sedang":
    kalori_per_kg = 30
else:
    kalori_per_kg = 35

# Persentase karbohidrat dari total energi
persentase_karbo_min = 0.45
persentase_karbo_max = 0.65

if st.button("Hitung Kebutuhan"):
    total_kalori = berat_badan * kalori_per_kg
    karbo_min = (total_kalori * persentase_karbo_min) / 4
    karbo_max = (total_kalori * persentase_karbo_max) / 4

    st.success(f"Kebutuhan kalori harian Anda: {total_kalori:.0f} kkal")
    st.info(f"Kebutuhan karbohidrat harian Anda: {karbo_min:.0f}–{karbo_max:.0f} gram")
