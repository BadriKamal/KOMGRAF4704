import numpy as np
import matplotlib.pyplot as plt

# Titik A(1, 5) dan B(0, 7), Karena cara pembacaan plot ada
points = np.array([[1, 0], [1, 7]])

# Faktor skala
sx = 3  
sy = 4  

# Terapkan transformasi skala
scaled_points = np.dot(np.array([[sx, 0], [0, sy]]), points)


# Plot titik-titik awal
plt.scatter(points[0], points[1], color='blue', label='Awal')
plt.plot(points[0], points[1], linestyle='-', color='blue', linewidth=2)

# Plot titik-titik yang telah di skala
plt.scatter(scaled_points[0], scaled_points[1], color='red', label='Setelah Skala')
plt.plot(scaled_points[0], scaled_points[1], linestyle='-', color='red', linewidth=2)

# Plot garis menggunakan matplotlib
plt.grid()
plt.legend()
plt.title('Transformasi 2D Skala')
plt.xlabel('Koordinat X')
plt.ylabel('Koordinat Y')
plt.show()
