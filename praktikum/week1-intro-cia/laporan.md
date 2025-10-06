🏛️ 1. Zaman Kuno

Kriptografi berasal dari bahasa Yunani: kryptos (tersembunyi) dan graphein (menulis), artinya “tulisan tersembunyi”.

Mesir Kuno (±1900 SM): Penggunaan simbol-simbol hieroglif rahasia dalam prasasti untuk menyembunyikan pesan.

Sparta (abad ke-5 SM): Menggunakan alat bernama scytale — sebatang kayu tempat menggulung pita kulit dengan pesan yang hanya bisa dibaca dengan batang berukuran sama.

Julius Caesar (abad ke-1 SM): Menggunakan sandi Caesar Cipher — mengganti setiap huruf dengan huruf lain yang berjarak tetap (misalnya, A diganti D jika jaraknya 3).

⚔️ 2. Abad Pertengahan

Sandi substitusi dan transposisi mulai berkembang untuk komunikasi diplomatik dan militer.

Arab abad ke-9: Ilmuwan Al-Kindi menulis Risalah tentang Dekripsi Pesan Terenkripsi, yang memperkenalkan analisis frekuensi — metode pertama untuk memecahkan sandi berdasarkan pola huruf.

💡 3. Zaman Renaisans hingga Abad ke-19

Leon Battista Alberti (1400-an): Menciptakan cipher disk, alat enkripsi polialfabetik pertama.

Blaise de Vigenère (1500-an): Mengembangkan Vigenère Cipher, sandi polialfabetik yang jauh lebih sulit dipecahkan.

Abad ke-19: Kriptografi masih bersifat manual dan digunakan dalam komunikasi diplomatik dan militer.

⚙️ 4. Abad ke-20 (Era Mesin dan Perang Dunia)

Perang Dunia I & II: Kriptografi menjadi senjata strategis.

Jerman menggunakan Mesin Enigma, dan sekutu memecahkannya dengan bantuan Alan Turing di Bletchley Park.

Setelah perang, kriptografi berkembang menjadi ilmu matematis dengan fokus pada keamanan komunikasi elektronik.

💻 5. Era Komputer (1970–1990-an)

1970-an: IBM dan NSA mengembangkan DES (Data Encryption Standard) — standar enkripsi pertama yang digunakan secara luas.

1976: Whitfield Diffie & Martin Hellman memperkenalkan konsep kriptografi kunci publik, yang memungkinkan enkripsi tanpa berbagi kunci rahasia sebelumnya.

1977: Ditemukan RSA Algorithm, dasar dari banyak sistem keamanan modern.

🌐 6. Era Internet & Modern (2000-an – Sekarang)

Kriptografi menjadi dasar keamanan digital: HTTPS, email terenkripsi, tanda tangan digital, dan cryptocurrency.

AES (Advanced Encryption Standard) menggantikan DES pada tahun 2001.

Blockchain & Cryptocurrency (Bitcoin, 2009): Menggabungkan kriptografi dengan teori desentralisasi.

Saat ini, penelitian fokus pada kriptografi kuantum dan post-quantum cryptography untuk menghadapi ancaman komputer kuantum.



🔐 1. Confidentiality (Kerahasiaan)

Kerahasiaan berarti menjaga agar informasi hanya bisa diakses oleh orang yang berwenang. Tujuannya adalah mencegah kebocoran data kepada pihak yang tidak berhak. Dalam kriptografi, hal ini dicapai dengan enkripsi, yaitu mengubah data menjadi bentuk kode yang tidak bisa dibaca tanpa kunci tertentu.
🧩 Contoh: Pesan WhatsApp yang terenkripsi tidak bisa dibaca oleh siapa pun selain pengirim dan penerima.

✅ 2. Integrity (Integritas)

Integritas memastikan bahwa data tetap asli, tidak diubah, dihapus, atau disisipkan selama proses pengiriman maupun penyimpanan. Kriptografi menjaga integritas dengan hash function atau digital signature, sehingga setiap perubahan sekecil apa pun dapat terdeteksi.
🧩 Contoh: Saat mengunduh file, sistem memeriksa “checksum” untuk memastikan file tidak dimodifikasi oleh pihak lain.

⚙️ 3. Availability (Ketersediaan)

Ketersediaan berarti data dan sistem selalu bisa diakses oleh pengguna yang berhak kapan pun dibutuhkan. Kriptografi berperan menjaga keamanan sistem tanpa menghalangi akses sah. Untuk menjaga ketersediaan, digunakan langkah-langkah seperti backup data, server cadangan, dan perlindungan dari serangan DoS (Denial of Service).
🧩 Contoh: Layanan perbankan online harus tetap bisa diakses 24 jam walau ada upaya peretasan.

🧭 Kesimpulan

Confidentiality, Integrity, dan Availability (CIA Triad) adalah tiga pilar utama keamanan informasi dalam kriptografi.

Confidentiality melindungi dari kebocoran data,

Integrity menjaga keaslian data, dan

Availability memastikan data tetap dapat digunakan.

Ketiganya bekerja bersama agar sistem informasi aman, andal, dan terpercaya.

🧑‍🏫 1. Tokoh yang dianggap sebagai Bapak Kriptografi Modern

➡️ Whitfield Diffie dan Martin Hellman dianggap sebagai bapak kriptografi modern.
Mereka memperkenalkan konsep kriptografi kunci publik (Public Key Cryptography) pada tahun 1976, yang menjadi dasar semua sistem keamanan digital modern seperti SSL, email terenkripsi, dan tanda tangan digital.

🔑 2. Algoritma kunci publik yang populer digunakan saat ini

Beberapa algoritma yang paling banyak digunakan:

RSA (Rivest–Shamir–Adleman) → digunakan untuk enkripsi dan tanda tangan digital.

Diffie–Hellman → untuk pertukaran kunci rahasia secara aman.

Elliptic Curve Cryptography (ECC) → versi lebih efisien dari RSA, banyak digunakan pada perangkat mobile dan blockchain.

DSA (Digital Signature Algorithm) → khusus untuk verifikasi tanda tangan digital.

⚙️ 3. Perbedaan utama antara kriptografi klasik dan kriptografi modern
Aspek	Kriptografi Klasik	Kriptografi Modern
Teknik	Mengandalkan penggantian (substitusi) dan penyusunan ulang (transposisi) huruf.	Menggunakan matematika kompleks dan algoritma komputer.
Jenis kunci	Hanya kunci simetris (kunci pengirim = kunci penerima).	Ada kunci simetris dan kunci publik (asimetris).
Media	Digunakan untuk pesan teks (manusia).	Digunakan untuk data digital (komputer & jaringan).
Contoh	Caesar Cipher, Vigenère Cipher	RSA, AES, ECC, DES, AES
