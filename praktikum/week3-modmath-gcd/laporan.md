# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: Modular Match
Nama: Arif Bowo Laksono  
NIM: 230202800
Kelas:5IKKA  

---

## 1. Tujuan
Menyelesaikan operasi aritmetika modular.
Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika modular merupakan dasar penting dalam kriptografi yang digunakan untuk melakukan operasi matematika dengan hasil yang dibatasi oleh suatu bilangan modulus. Operasi seperti penjumlahan, pengurangan, perkalian, dan pemangkatan dilakukan dengan aturan modulus, misalnya (a × b) mod m. Konsep ini berperan besar dalam algoritma seperti RSA dan Diffie-Hellman karena menjaga hasil perhitungan dalam batas tertentu dan memanfaatkan sifat periodik bilangan. Dalam kriptografi juga digunakan bilangan prima, yaitu bilangan yang hanya memiliki dua faktor, satu dan dirinya sendiri. Bilangan prima sulit difaktorkan sehingga menjadi dasar pembentukan kunci publik dan privat. Selain itu, GCD (Greatest Common Divisor) digunakan untuk menentukan apakah dua bilangan bersifat relatif prima, yang penting dalam perhitungan invers modular pada sistem enkripsi.
Logaritma diskrit merupakan konsep matematika yang sulit diselesaikan dan menjadi dasar keamanan pada sistem kriptografi modern. Masalah ini melibatkan pencarian nilai eksponen pada persamaan g^x ≡ h (mod p), yang sangat sulit dihitung jika bilangan prima yang digunakan besar. Konsep ini diterapkan dalam algoritma pertukaran kunci Diffie–Hellman, di mana dua pihak dapat menghasilkan kunci rahasia bersama tanpa mengirimkan kunci secara langsung. Keseluruhan konsep seperti aritmetika modular, bilangan prima, GCD, dan logaritma diskrit saling melengkapi untuk menciptakan sistem kriptografi yang aman dan sulit ditembus.

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
( ======== Jalankan ========
if __name__ == "__main__":
    menu()
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
Hasil eksekusi program Caesar Cipher:

)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:Aritmetika modular digunakan untuk menjaga hasil perhitungan tetap dalam batas tertentu, membentuk dasar operasi enkripsi dan dekripsi seperti pada RSA dan Diffie-Hellman, serta memastikan keamanan melalui sifat periodik dan sulitnya pembalikan operasi.
- Pertanyaan 2:Invers modular digunakan untuk menghitung kunci privat dari kunci publik, memungkinkan pesan yang telah dienkripsi dapat didekripsi kembali. Tanpa invers modular, proses pembalikan enkripsi tidak bisa dilakukan.
- Pertanyaan 3:Masalah logaritma diskrit sangat sulit diselesaikan karena tidak ada algoritma efisien untuk menemukan eksponen ketika modulusnya sangat besar, sehingga hal ini menjadi dasar keamanan banyak sistem kriptografi modern.
)
---

## 8. Kesimpulan
Program ini dibuat untuk mengenalkan dasar-dasar kriptografi lewat Python secara sederhana. Dari hasil percobaan, semua fitur berjalan dengan baik — mulai dari operasi aritmetika modular, cek bilangan prima, hitung GCD, sampai simulasi logaritma diskrit dan pertukaran kunci Diffie-Hellman. Program ini membantu memahami bagaimana konsep seperti modulus, bilangan prima, dan logaritma diskrit dipakai dalam sistem keamanan modern seperti RSA dan Diffie-Hellman.

---

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson Education.
Menezes, A. J., Van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
Paar, C., & Pelzl, J. (2010). Understanding Cryptography: A Textbook for Students and Practitioners. Springer.
Schneier, B. (2015). Applied Cryptography: Protocols, Algorithms, and Source Code in C (20th Anniversary ed.). Wiley.

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit modularmatch
Author: Arif Bowo Laksono <bowoarif65@gmail.com>
Date:   2025-11-10

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
