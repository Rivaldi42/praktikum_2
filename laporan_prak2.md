# Metode Integrasi Romberg
## Import Library

    import numpy as np
```Digunakan untuk meng-import fungsi fungsi di dalam numpy yang akan digunakan dalam program ini```

## Definisi Fungsi yang Ingin Diintegrasikan 
    
    def f(x):
        return np.sin(x)
```Mendefinisikan fungsi apa yang ingin di integralkan dengam metode integrasi Romberg```
## Fungsi Trapezoidal
    def trapezoidal(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h
```Fungsi Trapezoidal, berisi program iterasi untuk menghitung integrasi suatu fungsi dengan metode Trapezoidal, hal ini dikarenakan metode Romberg merupakan buffer untuk meningkatkan efisiensi dari Fungsi Trapezoidal sehingga dalam program ini fungsi perhitungan Trapezoidal tetap diperlukan sebagai fungsi dasar nya```

## Fungsi Romberg
    def romberg(f, a, b, max_order):
    R = [[0.0 for _ in range(max_order)] for _ in range(max_order)]

    # Trapezoidal dengan subinterval 2^1 
    for i in range(max_order):
        n = 2 ** i
        R[i][0] = trapezoidal(f, a, b, n)
        
    # Iterasi dengan Rumus Ekstrapolasi Richardson     
    for i in range(1, max_order):
        for k in range(1, i + 1):
            R[i][k] = (4**k * R[i][k-1] - R[i-1][k-1]) / (4**k - 1)

    return R
```Fungsi ini menjalankan algoritma Romberg. R[1][0] sebagai hasil trapezoidal dengan 2^1 subinterval nya. Baris demi baris dihitung, lalu disempurnakan menggunakan ekstrapolasi Richardson```
## Variabel Integrasi
    a = 0              # Batas bawah
    b = np.pi          # Batas atas
    max_order = 5      # Orde Romberg
```Variabel untuk batas bawah, atas integrasi dan juga banyak nya iterasi yang diinginkan. Semakin banyak iterasi yang dilakukan semakin akurat hasilnya```
## Hitung Integrasi Romberg
    romberg_table = romberg(f, a, b, max_order)
```Hitung hasil dari integrasi Romberg dengan menginputkan variabel yang ditentukan di kode sebelum nya ke dalam fungsi romberg```
## Tampilkan Integrasi Romberg
    print("Tabel Romberg:")
    for i in range(max_order):
        for j in range(i + 1):
            print(f"{romberg_table[i][j]:.10f}", end="\t")
        print()
  ```Tampilkan hasil tabel iterasi Integrasi Romberg```
## Hasil Integrasi Romberg
    hasil_akhir = romberg_table[max_order - 1][max_order - 1]
    print(f"\nHasil akhir estimasi integral Romberg: {hasil_akhir:.10f}")
  ```Menampilkan hasil akhir dari perhitungan integrasi Romberg```

```Kesimpulan:```

```Metode Integrasi Romberg lebih efisien dapat dilihat dari banyaknya iterasi yang diperlukan. untuk mendapatkan hasil aprokmasi yang diinginkan metode integrasi Romberg membutuhkan lebih sedikit iterasi dibandingkan dengan metode trapezoidal.```
