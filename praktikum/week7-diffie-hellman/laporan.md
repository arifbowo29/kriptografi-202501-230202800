# Laporan Praktikum Kriptografi
Minggu ke-: VII  
Topik: Diffie-Hellman Key Exchange
Nama: ARIF BOWO LAKSONO
NIM: 230202800
Kelas: 5IKKA

---

## 1. Tujuan
Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Diffie–Hellman Key Exchange adalah metode kriptografi kunci publik yang digunakan untuk menyepakati kunci rahasia bersama melalui jaringan yang tidak aman. Metode ini bekerja dengan memanfaatkan kesulitan perhitungan logaritma diskret, sehingga kunci privat tidak dapat dengan mudah ditebak meskipun parameter publik diketahui. Dua pihak bertukar kunci publik hasil perpangkatan modulo bilangan prima, lalu masing-masing menghitung kunci rahasia yang sama tanpa pernah mengirimkannya secara langsung. Namun, Diffie–Hellman tidak menyediakan autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle dan perlu dikombinasikan dengan mekanisme keamanan tambahan seperti sertifikat digital.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key dan hitung kunci bersama
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Karena kunci rahasia dihitung dari kunci publik dan kunci privat menggunakan operasi matematika yang sulit dibalik (logaritma diskret), sehingga kunci privat tidak dapat ditebak meskipun komunikasi disadap.
- Pertanyaan 2:Tidak memiliki mekanisme autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle (MITM)
- Pertanyaan 3:Dengan menambahkan autentikasi seperti tanda tangan digital, sertifikat digital (PKI), atau menggunakan protokol aman seperti TLS.
)
---

## 8. Kesimpulan
Berdasarkan beberapa kali percobaan, pertukaran kunci Diffie–Hellman hanya berhasil menghasilkan kunci yang sama ketika tidak terjadi gangguan pada proses pertukaran kunci publik. Pada percobaan yang melibatkan serangan Man-in-the-Middle, kunci yang dihasilkan Alice dan Bob menjadi berbeda sehingga komunikasi gagal. Hal ini menunjukkan bahwa Diffie–Hellman murni rentan terhadap serangan MITM dan memerlukan mekanisme autentikasi agar pertukaran kunci dapat berjalan dengan aman.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
week7-diffie-hellman
Author: Arif Bowo Laksono (bowoarif65@gmail.com)
Date:   2025-12-29

    week7-cDiffie-Hellman Key Exchange
```
