#include <iostream>

const int MATRIX_SIZE = 3;

// Fungsi untuk mencetak matriks
void printMatrix(int matrix[MATRIX_SIZE][MATRIX_SIZE]) {
    for (int i = 0; i < MATRIX_SIZE; ++i) {
        for (int j = 0; j < MATRIX_SIZE; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

// Fungsi untuk penjumlahan matriks
void addMatrices(int A[MATRIX_SIZE][MATRIX_SIZE], int B[MATRIX_SIZE][MATRIX_SIZE], int result[MATRIX_SIZE][MATRIX_SIZE]) {
    for (int i = 0; i < MATRIX_SIZE; ++i) {
        for (int j = 0; j < MATRIX_SIZE; ++j) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
}

// Fungsi untuk pengurangan matriks
void subtractMatrices(int A[MATRIX_SIZE][MATRIX_SIZE], int B[MATRIX_SIZE][MATRIX_SIZE], int result[MATRIX_SIZE][MATRIX_SIZE]) {
    for (int i = 0; i < MATRIX_SIZE; ++i) {
        for (int j = 0; j < MATRIX_SIZE; ++j) {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
}

// Fungsi untuk perkalian matriks dengan skalar
void scalarMultiply(int A[MATRIX_SIZE][MATRIX_SIZE], int result[MATRIX_SIZE][MATRIX_SIZE], int scalar) {
    for (int i = 0; i < MATRIX_SIZE; ++i) {
        for (int j = 0; j < MATRIX_SIZE; ++j) {
            result[i][j] = A[i][j] * scalar;
        }
    }
}

// Fungsi untuk perkalian dua matriks
void multiplyMatrices(int A[MATRIX_SIZE][MATRIX_SIZE], int B[MATRIX_SIZE][MATRIX_SIZE], int result[MATRIX_SIZE][MATRIX_SIZE]) {
    for (int i = 0; i < MATRIX_SIZE; ++i) {
        for (int j = 0; j < MATRIX_SIZE; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < MATRIX_SIZE; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    // Matriks A dan B
    int A[MATRIX_SIZE][MATRIX_SIZE] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[MATRIX_SIZE][MATRIX_SIZE] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};

    // Cetak matriks A
    std::cout << "Matriks A:" << std::endl;
    printMatrix(A);

    // Cetak matriks B
    std::cout << "\nMatriks B:" << std::endl;
    printMatrix(B);

    // A + B
    int sum[MATRIX_SIZE][MATRIX_SIZE];
    addMatrices(A, B, sum);
    std::cout << "\nA + B:" << std::endl;
    printMatrix(sum);

    // A - B
    int difference[MATRIX_SIZE][MATRIX_SIZE];
    subtractMatrices(A, B, difference);
    std::cout << "\nA - B:" << std::endl;
    printMatrix(difference);

    // A * n (dikali dengan skalar)
    int scalar = 2;
    int scalarProduct[MATRIX_SIZE][MATRIX_SIZE];
    scalarMultiply(A, scalarProduct, scalar);
    std::cout << "\nA * " << scalar << ":" << std::endl;
    printMatrix(scalarProduct);

    // A * B (perkalian matriks)
    int product[MATRIX_SIZE][MATRIX_SIZE];
    multiplyMatrices(A, B, product);
    std::cout << "\nA * B:" << std::endl;
    printMatrix(product);

    return 0;
}
