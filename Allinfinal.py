import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Judul Aplikasi
st.title("Pt pencari cinta sejati")
# Membuat layer di kiri
st.sidebar.title("Layer Kiri")

# Menambahkan elemen ke layer kiri
st.sidebar.write("Ini adalah layer kiri")
st.sidebar.button("Klik saya")
st.sidebar.selectbox("Pilih opsi", ["Opsi 1", "Opsi 2", "Opsi 3"])

# Membuat konten utama
st.title("Konten Utama")
st.write("Ini adalah konten utama")
# Anggota Group 6
st.header("Anggota Group 5")
st.write("1. ciwambha")
st.write("2. hanida")
st.write("3. laven")
st.write("3. yana")
# Upload Gambar
st.header("Upload Gambar")
uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

# Fungsi Pengolahan Citra
def pengolahan_citra(image):
    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Konversi gambar ke binary
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Deteksi tepi
    edges = cv2.Canny(thresh, 100, 200)
    
    return edges

# Tampilkan Gambar Asli
if uploaded_file is not None:
    st.header("Gambar Asli")
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar Asli")

    # Tampilkan Gambar Hasil Pengolahan
    st.header("Gambar Hasil Pengolahan")
    image_array = np.array(image)
    image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    hasil_pengolahan = pengolahan_citra(image_array)
    st.image(hasil_pengolahan, caption="Gambar Hasil Pengolahan")

# Fungsi Pengolahan Citra dengan OpenCV
def pengolahan_citra_opencv(image):
    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Konversi gambar ke binary
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Deteksi tepi
    edges = cv2.Canny(thresh, 100, 200)
    
    # Tampilkan gambar hasil pengolahan
    st.image(edges, caption="Gambar Hasil Pengolahan dengan OpenCV")

# Tampilkan Gambar Hasil Pengolahan dengan OpenCV
if uploaded_file is not None:
    st.header("Gambar Hasil Pengolahan dengan OpenCV")
    image_array = np.array(image)
    image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    pengolahan_citra_opencv(image_array)

# Fungsi Pengolahan Citra dengan PIL
def pengolahan_citra_pil(image):
    # Konversi gambar ke grayscale
    gray = image.convert('L')
    
    # Tampilkan gambar hasil pengolahan
    st.image(gray, caption="Gambar Hasil Pengolahan dengan PIL")

# Tampilkan Gambar Hasil Pengolahan dengan PIL
if uploaded_file is not None:
    st.header("Gambar Hasil Pengolahan dengan PIL")
    pengolahan_citra_pil(image)

# Fungsi Pengolahan Citra dengan Numpy
def pengolahan_citra_numpy(image):
    # Konversi gambar ke grayscale
    gray = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    
    # Tampilkan gambar hasil pengolahan
    st.image(gray, caption="Gambar Hasil Pengolahan dengan Numpy")

# Tampilkan Gambar Hasil Pengolahan dengan Numpy
if uploaded_file is not None:
    st.header("Gambar Hasil Pengolahan dengan Numpy")
    pengolahan_citra_numpy(image_array)