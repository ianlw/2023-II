#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <iostream>

#define N 6 

__global__ void encontrarEstrella(int* matriz, int* salida) {
    int i = blockIdx.y * blockDim.y + threadIdx.y + 1;
    int j = blockIdx.x * blockDim.x + threadIdx.x + 1;

    int suma = matriz[i * N + j] + matriz[(i - 1) * N + j] + matriz[(i + 1) * N + j] + matriz[i * N + j - 1] + matriz[i * N + j + 1];

    if (suma > 30) {
        salida[i * N + j] = 1;
    } else {
        salida[i * N + j] = 0;
    }
}

int main() {
    int* h_matriz, * h_matrizEstrella;
    int* d_matriz, * d_matrizEstrella;

    // Matriz con valores del 0 al 20 
    h_matriz = (int*)malloc(N * N * sizeof(int));
    for (int i = 0; i < N * N; ++i) {
        h_matriz[i] = rand() % 21;
    }

    // Reservar memoria en el dispositivo
    cudaMalloc((void**)&d_matriz, N * N * sizeof(int));
    cudaMalloc((void**)&d_matrizEstrella, N * N * sizeof(int));

    // Copiar datos de host a dispositivo
    cudaMemcpy(d_matriz, h_matriz, N * N * sizeof(int), cudaMemcpyHostToDevice);

    // Kernel
    dim3 dimGrid(1, 1);
    // No se toma en cuenta las dos filas ni las dos columnas que forman a los bordes
    dim3 dimBlock(N - 2, N - 2);  

    // Lanzar el kernel
    encontrarEstrella<<<dimGrid, dimBlock>>>(d_matriz, d_matrizEstrella);

    // Copiar resultado de dispositivo a host
    h_matrizEstrella = (int*)malloc(N * N * sizeof(int));
    cudaMemcpy(h_matrizEstrella, d_matrizEstrella, N * N * sizeof(int), cudaMemcpyDeviceToHost);

    // Imprimir matriz original
    std::cout << "Matriz Original:\n";
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cout << h_matriz[i * N + j] << " ";
        }
        std::cout << "\n";
    }

    // Imprimir matriz resultante
    std::cout << "\nMatriz Resultante:\n";
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            std::cout << h_matrizEstrella[i * N + j] << " ";
        }
        std::cout << "\n";
    }

    // Liberar memoria en el dispositivo y host
    free(h_matriz);
    free(h_matrizEstrella);
    cudaFree(d_matriz);
    cudaFree(d_matrizEstrella);

    return 0;
}

