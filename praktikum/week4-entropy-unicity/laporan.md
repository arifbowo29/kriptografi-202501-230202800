# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
Nama: ARIF BOWO LAKSONO  
NIM: 230202800
Kelas: 5IKKA  

---

## 1. Tujuan
Menyelesaikan perhitungan sederhana terkait entropi kunci.
Menggunakan teorema Euler pada contoh perhitungan modular & invers.
Menghitung unicity distance untuk ciphertext tertentu.
Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropy adalah ukuran seberapa acak dan sulit ditebaknya sebuah kunci dalam kriptografi. Semakin tinggi entropi, semakin besar jumlah kemungkinan kunci yang harus dicoba penyerang, sehingga brute force jadi jauh lebih sulit. Entropi diukur dalam bit, dan kunci dengan entropi tinggi—seperti kunci 128 bit atau 256 bit—punya ruang kemungkinan yang sangat besar sehingga tidak realistis untuk dipecahkan dengan percobaan acak.

Unicity distance adalah ukuran berapa banyak ciphertext yang dibutuhkan penyerang untuk bisa menentukan kunci secara pasti dengan memanfaatkan pola atau redundansi pada data. Jika nilai unicity distance besar, artinya walaupun banyak ciphertext bocor, penyerang tetap kesulitan menemukan kunci. Dalam evaluasi kekuatan kunci, entropi yang besar dan unicity distance yang tinggi membuat serangan brute force semakin tidak efektif, sehingga sistem kriptografi menjadi jauh lebih aman.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

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
def unicity_distance_bits(key_entropy_bits: float, redundancy_bits_per_char: float) -> float:
    if redundancy_bits_per_char <= 0:
        raise ValueError("redundancy_bits_per_char harus > 0")
    return key_entropy_bits / redundancy_bits_per_char
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
- Pertanyaan 1: …  Entropy menunjukkan tingkat keacakan kunci; semakin besar nilainya, semakin sulit kunci ditebak karena ruang kemungkinan makin luas.
- Pertanyaan 2: …  Unicity distance menentukan seberapa banyak ciphertext yang dibutuhkan untuk memastikan kunci bisa dipecahkan, sehingga makin besar nilainya, makin aman cipher dari analisis kunci.
- Pertanyaan 3: …  Meskipun algoritma kuat, brute force tetap berbahaya karena peningkatan kemampuan hardware, teknik optimasi, dan serangan otomatis yang bisa mencoba kunci dalam jumlah besar dengan cepat.
)
---

## 8. Kesimpulan
Percobaan menunjukkan bahwa Caesar Cipher sangat lemah karena hanya memiliki 26 kemungkinan kunci dengan entropi sekitar 4,7 bit. Unicity distance yang kecil membuat kunci mudah ditemukan hanya dari sedikit ciphertext. Brute force juga hampir instan karena jumlah percobaannya sangat sedikit. Secara keseluruhan, Caesar Cipher tidak aman dan hanya cocok untuk pembelajaran dasar.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
Shannon, C. E. (1949). Communication Theory of Secrecy Systems. Bell System Technical Journal, 28(4), 656–715.
(Referensi utama konsep entropy, redundancy, dan unicity distance.)

Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson.
(Pembahasan lengkap tentang evaluasi kekuatan kunci, brute force, serta cipher klasik seperti Caesar.)

Singhal, R. & Raina, R. (2014). Caesar Cipher and Basic Cryptanalysis. International Journal of Computer Science and Information Technologies.
(Menjelaskan kelemahan Caesar Cipher dan metode brute force.)

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit Arifbowo
Author: Arif bowo laksono <bowoarif65@gmail.com>
Date:   2025-12-3

Week-4 Entropy & Unicity Distance: (Evaluasi Kekuatan Kunci dan Brute Force)
```
