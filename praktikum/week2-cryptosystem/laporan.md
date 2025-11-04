# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: CRYPTOSYSTEM  
Nama: ARIF BOWO LAKSONO  
NIM: 230202800
Kelas: 5IKKA  

---

## 1. Tujuan
Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).
---

## 2. Dasar Teori
Cipher klasik adalah metode enkripsi tradisional yang digunakan sebelum munculnya komputer modern.
Prinsip dasarnya adalah mengubah (menyandikan) huruf-huruf pesan asli (plaintext) menjadi
bentuk lain (ciphertext) menggunakan aturan tertentu agar tidak mudah dibaca oleh orang lain.
Modular aritmetika adalah sistem perhitungan yang menggunakan sisa hasil bagi dari pembagian
suatu bilangan terhadap bilangan tertentu yang disebut modulus (m).

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
)
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
def buat_kamus_substitusi():

    abjad = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    kunci = abjad.copy()
    random.shuffle(kunci)  # kunci diacak agar hasil enkripsi berbeda setiap kali dijalankan

    kamus_enkripsi = dict(zip(abjad, kunci))
    kamus_dekripsi = dict(zip(kunci, abjad))
    return kamus_enkripsi, kamus_dekripsi, "".join(kunci)
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
- Pertanyaan 1:  Plaintext	Pesan asli atau data yang belum dienkripsi.
    Ciphertext	Hasil dari proses enkripsi, berupa pesan yang sudah disandikan.
    Algoritma Enkripsi	Proses atau rumus matematis yang digunakan untuk mengubah plaintext menjadi ciphertext.
    Algoritma Dekripsi	Proses kebalikan dari enkripsi, untuk mengubah ciphertext kembali menjadi plaintext.
    Kunci (Key)	Nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi. Tanpa kunci yang benar, pesan tidak dapat dibaca.
- Pertanyaan 2: Simetris unggul dalam kecepatan dan efisiensi, tapi asimetris lebih unggul dalam keamanan dan manajemen kunci.
- pertanyaan 3: Distribusi kunci adalah masalah utama dalam kriptografi simetris karena:Pengirim dan penerima harus memiliki kunci yang sama,Kunci tersebut harus dikirimkan terlebih dahulu melalui saluran komunikasi,Jika kunci tersebut disadap oleh pihak ketiga, maka seluruh pesan terenkripsi bisa dibuka,Tidak ada cara aman bawaan dalam sistem simetris untuk mendistribusikan kunci tersebut.Karena itu, banyak sistem modern menggabungkan kriptografi simetris dan asimetris (misalnya pada SSL/TLS): kunci simetris dikirim dengan cara aman menggunakan algoritma asimetris. 
)
---

## 8. Kesimpulan
Kriptosistem terdiri dari komponen utama seperti plaintext, ciphertext, algoritma enkripsi-dekripsi, dan kunci yang menjadi inti proses keamanan data.
Dalam perbandingan antara sistem simetris dan asimetris, sistem simetris lebih cepat dan sederhana, namun memiliki kelemahan besar pada keamanan distribusi kunci.
Masalah utama pada kriptografi simetris adalah pengiriman kunci secara aman antara pengirim dan penerima — jika kunci bocor, maka seluruh pesan bisa terbaca oleh pihak tidak berwenang.
Oleh karena itu, kombinasi antara sistem simetris dan asimetris sering digunakan untuk menyeimbangkan antara kecepatan dan keamanan dalam komunikasi data modern.

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
Author: Arif bowo laksono <bowoarif65@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
