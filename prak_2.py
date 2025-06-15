# PRAKTIKUM 2

import numpy as np

# Fungsi yang ingin diintegrasikan
def f(x):
    return np.sin(x)  # Ganti dengan fungsi lain jika perlu

# Metode Trapezoidal untuk level dasar Romberg
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# Metode Romberg dengan ekstrapolasi Richardson
def romberg(f, a, b, max_order):
    R = [[0.0 for _ in range(max_order)] for _ in range(max_order)]

    # Baris pertama: trapezoidal dengan 1, 2, 4, ..., 2^(max_order-1) subinterval
    for i in range(max_order):
        n = 2 ** i
        R[i][0] = trapezoidal(f, a, b, n)

    # Ekstrapolasi Richardson untuk meningkatkan akurasi
    for i in range(1, max_order):
        for k in range(1, i + 1):
            R[i][k] = (4*k * R[i][k-1] - R[i-1][k-1]) / (4*k - 1)

    return R
    
# ==== Parameter Integrasi ====
a = 0              # Batas bawah
b = np.pi          # Batas atas
max_order = 5      # Orde Romberg (semakin besar, semakin akurat)

# ==== Hitung Integrasi ====
romberg_table = romberg(f, a, b, max_order)

# ==== Tampilkan Tabel Romberg ====
print("Tabel Romberg:")
for i in range(max_order):
    for j in range(i + 1):
        print(f"{romberg_table[i][j]:.10f}", end="\t")
    print()
    
# ==== Hasil Akhir ====
hasil_akhir = romberg_table[max_order - 1][max_order - 1]
print(f"\nHasil akhir estimasi integral Romberg: {hasil_akhir:.10f}")
