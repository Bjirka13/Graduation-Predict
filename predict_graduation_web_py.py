# -*- coding: utf-8 -*-
"""Predict_Graduation-Web.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MEj4uYY9zRAKmSXWqfPixn8u3qG2PPfq

# Instal Streamlit dan import Library yang dibutuhkan
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile Predict_Graduation-Web.py
# import streamlit as st

import pandas as pd
from joblib import load

"""## Load dataset dan Model"""

def load_data():
  df = pd.read_csv('Fitur.csv')
  return df

data = load_data()

reg = load('regression_Exam.pkl')
clasif = load('Clasification_Graduation.pkl')

st.sidebar.title("Menu")
selection = st.sidebar.radio("", ["Deskripsi", "Dataset", "Grafik", "Prediksi"])

def main():
  if selection == "Deskripsi":
    st.title("Prediksi Kelulusan Siswa")
    st.write("""
    Input Setiap Data yang diminta dan Web ini akan memprediksi Kelulusanmu
    """)

  elif selection == "Dataset":
    st.title("Dataset Siswa")
    st.write("""
    Page ini menampilkan dataset yang digunakan untuk prediksi. Fitur yang digunakan



    Fitur yang digunakan dalam prediksi:
    Hours_Studied – Jumlah jam yang dihabiskan untuk belajar per minggu.

      1.  Hours_Studied – Jumlah jam yang dihabiskan untuk belajar per minggu.
      2.  Attendance – Persentase kehadiran di kelas.
      3.  Parental_Involvement – Tingkat keterlibatan orang tua dalam pendidikan siswa (Rendah, Sedang, Tinggi).
      4.  Access_to_Resources – Ketersediaan sumber daya pendidikan (Rendah, Sedang, Tinggi).
      5.  Extracurricular_Activities – Partisipasi dalam kegiatan ekstrakurikuler (Ya, Tidak).
      6.  Sleep_Hours – Rata-rata jumlah jam tidur per malam.
      7.  Previous_Scores – Nilai dari ujian sebelumnya.
      8.  Motivation_Level – Tingkat motivasi siswa (Rendah, Sedang, Tinggi).
      9.  Internet_Access – Ketersediaan akses internet (Ya, Tidak).
      10. Tutoring_Sessions – Jumlah sesi les privat yang diikuti per bulan.
      11. Family_Income – Tingkat pendapatan keluarga (Rendah, Sedang, Tinggi).
      12. Teacher_Quality – Kualitas guru (Rendah, Sedang, Tinggi).
      13. School_Type – Jenis sekolah yang dihadiri (Negeri, Swasta).
      14. Peer_Influence – Pengaruh teman sebaya terhadap performa akademik (Positif, Netral, Negatif).
      15. Physical_Activity – Rata-rata jumlah jam aktivitas fisik per minggu.
      16. Learning_Disabilities – Adanya gangguan belajar (Ya, Tidak).
      17. Parental_Education_Level – Tingkat pendidikan tertinggi dari orang tua (SMA, Perguruan Tinggi, Pascasarjana).
      18. Distance_from_Home – Jarak dari rumah ke sekolah (Dekat, Sedang, Jauh).
      19. Gender – Jenis kelamin siswa (Laki-laki, Perempuan).
      20. Exam_Score – Nilai ujian akhir.
    """)
    selected_columns = st.multiselect("Pilih kolom yang ingin ditampilkan: ", data.columns, default=data.columns)
    st.dataframe(data[selected_columns])

  # Grafik
  elif selection == "Prediksi":
    st.title("Prediksi Kelulusan Siswa")
    st.write("""
    input data siswa seperti absensi, waktu belajar, dll untuk
    mendapatkan prediksi apakah siswa tersebut lulus atau tidak.
    """)

    # Input
    st.subheader("Input Data Siswa untuk Prediksi")
    Hours_Studied = st.slider("Waktu Belajar dalam seminggu (1-35)", 1, 35, 0)
    Attendance = st.slider("Absensi (%)", 0, 100, 0)
    Parental_Involvement = st.slider("Peran Orang Tua (0: Rendah, 1: Sedang, 2: Tinggi)", 0, 2, 0)
    Access_to_Resources = st.slider("sumber daya pendidikan (0: Rendah, 1: Sedang, 2: Tinggi)", 0, 2, 0)
    Extracurricular_Activities = st.slider("Ekskul (0: Tidak, 1: Ya)", 0, 1, 0)
    Sleep_Hours = st.slider("Waktu Tidur per Hari (Jam)", 0, 10, 0)
    Previous_Scores = st.slider("Nilai Ujian sebelumnya", 0, 100, 10)
    Motivation_Level = st.slider("Motivasi (0: Rendah, 1: Sedang, 2: Tinggi)", 0, 2, 0)
    Internet_Access = st.slider("Akses Internet (0: Tidak, 1: Ya)", 0, 1, 0)
    Tutoring_Sessions = st.slider("Jumlah Les Privat per Bulan (0-10)", 0, 10, 0)
    Family_Income = st.slider("Penghasilan Orang Tua (0: Rendah, 1: Sedang, 2: Tinggi)", 0, 2, 0)
    Teacher_Quality = st.slider("Kualitas Guru (0: Rendah, 1: Sedang, 2: Tinggi)", 0, 2, 0)
    School_Type = st.slider("Tipe Sekolah (0: Privat, 1: Publik)", 0, 1, 0)
    Peer_Influence = st.slider("Pengaruh Teman (0: Buruk, 1: Netral, 2: Baik)", 0, 2, 0)
    Physical_Activity = st.slider("Rata-Rata Jumlah Aktivitas fisik per minggu (0-6)", 0, 6, 0)
    Learning_Disabilities = st.slider("Adanya Gangguan Belajar (0: Tidak, 1: Ya)", 0, 1, 0)
    Parental_Education_Level = st.slider("Riwayat Pendidikan Orang Tua (0: SMA, 1: Perguruan Tinggi, 2: Pascasarjana)")
    Distance_from_Home = st.slider("Jarak dari Rumah ke Sekolah (0: Jauh, 1: Sedang, 2: Dekat)")
    Gender = st.slider("Jenis Kelamin (0: Perempuan, 1: Pria)", 0, 1, 0)

    input_data = pd.DataFrame({
          'Hours_Studied': [Hours_Studied],
          'Attendance': [Attendance],
          'Parental_Involvement': [Parental_Education_Level],
          'Access_to_Resources': [Access_to_Resources],
          'Extracurricular_Activities': [Extracurricular_Activities],
          'Sleep_Hours': [Sleep_Hours],
          'Previous_Scores': [Previous_Scores],
          'Motivation_Level': [Motivation_Level],
          'Internet_Access': [Internet_Access],
          'Tutoring_Sessions': [Tutoring_Sessions],
          'Family_Income': [Family_Income],
          'Teacher_Quality': [Teacher_Quality],
          'School_Type': [School_Type],
          'Peer_Influence': [Peer_Influence],
          'Physical_Activity': [Physical_Activity],
          'Learning_Disabilities': [Learning_Disabilities],
          'Parental_Education_Level': [Parental_Education_Level],
          'Distance_from_Home': [Distance_from_Home],
          'Gender': [Gender]
      })

    # Prediksi
    reg_predict = reg.predict(input_data)
    clasif_predict = clasif.predict(reg_predict)


    # 5. Bantuan
  elif selection == "Bantuan":
        st.title("Bantuan Penggunaan Aplikasi")
        st.write("1. Gunakan navigasi di sidebar untuk berpindah antar halaman.")
        st.write("2. Halaman Deskripsi memberikan informasi tentang tujuan dan cara kerja aplikasi.")
        st.write("3. Halaman Dataset menampilkan data siswa yang digunakan.")
        st.write("4. Halaman Grafik menyediakan visualisasi data penting.")
        st.write("5. Halaman Prediksi memungkinkan Anda memprediksi kelulusan siswa berdasarkan input data.")

if __name__ == "__main__":
    main()
