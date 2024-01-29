#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 1000
#define ELEMENTO_A_BUSCAR 42

__global__ void sumaRepeticiones(const int* vector, int* resultado, int objetivo, int tamano) {
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    int conteo = 0;

    for (int i = tid; i < tamano; i += blockDim.x * gridDim.x) {
        if (vector[i] == objetivo) {
            conteo++;
        }
    }

    atomicAdd(resultado, conteo);
}

int main() {
    int* h_vector, * d_vector;
    int* h_resultado, * d_resultado;

    // Asignar memoria en el host
    h_vector = (int*)malloc(N * sizeof(int));
    h_resultado = (int*)malloc(sizeof(int));

    // Inicializar el vector con enteros aleatorios
    srand(time(NULL));
    for (int i = 0; i < N; i++) {
        h_vector[i] = rand() % 100;  // Suponiendo enteros aleatorios entre 0 y 99
    }

    // Asignar memoria en el device
    cudaMalloc((void**)&d_vector, N * sizeof(int));
    cudaMalloc((void**)&d_resultado, sizeof(int));

    // Copiar datos del host al device
    cudaMemcpy(d_vector, h_vector, N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_resultado, 0, sizeof(int));

    // Configurar parámetros de lanzamiento del kernel
    int hilosPorBloque = 256;
    int bloquesPorGrid = (N + hilosPorBloque - 1) / hilosPorBloque;

    // Lanzar el kernel
    sumaRepeticiones<<<bloquesPorGrid, hilosPorBloque>>>(d_vector, d_resultado, ELEMENTO_A_BUSCAR, N);

    // Copiar el resultado del device al host
    cudaMemcpy(h_resultado, d_resultado, sizeof(int), cudaMemcpyDeviceToHost);

    // Imprimir el resultado
    printf("Suma de ocurrencias de %d: %d\n", ELEMENTO_A_BUSCAR, *h_resultado);

    // Liberar memoria
    free(h_vector);
    free(h_resultado);
    cudaFree(d_vector);
    cudaFree(d_resultado);

    return 0;
}

