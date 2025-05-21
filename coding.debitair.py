import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Debit Air", layout="centered")

# Navigasi halaman
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Penjelasan", "Pembahasan", "Kalkulator", "Contoh Kasus"])

# -------------------------
# Halaman Penjelasan
# -------------------------
def halaman_penjelasan():
    st.header("💧 Penjelasan Debit Air")
    st.write("""
    **Debit air** adalah volume air yang mengalir dalam satu satuan waktu. Satuan umum:
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

# -------------------------
# Halaman Pembahasan
# -------------------------
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

# -------------------------
# Halaman Kalkulator
# -------------------------
def halaman_kalkulator():
    st.header("🧮 Kalkulator Debit Air")
    st.write("Hitung debit air berdasarkan dua metode:")

    metode = st.radio("Pilih Metode Perhitungan:", 
                      ("Volume dan Waktu", "Luas Penampang dan Kecepatan"))

    st.divider()

    # Metode 1
    if metode == "Volume dan Waktu":
        st.subheader("Metode 1: Volume dan Waktu")

        volume = st.number_input("Masukkan Volume Air", min_value=0.0, step=0.01)
        volume_unit = st.selectbox("Satuan Volume", ("m³", "Liter"))

        waktu = st.number_input("Masukkan Waktu", min_value=0.0, step=0.01)
        waktu_unit = st.selectbox("Satuan Waktu", ("Detik", "Menit", "Jam"))

        if st.button("Hitung Debit (Q)", key="volwaktu"):
            if volume_unit == "Liter":
                volume_m3 = volume / 1000
            else:
                volume_m3 = volume

            if waktu_unit == "Detik":
                waktu_s = waktu
            elif waktu_unit == "Menit":
                waktu_s = waktu * 60
            else:
                waktu_s = waktu * 3600

            if waktu_s == 0:
                st.error("Waktu tidak boleh 0.")
            else:
                debit_m3s = volume_m3 / waktu_s
                debit_ls = debit_m3s * 1000

                st.success("Hasil Perhitungan:")
                st.write(f"**Debit Air:** {debit_m3s:.6f} m³/s")
                st.write(f"**Debit Air:** {debit_ls:.2f} L/s")

                with st.expander("📘 Langkah Perhitungan"):
                    st.markdown(f"""
                    - Volume: `{volume}` {volume_unit} = `{volume_m3}` m³  
                    - Waktu: `{waktu}` {waktu_unit} = `{waktu_s}` detik  
                    - Rumus: `Q = V / t`  
                    - Q = `{volume_m3} / {waktu_s}` = `{debit_m3s:.6f}` m³/s = `{debit_ls:.2f}` L/s
                    """)

    # Metode 2
    else:
        st.subheader("Metode 2: Luas Penampang dan Kecepatan")

        bentuk = st.selectbox("Pilih Bentuk Penampang", ("Lingkaran (Pipa)", "Persegi Panjang"))

        if bentuk == "Lingkaran (Pipa)":
            diameter = st.number_input("Masukkan Diameter Pipa (m)", min_value=0.0, step=0.001)
            radius = diameter / 2
            luas = math.pi * (radius ** 2)

        else:  # Persegi Panjang
            lebar = st.number_input("Masukkan Lebar Saluran (m)", min_value=0.0, step=0.001)
            kedalaman = st.number_input("Masukkan Kedalaman Air (m)", min_value=0.0, step=0.001)
            luas = lebar * kedalaman

        kecepatan = st.number_input("Kecepatan Aliran Air (m/s)", min_value=0.0, step=0.01)

        if st.button("Hitung Debit (Q)", key="luaskecepatan"):
            debit_m3s = luas * kecepatan
            debit_ls = debit_m3s * 1000

            st.success("Hasil Perhitungan:")
            st.write(f"**Luas Penampang:** {luas:.6f} m²")
            st.write(f"**Debit Air:** {debit_m3s:.6f} m³/s")
            st.write(f"**Debit Air:** {debit_ls:.2f} L/s")

            with st.expander("📘 Langkah Perhitungan"):
                if bentuk == "Lingkaran (Pipa)":
                    st.markdown(f"""
                    - Diameter = `{diameter}` m → jari-jari = `{radius:.3f}` m  
                    - Luas = π × r² = `{math.pi:.5f} × {radius:.3f}²` = `{luas:.6f}` m²  
                    """)
                else:
                    st.markdown(f"""
                    - Luas = lebar × kedalaman = `{lebar} × {kedalaman}` = `{luas:.6f}` m²  
                    """)
                st.markdown(f"""
                - Kecepatan = `{kecepatan}` m/s  
                - Rumus: `Q = A × v`  
                - Q = `{luas:.6f} × {kecepatan}` = `{debit_m3s:.6f}` m³/s = `{debit_ls:.2f}` L/s
                """)

# -------------------------
# Halaman Contoh Kasus
# -------------------------
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

# -------------------------
# Tampilkan halaman
# -------------------------
if halaman == "Penjelasan":
    halaman_penjelasan()
elif halaman == "Pembahasan":
    halaman_pembahasan()
elif halaman == "Kalkulator":
    halaman_kalkulator()
elif halaman == "Contoh Kasus":
    halaman_contoh_kasus()
