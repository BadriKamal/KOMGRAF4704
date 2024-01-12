def calculate_region(x, y, x_min, x_max, y_min, y_max):
    region = 0

    if x < x_min:
        region |= 1  # Set L bit
    elif x > x_max:
        region |= 2  # Set R bit

    if y < y_min:
        region |= 4  # Set B bit
    elif y > y_max:
        region |= 8  # Set T bit

    return region


def cohen_sutherland_clipping(x_min, x_max, y_min, y_max, x1, y1, x2, y2):
    code1 = calculate_region(x1, y1, x_min, x_max, y_min, y_max)
    code2 = calculate_region(x2, y2, x_min, x_max, y_min, y_max)

    while (code1 | code2) != 0:  # Mengecek apakah garis ada di dalam viewport ?
        if (code1 & code2) != 0:  
            return None

        
        code_outside = code1 if code1 != 0 else code2

        x, y = 0, 0  # Inisialisasi nilai titik potong

        # Menghitung titik potong
        if code_outside & 1:  # Left
            x = x_min
            y = y1 + (y2 - y1) / (x2 - x1) * (x_min - x1)
        elif code_outside & 2:  # Right
            x = x_max
            y = y1 + (y2 - y1) / (x2 - x1) * (x_max - x1)
        elif code_outside & 4:  # Bottom
            y = y_min
            x = x1 + (x2 - x1) / (y2 - y1) * (y_min - y1)
        elif code_outside & 8:  # Top
            y = y_max
            x = x1 + (x2 - x1) / (y2 - y1) * (y_max - y1)

        # Mengganti titik luar dengan titik potong
        if code_outside == code1:
            x1, y1 = x, y
            code1 = calculate_region(x1, y1, x_min, x_max, y_min, y_max)
        else:
            x2, y2 = x, y
            code2 = calculate_region(x2, y2, x_min, x_max, y_min, y_max)

    # Hasil akhir titik potong
    return (x1, y1, x2, y2)

# Titik untuk area clipping / viewport
x_min = 1
x_max = 4
y_min = 1
y_max = 5

# Titik yang ditentukan :
x1, y1 = -1, -2
x2, y2 = 5, 6

result = cohen_sutherland_clipping(x_min, x_max, y_min, y_max, x1, y1, x2, y2)
print(result)
