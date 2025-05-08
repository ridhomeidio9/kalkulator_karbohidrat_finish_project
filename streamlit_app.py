import streamlit as st

def halaman_beranda():
    st.title("Kebutuhan Karbohidrat Harian")
    st.markdown("""
        Selamat datang di kalkulator kebutuhan karbohidrat harian!

        Karbohidrat adalah sumber energi utama bagi tubuh. Jumlah kebutuhan karbohidrat harian seseorang tergantung dari usia, berat badan, dan tingkat aktivitas fisik.

        **Pedoman Umum:**
        - Energi harian: 25–30 kkal per kg berat badan
        - 45–65% dari total energi berasal dari karbohidrat
        - 1 gram karbohidrat = 4 kkal

        Silakan klik halaman **Kalkulator** di sidebar untuk mulai menghitung kebutuhan Anda.
    """)

def halaman_kalkulator():
    st.title("Kalkulator Kebutuhan Karbohidrat Harian")

    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0, step=0.5)
    aktivitas = st.selectbox("Tingkat Aktivitas Fisik Anda:", ["Ringan", "Sedang", "Berat"])
    
    if aktivitas == "Ringan":
        kalori_per_kg = 25
    elif aktivitas == "Sedang":
        kalori_per_kg = 30
    else:
        kalori_per_kg = 35

    persentase_karbo_min = 0.45
    persentase_karbo_max = 0.65

    if st.button("Hitung Kebutuhan"):
        total_kalori = berat_badan * kalori_per_kg
        karbo_min = (total_kalori * persentase_karbo_min) / 4
        karbo_max = (total_kalori * persentase_karbo_max) / 4

        st.success(f"Kebutuhan kalori harian Anda: {total_kalori:.0f} kkal")
        st.info(f"Kebutuhan karbohidrat harian Anda: {karbo_min:.0f}–{karbo_max:.0f} gram")

# Sidebar navigasi
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Kalkulator"])

if halaman == "Beranda":
    halaman_beranda()
else:
    halaman_kalkulator()
