# Graduation-Predict


Proyek ini bertujuan untuk memprediksi kelulusan siswa berdasarkan fitur-fitur seperti waktu belajar, kehadiran, nilai sebelumnya, jam tidur, dan sesi tutoring. Model ini menggunakan pendekatan klasifikasi dengan beberapa algoritma seperti Logistic Regression, Decision Tree, dan SVM.

## Deskripsi Singkat

- **Nama Proyek**: Graduation Predict  
- **Tujuan**: Memprediksi kelulusan siswa berdasarkan skor ujian (`Exam_Score`) menggunakan machine learning.  
- **Metode**: Klasifikasi biner (lulus vs tidak lulus)  
- **Threshold**: Siswa diklasifikasikan "Lulus" jika `Exam_Score > 70`

## Struktur Direktori

```

Graduation-Predict/
├── Data/                          # Dataset yang digunakan
├── Notebook/                      # Notebook eksplorasi dan pelatihan model
├── predict\_graduation\_web\_py.py  # Script aplikasi prediksi berbasis Streamlit
├── Clasification\_Graduation.pkl  # Model klasifikasi yang sudah dilatih
├── regression\_Exam.pkl           # Model regresi untuk prediksi nilai ujian
├── feature\_Exam-Score.pkl        # Pipeline fitur untuk nilai ujian
├── requirements.txt              # Daftar dependensi
└── README.md                     # Dokumentasi proyek

````

## Model yang Digunakan

- **Logistic Regression**
- **Decision Tree Classifier**
- **Support Vector Classifier (SVC)**
- **RandomForestClassifier**
- **XGBClassifier**

### Metrik Evaluasi:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Model terbaik berdasarkan hasil evaluasi: **XGBClassifier"" dengan akurasi 95.36%. Selain itu, nilai metriks evaluasi model tersebut
lebih stabil dibandingkan model yang lain:
Report: 

               precision    recall  f1-score   support

           0       0.91      0.91      0.91       320
           1       0.97      0.97      0.97       930

    accuracy                           0.95      1250
   macro avg       0.94      0.94      0.94      1250
weighted avg       0.95      0.95      0.95      1250

## Penanganan Data

- **Outliers**: Dihapus berdasarkan boxplot  
- **Missing Values**: Sangat sedikit, langsung dihapus  
- **SMOTE**: Digunakan untuk menyeimbangkan distribusi target  
- **Encoding**: Label Encoding untuk fitur kategorikal  

## Web App

Aplikasi berbasis **Streamlit** memungkinkan pengguna memasukkan fitur-fitur sebagai input:

- Hours Studied
- Attendance
- Sleep Hours
- Previous Scores
- Tutoring Sessions
- Physical Activity
- Peer Influence

Kemudian menghasilkan prediksi apakah siswa akan **Lulus** atau **Tidak Lulus**.

## Catatan

Saya telah menambahkan metode SMOTE untuk menangani imbalance data, namun hasilnya tidak memberikan perubahan yang signifikan terhadap imbalance data.
SMOTE hanya memberikan peningkatan yang signifikan pada nilai metrik evaluasi
