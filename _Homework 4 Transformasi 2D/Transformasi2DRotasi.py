import math
import matplotlib.pyplot as plt

def rotate_point(x, y, angle_degrees):
    # Konversi sudut dari derajat ke radian
    angle_radians = math.radians(angle_degrees)

    # Hitung koordinat titik yang dirotasi
    x_rotated = x * math.cos(angle_radians) - y * math.sin(angle_radians)
    y_rotated = x * math.sin(angle_radians) + y * math.cos(angle_radians)

    return x_rotated, y_rotated

# Koordinat awal titik
x_awal, y_awal = 3, 4

# Sudut rotasi (misalnya, 45 derajat)
sudut_rotasi = 90

# Panggil fungsi rotate_point untuk mendapatkan koordinat titik yang dirotasi
x_rotasi, y_rotasi = rotate_point(x_awal, y_awal, sudut_rotasi)

# Plot titik awal
plt.scatter(x_awal, y_awal, color='blue', label='Titik Awal')

# Plot titik yang dirotasi
plt.scatter(x_rotasi, y_rotasi, color='red', label='Titik yang Dirotasi')

# Atur batas plot agar sesuai dengan koordinat titik
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Tambahkan label dan legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Transformasi 2D Rotasi')
plt.legend(loc='lower right')

# Tampilkan grid
plt.grid(True)

# Tampilkan plot
plt.show()
