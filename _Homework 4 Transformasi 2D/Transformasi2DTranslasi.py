import matplotlib.pyplot as plt

def translate_point(x, y, tx, ty):
    # Melakukan translasi pada koordinat titik
    x_translated = x + tx
    y_translated = y + ty

    return x_translated, y_translated

# Koordinat awal titik
x_awal, y_awal = 3, 4

# Jumlah translasi pada sumbu x dan y (misalnya, tx = 2, ty = -1)
tx, ty = 2, -1

# Panggil fungsi translate_point untuk mendapatkan koordinat titik yang telah di-translasi
x_translated, y_translated = translate_point(x_awal, y_awal, tx, ty)

# Plot titik awal
plt.scatter(x_awal, y_awal, color='blue', label='Titik Awal')

# Plot titik yang telah di-translasi
plt.scatter(x_translated, y_translated, color='red', label='Titik yang Di-Translasi')

# Atur batas plot agar sesuai dengan koordinat titik
plt.xlim(-1, 6)
plt.ylim(-2, 5)

# Tambahkan label dan legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Transformasi 2D Translasi')

# Tampilkan grid
plt.grid(True)

# Tampilkan legend
plt.legend(loc='lower right')

# Tampilkan plot
plt.show()
