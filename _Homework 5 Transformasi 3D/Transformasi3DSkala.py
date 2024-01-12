import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def scale_line(center, line, sx, sy, sz):
    # Terapkan skala ke setiap titik dalam garis
    scaled_line = [center + np.dot(point - center, np.diag([sx, sy, sz])) for point in line]

    return scaled_line

# Inisialisasi plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Koordinat dan skala awal garis (2 titik)
center = np.array([1, 1, 1])
line = [np.array([2, 2, 2]), np.array([3, 3, 3])]
sx, sy, sz = 2, 0.5, 3

# Terapkan transformasi skala ke garis
scaled_line = scale_line(center, line, sx, sy, sz)

# Plot garis awal
ax.plot(*zip(*line), c='blue', marker='o', label='Garis Awal')

# Plot garis yang telah di-scaled
ax.plot(*zip(*scaled_line), c='red', marker='o', label='Garis yang Di-Scaled')

# Atur batas plot agar sesuai dengan koordinat garis
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])

# Tambahkan label dan legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Transformasi 3D Translasi')

# Tampilkan legend di kanan bawah
ax.legend(loc='lower right')

# Tampilkan plot
plt.show()
