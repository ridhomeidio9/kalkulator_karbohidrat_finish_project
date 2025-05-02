import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kalkulator Karbohidrat Harian", layout="centered")

def hitung_kebutuhan_karbo(berat_badan, tingkat_aktivitas):
    faktor_aktivitas = {
        "Rendah (sedentari)": 4,
        "Sedang (aktivitas ringan - sedang)": 5,
        "Tinggi (aktivitas berat)": 6
    }
    kebutuhan = berat_badan * faktor_aktivitas[tingkat_aktivitas]
    return kebutuhan

with st.sidebar:
    selected = option_menu("Navigasi", ["Kalkulator", "Informasi Karbohidrat"],
                           icons=["calculator", "info-circle"], default_index=0)

if selected == "Kalkulator":
    st.title("🧮 Kalkulator Karbohidrat Harian")
    st.markdown("Hitung kebutuhan karbohidrat harian berdasarkan berat badan dan aktivitas.")

    berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1, max_value=300, step=1)
    aktivitas = st.selectbox("Pilih tingkat aktivitas fisik Anda:", 
                             ["Rendah (sedentari)", "Sedang (aktivitas ringan - sedang)", "Tinggi (aktivitas berat)"])

    if st.button("Hitung"):
        kebutuhan = hitung_kebutuhan_karbo(berat, aktivitas)
        st.success(f"Kebutuhan karbohidrat harian Anda adalah sekitar **{kebutuhan} gram** per hari.")
        st.caption("Sumber: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya)")

elif selected == "Informasi Karbohidrat":
    st.title("🍚 Informasi Kebutuhan Karbohidrat")
    st.image("https://cdn.alodokter.com/raw/upload/alodokter/shutterstock_1032429234_1.jpg", use_column_width=True)
    st.markdown("""
### Berapa Banyak Karbohidrat yang Dibutuhkan?
Menurut **Alodokter**, jumlah karbohidrat yang dibutuhkan setiap orang berbeda-beda tergantung:
- Berat badan
- Tingkat aktivitas fisik
- Kondisi kesehatan

Rata-rata, kebutuhan karbohidrat per hari:
- **Sedentari**: 4 gram/kg berat badan
- **Aktivitas ringan-sedang**: 5 gram/kg
- **Aktivitas berat**: 6 gram/kg

### Contoh Sumber Karbohidrat Sehat:
- Nasi merah
- Kentang
- Oatmeal
- Roti gandum utuh
- Buah-buahan dan sayuran
- Kacang-kacangan

> Karbohidrat merupakan sumber energi utama, tapi penting untuk memilih karbohidrat kompleks dan berserat tinggi.

📚 Baca selengkapnya: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya)
""")
