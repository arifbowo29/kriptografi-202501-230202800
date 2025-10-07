# 1. Era Kriptografi Klasik
Periode: Zaman kuno hingga awal abad ke-20
Ciri utama: Mengandalkan manipulasi huruf (substitusi dan transposisi) tanpa bantuan komputer.

Contoh penting:

Caesar Cipher (Kode Caesar)
Diperkenalkan oleh Julius Caesar. Huruf dalam pesan digeser beberapa posisi dalam alfabet.
Contoh: Geser 3 huruf → A → D, B → E.
Pesan “CHATGPT” menjadi “FKDWJSW”.
Kelemahan: Mudah dipecahkan dengan analisis frekuensi huruf.

Vigenère Cipher
Menggunakan kunci kata untuk menentukan banyaknya pergeseran huruf, membuat pola lebih kompleks.
Contoh: Pesan “HELLO” dengan kunci “KEY” → terenkripsi lebih acak.
Kelebihan: Lebih aman dibanding Caesar Cipher.
Kelemahan: Masih bisa dipecahkan dengan metode Kasiski atau Index of Coincidence.

# 2. Perkembangan Kriptografi Modern

Periode: Pertengahan abad ke-20 hingga 2000-an
Ciri utama: Menggunakan algoritma matematis kompleks dan komputer untuk enkripsi.

Contoh penting:

RSA (Rivest–Shamir–Adleman, 1977)
Menggunakan konsep kunci publik dan kunci privat berdasarkan faktor bilangan prima besar.
Digunakan dalam keamanan internet (SSL/TLS, email, tanda tangan digital).

AES (Advanced Encryption Standard, 2001)
Pengganti algoritma DES. Menggunakan sistem blok 128-bit dengan kunci 128, 192, atau 256 bit.
Digunakan secara luas dalam keamanan data, perangkat mobile, dan jaringan nirkabel.

# 3. Evolusi Menuju Kriptografi Kontemporer
Periode: 2010-an hingga sekarang
Ciri utama: Fokus pada keamanan digital terdistribusi, privasi, dan komputasi pasca-kuantum.

Contoh penting:

Blockchain & Cryptocurrency
Menggunakan kriptografi hash (misalnya SHA-256 pada Bitcoin) untuk mencatat transaksi yang tidak bisa diubah.
Tanda tangan digital memastikan keaslian dan kepemilikan.
Digunakan pada sistem keuangan terdesentralisasi (cryptocurrency), kontrak pintar, dan identitas digital.
Kriptografi Pasca-Kuantum (Post-Quantum Cryptography)
Dikembangkan untuk melawan ancaman komputer kuantum yang bisa memecahkan algoritma klasik (seperti RSA).
Contoh: Lattice-based cryptography.

# Kesimpulan
Era	Ciri Utama	Contoh	Tujuan Utama
Klasik	Pergeseran huruf / simbol	Caesar, Vigenère	Menyembunyikan pesan
Modern	Algoritma matematis & komputer	AES, RSA	Keamanan komunikasi digital
Kontemporer	Sistem terdistribusi & anti-kuantum	Blockchain, Cryptocurrency	Privasi, desentralisasi, dan keamanan masa depan


# Prinsip CIA dalam Keamanan Informasi

Tiga pilar utama keamanan informasi dikenal dengan istilah CIA Triad, yaitu Confidentiality, Integrity, dan Availability.
Tujuan utamanya adalah melindungi data agar aman, utuh, dan dapat diakses saat dibutuhkan.

# 1. Confidentiality (Kerahasiaan)

Pengertian:
Menjamin bahwa informasi hanya dapat diakses oleh pihak yang berwenang.
Artinya, data sensitif tidak boleh diketahui oleh orang yang tidak memiliki izin.

Contoh nyata:

Penggunaan password atau autentikasi dua faktor (2FA) pada akun email atau mobile banking untuk mencegah orang lain mengakses data pribadi.
Enkripsi data pada aplikasi WhatsApp (end-to-end encryption) sehingga pesan hanya bisa dibaca oleh pengirim dan penerima.
Tujuan: Mencegah kebocoran data dan akses ilegal.

# 2. Integrity (Integritas)

Pengertian:
Menjamin bahwa data tetap utuh, akurat, dan tidak diubah tanpa izin selama penyimpanan atau pengiriman.
Integritas melindungi data dari modifikasi, baik disengaja maupun karena kesalahan sistem.

Contoh nyata:
Checksum atau hash function (misalnya SHA-256) digunakan untuk memastikan file yang diunduh tidak berubah dari versi aslinya.
Dalam sistem keuangan, perubahan saldo rekening harus melalui proses transaksi resmi, bukan manipulasi data oleh pihak tidak sah.
Tujuan: Menjaga keaslian dan keandalan data.

# 3. Availability (Ketersediaan)

Pengertian:
Menjamin bahwa informasi dan sistem selalu dapat diakses oleh pengguna yang berwenang saat dibutuhkan.
Sistem harus tetap berjalan meskipun terjadi gangguan.

Contoh nyata:
Server e-commerce menggunakan backup system dan load balancing agar situs tetap bisa diakses meski terjadi lonjakan pengunjung.
Rumah sakit digital memiliki sistem cadangan listrik dan jaringan untuk menjaga layanan pasien tetap berjalan.
Tujuan: Memastikan layanan tetap aktif dan data dapat diakses tanpa hambatan.

# JAWABAN PERTANYAAN

 # 1. Tokoh yang dianggap sebagai Bapak Kriptografi Modern

      Whitfield Diffie dan Martin Hellman dianggap sebagai bapak kriptografi modern.
      Mereka memperkenalkan konsep kriptografi kunci publik (Public Key Cryptography) pada tahun 1976,
      yang menjadi dasar semua sistem keamanan digital modern seperti SSL, email terenkripsi, dan tanda tangan digital.

 # 2. Algoritma kunci publik yang populer digunakan saat ini

    Beberapa algoritma yang paling banyak digunakan:
    RSA (Rivest–Shamir–Adleman) → digunakan untuk enkripsi dan tanda tangan digital.
    Diffie–Hellman → untuk pertukaran kunci rahasia secara aman.
    Elliptic Curve Cryptography (ECC) → versi lebih efisien dari RSA, banyak digunakan pada perangkat mobile dan blockchain.
    DSA (Digital Signature Algorithm) → khusus untuk verifikasi tanda tangan digital.

 # 3. Perbedaan utama antara kriptografi klasik dan kriptografi modern
    Aspek	Kriptografi Klasik	Kriptografi Modern
    Teknik	Mengandalkan penggantian (substitusi) dan penyusunan ulang (transposisi) huruf.	Menggunakan matematika kompleks dan algoritma komputer.
    Jenis kunci	Hanya kunci simetris (kunci pengirim = kunci penerima).	Ada kunci simetris dan kunci publik (asimetris).
    Media	Digunakan untuk pesan teks (manusia).	Digunakan untuk data digital (komputer & jaringan).
    Contoh	Caesar Cipher, Vigenère Cipher	RSA, AES, ECC, DES, AES
