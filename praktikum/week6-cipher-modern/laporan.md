# Laporan Praktikum Kriptografi
Minggu ke-: 6
Topik:Cipher Modern (DES, AES, RSA) 
Nama: Arif Bowo Laksono  
NIM: 230202800
Kelas: 5IKKA

---

## 1. Tujuan
Mengimplementasikan algoritma DES untuk blok data sederhana.
Menerapkan algoritma AES dengan panjang kunci 128 bit.
Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.


---

## 2. Dasar Teori
Cipher modern merupakan algoritma kriptografi yang digunakan untuk mengamankan data pada sistem digital, di antaranya DES, AES, dan RSA. DES (Data Encryption Standard) adalah cipher kunci simetris yang menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi dengan panjang kunci 56 bit, namun saat ini dianggap tidak aman karena rentan terhadap serangan brute force. AES (Advanced Encryption Standard) juga merupakan cipher kunci simetris, tetapi memiliki tingkat keamanan yang jauh lebih tinggi dengan panjang kunci 128, 192, atau 256 bit, sehingga banyak digunakan dalam sistem keamanan modern. Berbeda dengan DES dan AES, RSA (Rivest–Shamir–Adleman) merupakan cipher kunci asimetris yang menggunakan sepasang kunci publik dan privat, dengan tingkat keamanan yang bergantung pada kesulitan memfaktorkan bilangan prima besar, dan umumnya digunakan untuk pertukaran kunci serta tanda tangan digital.

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

```plaintext = b"Arifbowo 230202800"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext) ...
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
- Pertanyaan 1: DES dan AES adalah algoritma simetris yang menggunakan satu kunci yang sama, tetapi DES kurang aman karena kuncinya pendek, sedangkan AES lebih aman dengan kunci yang lebih panjang. RSA adalah algoritma asimetris yang menggunakan sepasang kunci (publik dan privat) dan memiliki tingkat keamanan tinggi untuk pertukaran kunci.
- Pertanyaan 2:AES lebih aman karena memiliki panjang kunci yang lebih besar dan tahan terhadap serangan kriptografi modern, sementara DES mudah ditembus dengan brute force.
- Pertanyaan 3:RSA disebut asimetris karena menggunakan dua kunci berbeda, yaitu kunci publik dan kunci privat. Kunci tersebut dibangkitkan dari dua bilangan prima besar yang sulit difaktorkan, sehingga menjamin keamanannya.
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
week6-cipher-modern
Author: Arif Bowo Laksono (bowoarif65@gmail.com
Date:   2025-12-30

    week6-Cipher Modern (DES, AES, RSA) 
```
