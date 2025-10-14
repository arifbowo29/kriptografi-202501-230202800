# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: Cryptosistem  
Nama: Arif Bowo Laksono  
NIM: 230202800  
Kelas: 5 IKKA  

---

## 1. Tujuan
Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori
Cipher klasik adalah metode enkripsi tradisional yang digunakan sebelum munculnya komputer modern.
Prinsip dasarnya adalah mengubah (menyandikan) huruf-huruf pesan asli (plaintext) menjadi bentuk lain (ciphertext) menggunakan aturan tertentu agar tidak mudah dibaca oleh orang lain.

Contohnya:

Caesar Cipher → setiap huruf digeser beberapa langkah dalam alfabet.
Vigenère Cipher → menggunakan kata kunci untuk menentukan pergeseran tiap huruf.
Substitution Cipher → mengganti tiap huruf dengan huruf lain sesuai tabel substitusi.
Tujuan utamanya: menjaga kerahasiaan pesan dengan cara sederhana namun efektif pada zamannya.
Modular aritmetika adalah sistem perhitungan yang menggunakan sisa hasil bagi dari pembagian
suatu bilangan terhadap bilangan tertentu yang disebut modulus (m).

---

## 3. Alat dan Bahan
- Python 3.x  
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
def enkripsi(teks, kamus_enkripsi):
    hasil = ""
    for huruf in teks.upper():
        if huruf in kamus_enkripsi:
            hasil += kamus_enkripsi[huruf]
        elif huruf == " ":
            continue  # hapus spasi agar hasil lebih "rapat" dan aman
        else:
            hasil += huruf
    return hasil

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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
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
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
