import matplotlib.pyplot as plt

def mirror_point(x, y, axis):
    # Melakukan pencerminan pada koordinat titik tergantung sumbu yang dipilih
    if axis == 'x':
        y_mirrored = -y
        return x, y_mirrored
    elif axis == 'y':
        x_mirrored = -x
        return x_mirrored, y
    else:
        raise ValueError("Sumbu harus 'x' atau 'y'.")

# Koordinat awal titik
x_awal, y_awal = 3, 4

# Pilih sumbu untuk pencerminan ('x' atau 'y')
sumbu_pencerminan = 'y'

# Panggil fungsi mirror_point untuk mendapatkan koordinat titik yang telah dipermirrored
x_mirrored, y_mirrored = mirror_point(x_awal, y_awal, sumbu_pencerminan)

# Plot titik awal
plt.scatter(x_awal, y_awal, color='blue', label='Titik Awal')

# Plot titik yang telah dipermirrored
plt.scatter(x_mirrored, y_mirrored, color='red', label='Titik yang Di-Permirror')

# Atur batas plot agar sesuai dengan koordinat titik
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Tambahkan label dan legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Transformasi 2D Mirror')

# Tampilkan grid
plt.grid(True)

# Tampilkan legend di kanan bawah
plt.legend(loc='lower left')

# Tampilkan plot
plt.show()
