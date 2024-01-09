import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

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
    # Center-aligned title
    st.markdown("<h1 style='text-align:center;'>Modulasi Amplitudo dan Frekuensi</h1>", unsafe_allow_html=True)

    # Center-aligned text
    st.markdown("<p style='text-align:center;'>Dibuat oleh:</p>", unsafe_allow_html=True)

    # Center-aligned header
    st.markdown("<p style='text-align:center;'>ARILA RANGGA ALRASYID</p>", unsafe_allow_html=True)

    # Center-aligned text
    st.markdown("<p style='text-align:center;'>11-2021-008</p>", unsafe_allow_html=True)

    st.markdown("<p style='text-align:center;'>Dosen Pembimbing:</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Ir. Rustamaji, M.T</p>", unsafe_allow_html=True)

    # Get user input
    amplitudo_informasi = st.number_input("Amplitudo Informasi (V):", min_value=0.1, value=1.0)
    frekuensi_informasi = st.number_input("Frekuensi Informasi (Hz):", min_value=1.0, max_value=100.0, value=10.0)
    amplitudo_pembawa = st.number_input("Amplitudo Pembawa (V):", min_value=0.1, value=5.0)
    frekuensi_pembawa = st.number_input("Frekuensi Pembawa (Hz):", min_value=1.0, max_value=1000.0, value=100.0)

    # Choose modulation type
    jenis_modulasi = st.radio("Pilih Modulasi:", ["Modulasi Amplitudo", "Modulasi Frekuensi"])


    if st.button("Proses"):
        # Waktu (t) with more points
        t = np.linspace(0, 1, 10000)

        if jenis_modulasi == "Modulasi Amplitudo":
            # Perform modulation
            sinyal_informasi, sinyal_pembawa, sinyal_AM, nilai_m = modulasi_amplitudo(
                amplitudo_informasi, frekuensi_informasi, amplitudo_pembawa, frekuensi_pembawa, t)

            # Create a DataFrame for the time series data
            df = pd.DataFrame({'Time': t, 'Informasi': sinyal_informasi, 'Pembawa': sinyal_pembawa, 'Modulasi': sinyal_AM})

            # Display the DataFrame
            st.write(df)

        elif jenis_modulasi == "Modulasi Frekuensi":
            # Perform modulation
            sinyal_informasi, sinyal_pembawa, sinyal_FM, nilai_m = modulasi_frekuensi(
                amplitudo_informasi, frekuensi_informasi, amplitudo_pembawa, frekuensi_pembawa, t)

            # Create a DataFrame for the time series data
            df = pd.DataFrame({'Time': t, 'Informasi': sinyal_informasi, 'Pembawa': sinyal_pembawa, 'Modulasi': sinyal_FM})

            # Display the DataFrame
            st.write(df)

    # Load and display the image
    image_path = "RumusFM_dan_AM.png"
    image = Image.open(image_path)
    st.image(image, caption="Modulation Formulas", use_column_width=True)

if __name__ == "__main__":
    main()
