import streamlit as st
import numpy as np
import pandas as pd

# Modulasi Amplitudo
def modulasi_amplitudo(amplitudo_informasi, frekuensi_informasi, amplitudo_pembawa, frekuensi_pembawa, t):
    sinyal_informasi = amplitudo_informasi * np.cos(2 * np.pi * frekuensi_informasi * t)
    sinyal_pembawa = amplitudo_pembawa * np.cos(2 * np.pi * frekuensi_pembawa * t)
    nilai_m = amplitudo_informasi / amplitudo_pembawa

    sinyal_AM = amplitudo_pembawa * (1 + nilai_m * np.cos(2 * np.pi * frekuensi_informasi * t) * np.cos(2 * np.pi * frekuensi_pembawa * t))
    
    return sinyal_informasi, sinyal_pembawa, sinyal_AM, nilai_m

# Modulasi Frekuensi
def modulasi_frekuensi(amplitudo_informasi, frekuensi_informasi, amplitudo_pembawa, frekuensi_pembawa, t):
    sinyal_informasi = amplitudo_informasi * np.cos(2 * np.pi * frekuensi_informasi * t)
    sinyal_pembawa = amplitudo_pembawa * np.cos(2 * np.pi * frekuensi_pembawa * t)
    
    nilai_m = frekuensi_pembawa / frekuensi_informasi
    
    sinyal_FM = amplitudo_pembawa * np.cos(2 * np.pi * frekuensi_pembawa * t + nilai_m * np.cos(2 * np.pi * frekuensi_informasi * t))
    
    return sinyal_informasi, sinyal_pembawa, sinyal_FM, nilai_m

# Streamlit App
def main():
    # Judul
    st.title("Modulasi Amplitudo dan Frekuensi")
    
    # Informasi Pembuat
    st.markdown("### Dibuat oleh:")
    st.markdown("ARILA RANGGA ALRASYID")
    st.markdown("11-2021-008")
    
    # Dosen Pembimbing
    st.markdown("### Dosen Pembimbing:")
    st.markdown("Ir. Rustamaji, M.T")
    
    # Input User
    amplitudo_informasi = st.number_input("Amplitudo Informasi (V):", min_value=0.1, value=1.0)
    frekuensi_informasi = st.number_input("Frekuensi Informasi (Hz):", min_value=1.0, max_value=100.0, value=10.0)
    amplitudo_pembawa = st.number_input("Amplitudo Pembawa (V):", min_value=0.1, value=5.0)
    frekuensi_pembawa = st.number_input("Frekuensi Pembawa (Hz):", min_value=1.0, max_value=1000.0, value=100.0)

    # Pilih Modulasi
    jenis_modulasi = st.radio("Pilih Modulasi:", ["Modulasi Amplitudo", "Modulasi Frekuensi"])

    if st.button("Proses"):
        # Waktu (t) dengan lebih banyak titik
        t = np.linspace(0, 1, 10000)

        if jenis_modulasi == "Modulasi Amplitudo":
            # Melakukan modulasi
            sinyal_informasi, sinyal_pembawa, sinyal_AM, nilai_m = modulasi_amplitudo(
                amplitudo_informasi, frekuensi_informasi, amplitudo_pembawa, frekuensi_pembawa, t)

            # Menampilkan nilai Indeks Modulasi
            st.write(f"Nilai Indeks Modulasi: {nilai_m}")

            # Membuat DataFrame untuk data deret waktu
            df = pd.DataFrame({'Waktu (s)': t, 'Sinyal Informasi': sinyal_informasi, 'Sinyal Pembawa': sinyal_pembawa, 'Modulasi Amplitudo': sinyal_AM})

            # Menampilkan DataFrame
            st.write(df)

            # Plot grafik menggunakan plotting natif Streamlit
            st.line_chart(df.set_index('Waktu (s)'))

        elif jenis_modulasi == "Modulasi Frekuensi":
            # Melakukan modulasi
            sinyal_informasi, sinyal_pembawa, sinyal_FM, nilai_m = modulasi_frekuensi(
                amplitudo_informasi, frekuensi_informasi, amplitudo_pembawa, frekuensi_pembawa, t)

            # Menampilkan nilai Indeks Modulasi
            st.write(f"Nilai Indeks Modulasi: {nilai_m}")

            # Membuat DataFrame untuk data deret waktu
            df = pd.DataFrame({'Waktu (s)': t, 'Sinyal Informasi': sinyal_informasi, 'Sinyal Pembawa': sinyal_pembawa, 'Modulasi Frekuensi': sinyal_FM})

            # Menampilkan DataFrame
            st.write(df)

            # Plot grafik menggunakan plotting natif Streamlit
            st.line_chart(df.set_index('Waktu (s)'))

    # Load dan tampilkan gambar
    image_path = "RumusFM_dan_AM.png"
    image = Image.open(image_path)
    st.image(image, caption="Modulation Formulas", use_column_width=True)

if __name__ == "__main__":
    main()
