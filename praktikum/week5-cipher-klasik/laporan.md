# Laporan Praktikum Kriptografi
Minggu ke-: V  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi) 
Nama: Arif Bowo Laksono  
NIM: 230202800
Kelas: 5IKKA  

---

## 1. Tujuan
Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Cipher klasik adalah metode kriptografi awal yang digunakan untuk menyamarkan pesan. Caesar Cipher bekerja dengan menggeser setiap huruf pada plaintext sejumlah tertentu dalam alfabet sehingga mudah digunakan tetapi sangat lemah keamanannya. Vigenère Cipher merupakan pengembangan dari Caesar dengan menggunakan kata kunci sehingga setiap huruf dienkripsi dengan pergeseran berbeda, membuatnya lebih aman karena mengurangi pola frekuensi huruf.

Transposition Cipher berbeda dari dua cipher sebelumnya karena tidak mengganti huruf, melainkan mengacak posisi karakter dalam pesan berdasarkan suatu kunci. Metode ini mempertahankan frekuensi huruf asli tetapi tetap rentan jika digunakan sendiri. Secara umum, cipher klasik memiliki tingkat keamanan rendah dan tidak digunakan dalam sistem modern, namun tetap penting sebagai dasar pemahaman konsep kriptografi.

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
# contoh potongan kode
def encrypt(text, key):
    return ...
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
- Pertanyaan 1: Caesar mudah dipecahkan karena kunci sedikit, sedangkan Vigenère lemah jika kunci pendek atau berulang.
- Pertanyaan 2: Karena pola kemunculan huruf pada ciphertext masih menyerupai bahasa asli.
- Pertanyaan 3: Substitusi mengubah huruf tapi rentan analisis frekuensi, sedangkan transposisi hanya mengacak posisi huruf namun pola masih bisa dianalisis. 
)
---

## 8. Kesimpulan
Berdasarkan percobaan yang dilakukan, proses enkripsi dan dekripsi cipher klasik dapat berjalan dengan baik meskipun sempat terjadi beberapa kesalahan, seperti kesalahan penentuan kunci dan pengurutan karakter. Kesalahan tersebut membantu memahami pentingnya ketelitian dalam penerapan algoritma. Secara keseluruhan, percobaan menunjukkan bahwa cipher klasik mudah diimplementasikan tetapi memiliki tingkat keamanan yang rendah.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit abc12345
Author: Arif Bowo Laksono ( bowoarif65@gmail.com)
Date:   2025-11-23

    week5-Cipher Klasik (Caesar, Vigenère, Transposisi)
```
