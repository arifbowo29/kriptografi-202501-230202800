import random

# parameter publik
p = 23
g = 5

# =====================
# Secret key masing-masing
# =====================
a = random.randint(1, p-1)  # Alice
b = random.randint(1, p-1)  # Bob
e = random.randint(1, p-1)  # Eve (penyerang)

# =====================
# Public key asli
# =====================
A = pow(g, a, p)  # Alice
B = pow(g, b, p)  # Bob
E = pow(g, e, p)  # Eve

# =====================
# MITM: Eve mengganti public key
# =====================
# Alice menerima public key palsu dari Eve
shared_Alice = pow(E, a, p)

# Bob menerima public key palsu dari Eve
shared_Bob = pow(E, b, p)

# Eve menghitung dua kunci
shared_Eve_with_Alice = pow(A, e, p)
shared_Eve_with_Bob   = pow(B, e, p)

# =====================
# Output
# =====================
print("Kunci Alice (dengan Eve):", shared_Alice)
print("Kunci Bob   (dengan Eve):", shared_Bob)
print("Kunci Eve - Alice       :", shared_Eve_with_Alice)
print("Kunci Eve - Bob         :", shared_Eve_with_Bob)
