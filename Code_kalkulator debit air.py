import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Debit Air",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS untuk styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #0050B3 !important;
        margin-bottom: 0.5rem !important;
    }
    .sub-header {
        font-size: 1.5rem !important;
        color: #0050B3 !important;
        margin-bottom: 1.5rem !important;
    }
    .info-box {
        background-color: #F0F7FF;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 4rem;
        white-space: pre-wrap;
        font-size: 1rem;
        font-weight: 500;
        color: #0050B3;
        border-radius: 0.5rem 0.5rem 0 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #F0F7FF;
        border-bottom: 4px solid #0050B3;
    }
    .formula {
        font-size: 1.2rem;
        text-align: center;
        margin: 1rem 0;
        font-weight: 500;
    }
    .highlight {
        font-weight: 600;
        color: #0050B3;
    }
    footer {
        margin-top: 3rem;
        text-align: center;
        color: #888;
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk halaman penjelasan
def tampilkan_penjelasan():
    st.markdown('<h2 class="sub-header">Penjelasan Debit Air</h2>', unsafe_allow_html=True)
    st.write("""
    Debit air adalah volume air yang mengalir melalui suatu penampang dalam satuan waktu tertentu. 
    Debit biasanya diukur dalam satuan meter kubik per detik (m³/s) atau liter per detik (L/s).
    """)
    
    with st.container():
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Rumus Dasar Debit Air:")
        st.markdown('<p class="formula">Q = V / t</p>', unsafe_allow_html=True)
        st.write("Dimana:")
        st.write("- Q = Debit air (m³/s atau L/s)")
        st.write("- V = Volume air (m³ atau L)")
        st.write("- t = Waktu (detik)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Rumus Alternatif:")
        st.markdown('<p class="formula">Q = A × v</p>', unsafe_allow_html=True)
        st.write("Dimana:")
        st.write("- Q = Debit air (m³/s)")
        st.write("- A = Luas penampang saluran (m²)")
        st.write("- v = Kecepatan aliran air (m/s)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Visualisasi ilustrasi konsep debit air
    st.subheader("Ilustrasi Debit Air")
    col1, col2 = st.columns(2)
    
    with col1:
        # Membuat data untuk visualisasi penampang
        x = np.linspace(0, 10, 100)
        y1 = 2 + np.sin(x/2) * 0.5
        y2 = 0
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.fill_between(x, y1, y2, alpha=0.6, color='skyblue')
        ax.plot(x, y1, 'b-')
        ax.plot(x, [y2] * len(x), 'b-')
        ax.set_xlim(0, 10)
        ax.set_ylim(-0.5, 3)
        ax.set_title('Penampang Saluran Air')
        ax.set_xlabel('Lebar (m)')
        ax.set_ylabel('Kedalaman (m)')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Menambahkan tanda panah untuk menunjukkan arah aliran
        ax.arrow(5, 1, 2, 0, head_width=0.2, head_length=0.3, fc='blue', ec='blue')
        ax.text(5, 1.3, 'Arah Aliran', fontsize=10, color='blue')
        
        # Menambahkan formula
        ax.text(5, -0.3, 'Debit (Q) = Luas (A) × Kecepatan (v)', 
                horizontalalignment='center', fontsize=10)
        
        st.pyplot(fig)
    
    with col2:
        # Create demonstration data for flow rate chart
        times = [0, 10, 20, 30, 40, 50, 60]
        volumes = [0, 50, 100, 150, 200, 250, 300]
        
        # Create a DataFrame for Altair
        data = pd.DataFrame({
            'Waktu (detik)': times,
            'Volume (Liter)': volumes
        })
        
        # Create an Altair chart
        chart = alt.Chart(data).mark_line(point=True).encode(
            x=alt.X('Waktu (detik)', title='Waktu (detik)'),
            y=alt.Y('Volume (Liter)', title='Volume (Liter)')
        ).properties(
            title='Hubungan Volume dan Waktu',
            width=400,
            height=300
        ).interactive()
        
        # Calculate flow rate
        flow_rate = (volumes[-1] - volumes[0]) / (times[-1] - times[0])
        
        st.altair_chart(chart, use_container_width=True)
        st.write(f"Dari grafik: Debit Air = {flow_rate} L/s")

# Fungsi untuk halaman pembahasan
def tampilkan_pembahasan():
    st.markdown('<h2 class="sub-header">Pembahasan Debit Air</h2>', unsafe_allow_html=True)
    
    st.subheader("Aplikasi Pengukuran Debit Air")
    st.write("""
    Pengukuran debit air memiliki banyak aplikasi penting dalam kehidupan sehari-hari dan industri.
    Beberapa aplikasi utama pengukuran debit air meliputi:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<p class="highlight">Sistem Irigasi</p>', unsafe_allow_html=True)
        st.write("Memastikan distribusi air yang tepat untuk area pertanian dan menentukan kebutuhan air tanaman.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<p class="highlight">Pengolahan Air Limbah</p>', unsafe_allow_html=True)
        st.write("Menentukan kapasitas pengolahan yang diperlukan untuk sistem pengolahan air limbah.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<p class="highlight">Sistem Penyediaan Air Bersih</p>', unsafe_allow_html=True)
        st.write("Mengatur distribusi air ke rumah-rumah dan bangunan untuk memenuhi kebutuhan konsumsi.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<p class="highlight">Manajemen Banjir</p>', unsafe_allow_html=True)
        st.write("Memprediksi dan mengelola aliran air selama musim hujan untuk mencegah banjir.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("Metode Pengukuran Debit Air")
    
    metode_data = {
        "Metode": ["Metode Volumetrik", "Metode Area-Kecepatan", "Penggunaan Alat Ukur"],
        "Deskripsi": [
            "Mengukur waktu yang diperlukan untuk mengisi wadah dengan volume tertentu.", 
            "Mengukur kecepatan aliran air dan luas penampang saluran.",
            "Flow meter, weir, flume, atau current meter."
        ],
        "Keunggulan": [
            "Sederhana, akurat untuk aliran kecil", 
            "Dapat digunakan untuk saluran besar",
            "Pengukuran kontinyu dan otomatis"
        ],
        "Keterbatasan": [
            "Tidak praktis untuk aliran besar", 
            "Memerlukan pengukuran yang tepat",
            "Biaya tinggi, memerlukan kalibrasi"
        ]
    }
    
    df_metode = pd.DataFrame(metode_data)
    st.dataframe(df_metode, use_container_width=True, hide_index=True)
    
    st.subheader("Faktor yang Mempengaruhi Debit Air")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<p class="highlight">Faktor Geografis</p>', unsafe_allow_html=True)
        st.write("""
        - Topografi dan kemiringan lahan
        - Karakteristik daerah aliran sungai
        - Jenis dan kondisi tanah
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<p class="highlight">Faktor Meteorologis</p>', unsafe_allow_html=True)
        st.write("""
        - Intensitas curah hujan
        - Distribusi hujan
        - Evaporasi dan transpirasi
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Fungsi untuk halaman kalkulator
def tampilkan_kalkulator():
    st.markdown('<h2 class="sub-header">Kalkulator Debit Air</h2>', unsafe_allow_html=True)
    
    # Pilihan metode perhitungan
    metode = st.radio(
        "Pilih Metode Perhitungan:",
        ["Volume/Waktu", "Luas Penampang × Kecepatan"],
        horizontal=True
    )
    
    # Pilihan satuan
    satuan_debit = st.selectbox(
        "Pilih Satuan Debit:",
        ["m³/s (meter kubik per detik)", "L/s (liter per detik)"]
    )
    
    # Form untuk input data
    with st.form("form_debit"):
        if metode == "Volume/Waktu":
            if "m³/s" in satuan_debit:
                volume = st.number_input("Volume Air (m³):", min_value=0.0, step=0.1)
                satuan_volume = "m³"
            else:
                volume = st.number_input("Volume Air (L):", min_value=0.0, step=0.1)
                satuan_volume = "L"
            
            waktu = st.number_input("Waktu (detik):", min_value=0.1, step=0.1)
            
        else:  # Luas Penampang × Kecepatan
            luas_penampang = st.number_input("Luas Penampang (m²):", min_value=0.0, step=0.01)
            kecepatan = st.number_input("Kecepatan Aliran (m/s):", min_value=0.0, step=0.01)
        
        submit_button = st.form_submit_button("Hitung Debit Air")
    
    # Hasil perhitungan
    if submit_button:
        if metode == "Volume/Waktu" and waktu > 0:
            debit = volume / waktu
            
            # Konversi satuan jika diperlukan
            if "m³/s" in satuan_debit and satuan_volume == "L":
                debit = debit / 1000  # Konversi L/s ke m³/s
            elif "L/s" in satuan_debit and satuan_volume == "m³":
                debit = debit * 1000  # Konversi m³/s ke L/s
                
            st.success(f"Debit Air = {debit:.4f} {'m³/s' if 'm³/s' in satuan_debit else 'L/s'}")
            
            # Visualisasi hasil
            progress_bar(debit, "m³/s" if "m³/s" in satuan_debit else "L/s")
            
        elif metode == "Luas Penampang × Kecepatan":
            debit = luas_penampang * kecepatan  # Hasil dalam m³/s
            
            # Konversi satuan jika diperlukan
            if "L/s" in satuan_debit:
                debit = debit * 1000  # Konversi m³/s ke L/s
                
            st.success(f"Debit Air = {debit:.4f} {'m³/s' if 'm³/s' in satuan_debit else 'L/s'}")
            
            # Visualisasi hasil
            progress_bar(debit, "m³/s" if "m³/s" in satuan_debit else "L/s")
    
    # Informasi tambahan
    with st.expander("Panduan Penggunaan Kalkulator"):
        st.write("""
        ### Cara Menggunakan Kalkulator Debit Air:
        
        1. **Metode Volume/Waktu**:
           - Masukkan volume air dalam satuan yang sesuai (m³ atau L)
           - Masukkan waktu yang diperlukan untuk volume tersebut (dalam detik)
           - Debit = Volume ÷ Waktu
        
        2. **Metode Luas Penampang × Kecepatan**:
           - Masukkan luas penampang saluran air (dalam m²)
           - Masukkan kecepatan aliran air (dalam m/s)
           - Debit = Luas Penampang × Kecepatan
        
        Satuan hasil dapat dipilih antara m³/s atau L/s, dengan konversi 1 m³ = 1000 L.
        """)

# Fungsi untuk menampilkan progress bar visualisasi
def progress_bar(value, unit):
    # Menentukan nilai maksimum untuk menyesuaikan skala
    max_value = 10 if unit == "m³/s" else 10000 if unit == "L/s" else 10
    
    # Menyesuaikan nilai untuk visualisasi
    norm_value = min(value, max_value) / max_value
    
    st.write("Visualisasi Debit:")
    
    # Progress bar
    st.progress(norm_value)
    
    # Interpretasi nilai debit
    if unit == "m³/s":
        if value < 0.1:
            st.info("💧 Debit sangat kecil, setara dengan aliran air dalam pipa rumah tangga.")
        elif value < 1:
            st.info("💧💧 Debit kecil, setara dengan aliran air dalam saluran kecil.")
        elif value < 5:
            st.info("💧💧💧 Debit sedang, setara dengan aliran air dalam saluran irigasi.")
        else:
            st.info("💧💧💧💧 Debit besar, setara dengan aliran air dalam sungai.")
    else:  # L/s
        if value < 10:
            st.info("💧 Debit sangat kecil, setara dengan aliran air dalam keran rumah tangga.")
        elif value < 100:
            st.info("💧💧 Debit kecil, setara dengan aliran air dalam pipa distribusi kecil.")
        elif value < 1000:
            st.info("💧💧💧 Debit sedang, setara dengan aliran air dalam saluran irigasi.")
        else:
            st.info("💧💧💧💧 Debit besar, setara dengan aliran air dalam sungai.")

# Fungsi untuk menampilkan contoh kasus
def tampilkan_contoh_kasus():
    st.markdown('<h2 class="sub-header">Contoh Kasus Debit Air</h2>', unsafe_allow_html=True)
    
    st.write("""
    Berikut adalah beberapa contoh kasus penghitungan debit air dalam berbagai konteks:
    """)
    
    tab1, tab2, tab3 = st.tabs(["Contoh 1: Irigasi", "Contoh 2: Saluran Air", "Contoh 3: Banjir"])
    
    with tab1:
        st.subheader("Contoh Kasus Irigasi")
        st.write("""
        **Kasus**: Sebuah saluran irigasi dengan lebar 2 meter dan kedalaman air 0,5 meter. 
        Kecepatan aliran air diukur sebesar 0,8 m/s.
        Berapakah debit air dalam saluran tersebut?
        """)
        
        st.write("**Penyelesaian**:")
        st.write("1. Menentukan luas penampang saluran:")
        st.write("   A = lebar × kedalaman = 2 m × 0,5 m = 1 m²")
        st.write("2. Menghitung debit air:")
        st.write("   Q = A × v = 1 m² × 0,8 m/s = 0,8 m³/s")
        st.write("3. Konversi ke satuan lain (opsional):")
        st.write("   Q = 0,8 m³/s = 800 L/s")
        
        st.write("**Kesimpulan**: Debit air dalam saluran irigasi tersebut adalah 0,8 m³/s atau 800 L/s.")
    
    with tab2:
        st.subheader("Contoh Kasus Saluran Air")
        st.write("""
        **Kasus**: Sebuah tangki penampungan air bervolume 5.000 liter kosong. 
        Air dialirkan ke dalam tangki dan terisi penuh dalam waktu 10 menit.
        Berapakah debit air yang masuk ke dalam tangki?
        """)
        
        st.write("**Penyelesaian**:")
        st.write("1. Mengkonversi volume ke satuan yang konsisten:")
        st.write("   V = 5.000 L = 5 m³")
        st.write("2. Mengkonversi waktu ke satuan detik:")
        st.write("   t = 10 menit = 600 detik")
        st.write("3. Menghitung debit air:")
        st.write("   Q = V / t = 5 m³ / 600 s = 0,00833 m³/s = 8,33 L/s")
        
        st.write("**Kesimpulan**: Debit air yang masuk ke dalam tangki adalah 0,00833 m³/s atau 8,33 L/s.")
    
    with tab3:
        st.subheader("Contoh Kasus Penanganan Banjir")
        st.write("""
        **Kasus**: Sebuah saluran drainase harus mampu mengalirkan air hujan dengan intensitas 
        100 mm/jam dari area seluas 5 hektar.
        Berapakah kapasitas debit minimum yang harus dimiliki saluran tersebut?
        """)
        
        st.write("**Penyelesaian**:")
        st.write("1. Menghitung volume air yang jatuh per jam:")
        st.write("   V = intensitas × luas area = 100 mm/jam × 5 hektar")
        st.write("   V = 0,1 m/jam × 50.000 m² = 5.000 m³/jam")
        st.write("2. Mengkonversi ke satuan debit per detik:")
        st.write("   Q = 5.000 m³/jam ÷ 3.600 detik = 1,39 m³/s")
        
        st.write("**Kesimpulan**: Kapasitas debit minimum saluran drainase adalah 1,39 m³/s.")

# Main function
def main():
    # Header
    st.markdown('<h1 class="main-header">Aplikasi Debit Air</h1>', unsafe_allow_html=True)
    st.markdown('<p>Aplikasi untuk mempelajari dan menghitung debit aliran air</p>', unsafe_allow_html=True)
    
    # Menu navigasi
    tab1, tab2, tab3, tab4 = st.tabs(["Penjelasan", "Pembahasan", "Kalkulator", "Contoh Kasus"])
    
    with tab1:
        tampilkan_penjelasan()
    
    with tab2:
        tampilkan_pembahasan()
    
    with tab3:
        tampilkan_kalkulator()
    
    with tab4:
        tampilkan_contoh_kasus()
    
    # Footer
    st.markdown('<footer>© 2025 Aplikasi Debit Air - Alat Bantu Pembelajaran</footer>', unsafe_allow_html=True)

if __name__ == '_main_':
    main()
