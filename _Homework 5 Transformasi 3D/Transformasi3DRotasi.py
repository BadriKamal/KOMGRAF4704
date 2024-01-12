import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def rotate_point_3d(x, y, z, theta_x, theta_y, theta_z):
    # Konversi sudut dari derajat ke radian
    theta_x_rad = np.radians(theta_x)
    theta_y_rad = np.radians(theta_y)
    theta_z_rad = np.radians(theta_z)

    # Matriks rotasi untuk sumbu x
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(theta_x_rad), -np.sin(theta_x_rad)],
                    [0, np.sin(theta_x_rad), np.cos(theta_x_rad)]])

    # Matriks rotasi untuk sumbu y
    R_y = np.array([[np.cos(theta_y_rad), 0, np.sin(theta_y_rad)],
                    [0, 1, 0],
                    [-np.sin(theta_y_rad), 0, np.cos(theta_y_rad)]])

    # Matriks rotasi untuk sumbu z
    R_z = np.array([[np.cos(theta_z_rad), -np.sin(theta_z_rad), 0],
                    [np.sin(theta_z_rad), np.cos(theta_z_rad), 0],
                    [0, 0, 1]])

    # Gabungkan matriks rotasi untuk semua sumbu
    R_combined = np.dot(R_z, np.dot(R_y, R_x))

    # Koordinat titik yang dirotasi
    point_rotated = np.dot(R_combined, np.array([x, y, z]))

    return point_rotated[0], point_rotated[1], point_rotated[2]

# Koordinat awal titik 3D
x_awal, y_awal, z_awal = 1, 2, 3

# Sudut rotasi pada masing-masing sumbu (misalnya, theta_x = 30, theta_y = 45, theta_z = 60)
theta_x, theta_y, theta_z = 30, 45, 60

# Panggil fungsi rotate_point_3d untuk mendapatkan koordinat titik 3D yang telah dirotasi
x_rotated, y_rotated, z_rotated = rotate_point_3d(x_awal, y_awal, z_awal, theta_x, theta_y, theta_z)

# Inisialisasi plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot titik awal
ax.scatter(x_awal, y_awal, z_awal, color='blue', label='Titik Awal')

# Plot titik yang telah dirotasi
ax.scatter(x_rotated, y_rotated, z_rotated, color='red', label='Titik yang Dirotasi')

# Atur batas plot agar sesuai dengan koordinat titik
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])

# Tambahkan label dan legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Transformasi 3D Rotasi')

# Tampilkan legend di kanan bawah
ax.legend(loc='lower right')

# Tampilkan plot
plt.show()
