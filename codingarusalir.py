import streamlit as st
import math

# Fungsi untuk halaman Penjelasan
def halaman_penjelasan():
    st.header("💧 Penjelasan Debit Air")
    st.write("""
    **Debit air** adalah besarnya volume air yang mengalir dalam satu satuan waktu. Satuan umum:
    - Liter/detik (L/s)
    - Meter kubik/detik (m³/s)

    **Rumus umum:**

    ```text
    Debit = Luas Penampang Aliran × Kecepatan Aliran
    ```

    - Debit = Volume air per satuan waktu
    - Luas Penampang = luas area aliran (m²)
    - Kecepatan = kecepatan rata-rata aliran (m/s)
    """)

# Fungsi untuk halaman Pembahasan
def halaman_pembahasan():
    st.header("📘 Pembahasan")
    st.write("""
    Dalam teknik hidrologi atau sipil, debit air penting untuk:
    - Perencanaan irigasi
    - Analisis banjir
    - Perancangan saluran drainase

    ### Komponen Perhitungan:
    - **Luas Penampang Aliran:** bisa persegi, lingkaran, dll
    - **Kecepatan Aliran:** diukur dengan flowmeter atau pelampung

    **Pastikan satuan konsisten (meter dan detik)** agar hasil akurat.
    """)

# Fungsi untuk halaman Kalkulator
def halaman_kalkulator():
    st.header("🧮 Kalkulator Debit Air")

    bentuk = st.selectbox("Pilih Bentuk Penampang", ["Persegi Panjang", "Lingkaran"])

    if bentuk == "Persegi Panjang":
        lebar = st.number_input("Lebar Penampang (m)", min_value=0.0, format="%.2f")
        tinggi = st.number_input("Tinggi Air (m)", min_value=0.0, format="%.2f")
        luas = lebar * tinggi
    elif bentuk == "Lingkaran":
        diameter = st.number_input("Diameter Pipa (m)", min_value=0.0, format="%.2f")
        jari_jari = diameter / 2
        luas = math.pi * jari_jari ** 2

    kecepatan = st.number_input("Kecepatan Aliran (m/s)", min_value=0.0, format="%.2f")

    if st.button("Hitung Debit"):
        debit = luas * kecepatan
        st.success(f"Debit Air = {debit:.2f} m³/s")

# Fungsi untuk halaman Contoh Kasus
def halaman_contoh_kasus():
    st.header("📚 Contoh Kasus Perhitungan")

    st.subheader("Kasus 1: Saluran Persegi Panjang")
    st.write("""
    - Lebar: 2 meter  
    - Tinggi air: 1 meter  
    - Kecepatan: 1.5 m/s  

    → Luas = 2 × 1 = 2 m²  
    → Debit = 2 × 1.5 = **3.00 m³/s**
    """)

    st.subheader("Kasus 2: Pipa Lingkaran")
    st.write("""
    - Diameter: 0.5 meter  
    - Kecepatan: 2 m/s  

    → Luas = π × (0.25)² ≈ 0.196 m²  
    → Debit = 0.196 × 2 ≈ **0.39 m³/s**
    """)

# Navigasi halaman
st.set_page_config(page_title="Kalkulator Debit Air", layout="centered")

st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Penjelasan", "Pembahasan", "Kalkulator", "Contoh Kasus"])

if halaman == "Penjelasan":
    halaman_penjelasan()
elif halaman == "Pembahasan":
    halaman_pembahasan()
elif halaman == "Kalkulator":
    halaman_kalkulator()
elif halaman == "Contoh Kasus":
    halaman_contoh_kasus()
