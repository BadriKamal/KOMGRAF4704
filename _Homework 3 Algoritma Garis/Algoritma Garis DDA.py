import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Hitung langkah yang lebih besar antara dx dan dy
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Hitung perubahan x dan y per langkah
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)

    # Inisialisasi koordinat awal
    x, y = x1, y1

    # Buat list untuk menyimpan titik-titik garis
    points = [(round(x), round(y))]

    # Loop melalui langkah-langkah dan tambahkan titik-titik pada garis
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points

# Koordinat titik awal A dan titik akhir B
x1, y1 = 10, 1
x2, y2 = 0, 7

# Gambar garis dengan DDA
line_points = draw_line_DDA(x1, y1, x2, y2)

# Tampilkan hasilnya
for point in line_points:
    print(point)

# Plot titik-titik awal
plt.scatter([x1,x2],[y1,y2], color='blue', label='Garis Asli')
plt.plot([x1,x2],[y1,y2], linestyle='-', color='blue', linewidth=2)

# Plot titik-titik DDA
x, y = zip(*line_points)
plt.scatter(x,y, color='red', label='DDA')
plt.plot(x, y, linestyle='-', color='red', linewidth=2)

# Plot garis menggunakan matplotlib
plt.title('Garis menggunakan Algoritma DDA')
plt.grid()
plt.legend()
plt.xlabel('Koordinat X')
plt.ylabel('Koordinat Y')
plt.show()
