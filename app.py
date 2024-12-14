import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Fungsi untuk menerapkan efek blur
def apply_blur(image, blur_strength):
    return cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)

# Fungsi untuk halaman pertama
def page_home():
    st.title("Aplikasi Efek Blur pada Gambar")
    st.write("Selamat datang di aplikasi efek blur. Pilih halaman di sidebar untuk melanjutkan.")

# Fungsi untuk halaman efek blur
def page_blur():
    st.title("Efek Blur pada Gambar")
    
    # Upload gambar
    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Membaca gambar
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        # Menampilkan gambar asli
        st.image(image, caption='Gambar Asli', use_column_width=True)

        # Slider untuk mengatur kekuatan blur
        blur_strength = st.slider("Pilih kekuatan blur (harus bilangan ganjil)", 1, 25, 5, step=2)

        # Menerapkan efek blur
        blurred_image = apply_blur(image_np, blur_strength)

        # Menampilkan gambar yang telah diblur
        st.image(blurred_image, caption='Gambar dengan Efek Blur', use_column_width=True)

# Fungsi untuk halaman tentang
def page_about():
    st.title("Tentang Aplikasi")
    st.write("Aplikasi ini dibuat untuk mendemonstrasikan efek blur pada gambar menggunakan Python dan Streamlit.")

# Menentukan halaman yang dipilih
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Beranda", "Efek Blur", "Tentang"])

# Menampilkan halaman yang sesuai
if page == "Beranda":
    page_home()
elif page == "Efek Blur":
    page_blur()
elif page == "Tentang":
    page_about()   