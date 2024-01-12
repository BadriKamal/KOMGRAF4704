import numpy as np
import matplotlib.pyplot as plt

def draw_line_Bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    y = y1
    points = []

    for x in range(x1, x2 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))
        if p >= 0:
            y += 1 if y1 < y2 else -1
            p -= 2 * dx
        p += 2 * dy

    return points

# Koordinat titik awal A dan titik akhir B
x1, y1 = 10, 1
x2, y2 = 0, 7

# Gambar garis dengan algoritma Bresenham
line_points = draw_line_Bresenham(x1, y1, x2, y2)

# Tampilkan hasilnya
for point in line_points:
    print(point)

# Plot titik-titik awal
plt.scatter([x1,x2],[y1,y2], color='blue', label='Garis Asli')
plt.plot([x1,x2],[y1,y2], linestyle='-', color='blue', linewidth=2)

# Plot titik-titik bressenham
x, y = zip(*line_points)
plt.scatter(x,y, color='red', label='Bressenham')
plt.plot(x, y, linestyle='-', color='red', linewidth=2)

# Plot garis menggunakan matplotlib

plt.title('Garis menggunakan Algoritma Bresenham')
plt.grid()
plt.legend()
plt.xlabel('Koordinat X')
plt.ylabel('Koordinat Y')
plt.show()
