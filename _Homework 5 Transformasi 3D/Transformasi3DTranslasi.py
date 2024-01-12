import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translate_point_3d(x, y, z, tx, ty, tz):
    # Melakukan translasi pada koordinat titik 3D
    x_translated = x + tx
    y_translated = y + ty
    z_translated = z + tz

    return x_translated, y_translated, z_translated

# Koordinat awal titik 3D
x_awal, y_awal, z_awal = 5, 5, 5

# Jumlah translasi pada sumbu x, y, dan z (misalnya, tx = 2, ty = -1, tz = 3)
tx, ty, tz = 2, -1, 3

# Panggil fungsi translate_point_3d untuk mendapatkan koordinat titik 3D yang telah di-translasi
x_translated, y_translated, z_translated = translate_point_3d(x_awal, y_awal, z_awal, tx, ty, tz)

# Inisialisasi plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot titik awal
ax.scatter(x_awal, y_awal, z_awal, color='blue', label='Titik Awal')

# Plot titik yang telah di-translasi
ax.scatter(x_translated, y_translated, z_translated, color='red', label='Titik yang Di-Translasi')

# Atur batas plot agar sesuai dengan koordinat titik
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])

# Tambahkan label dan legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Transformasi 3D Translasi')

# Tampilkan legend di kanan bawah
ax.legend(loc='lower right')

# Tampilkan plot
plt.show()
