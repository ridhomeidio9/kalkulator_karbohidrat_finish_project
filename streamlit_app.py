import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Karbohidrat Harian", layout="centered")

# Fungsi: Hitung kebutuhan karbohidrat harian
def hitung_kebutuhan_karbo(berat_badan, tingkat_aktivitas):
    faktor_aktivitas = {
        "Rendah (sedentari)": 4,
        "Sedang (aktivitas ringan - sedang)": 5,
        "Tinggi (aktivitas berat)": 6
    }
    kebutuhan = berat_badan * faktor_aktivitas[tingkat_aktivitas]
    return kebutuhan

# Navigasi menggunakan radio di sidebar
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih halaman:", ["Kalkulator", "Informasi Karbohidrat"])

# Halaman Kalkulator
if halaman == "Kalkulator":
    st.title("🧮 Kalkulator Karbohidrat Harian")
    st.markdown("Hitung kebutuhan karbohidrat harian berdasarkan berat badan dan aktivitas.")

    berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1, max_value=300, step=1)
    aktivitas = st.selectbox("Pilih tingkat aktivitas fisik Anda:", 
                             ["Rendah (sedentari)", "Sedang (aktivitas ringan - sedang)", "Tinggi (aktivitas berat)"])

    if st.button("Hitung"):
        kebutuhan = hitung_kebutuhan_karbo(berat, aktivitas)
        st.success(f"Kebutuhan karbohidrat harian Anda adalah sekitar **{kebutuhan} gram** per hari.")
        st.caption("Sumber: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya)")

# Halaman Informasi
elif halaman == "Informasi Karbohidrat":
    st.title("🍚 Informasi Kebutuhan Karbohidrat")
    st.image("https://cdn.alodokter.com/raw/upload/alodokter/shutterstock_1032429234_1.jpg", use_column_width=True)
    
    st.markdown("""
### Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat

Berikut adalah beberapa contoh makanan yang kaya akan karbohidrat beserta jumlah karbohidrat dalam setiap porsinya:

""")
    
    # Daftar makanan dan karbohidrat
    makanan = [
        ("Nasi Merah (150g)", 35),
        ("Kentang (150g)", 30),
        ("Oatmeal (40g)", 27),
        ("Roti Gandum Utuh (40g)", 20),
        ("Quinoa (185g setelah dimasak)", 39),
        ("Pasta Gandum Utuh (200g setelah dimasak)", 40),
        ("Pisang (118g)", 27),
        ("Kacang-kacangan (40g)", 20),
        ("Sereal (30g)", 20),
        ("Jagung (100g)", 19)
    ]
    
    # Menampilkan daftar makanan dan karbohidrat
    for item in makanan:
        st.markdown(f"**{item[0]}**: {item[1]} gram karbohidrat")
    
    st.markdown("""
> Pilih makanan yang sesuai dengan kebutuhan karbohidrat Anda, dan pastikan untuk memadukan dengan sumber makanan lain agar pola makan lebih seimbang.

📚 Baca selengkapnya: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya)
""")
