#include <stdio.h>
#include <omp.h>

// Función a integrar
double funcion(double x) {
    return (x * x * x) / 3 + 4 * x; 
}

int main() {
    // Número de los rectángulos
    int n = 1000000; 
    // Límites de integración
    double a = 0.0;
    double b = 1.0; 
    // Ancho de los rectángulos
    double h = (b - a) / n; 
    double integral;

    double start = omp_get_wtime();
    // Calcular de forma paralela
    #pragma omp parallel for reduction(+:integral)
    for (int i = 0; i < n; i++) {
        // calcular el valor de x para el i-ésimo rectángulo
        double x = a + i * h;
        // calcular el área del i-ésimo rectángulo
        integral += funcion(x) * h;
    }
    double end = omp_get_wtime();
    double tiempo_paralelo = end - start;

    printf("Integral = %f\n", integral);

    // Cálcular de forma secuencial 
    integral = 0.0;
    start = omp_get_wtime();
    for (int i = 0; i < n; i++) {
        // calcular el valor de x para el i-ésimo rectángulo
        double x = a + i * h;
        // calcular el área del i-ésimo rectángulo
        integral += funcion(x) * h;
    }
    end = omp_get_wtime();
    double tiempo_secuencial = end - start;

    printf("Integral (secuencial) = %f\n", integral);

    // Cálculo del speedup y la eficiencia
    double speedup = tiempo_secuencial / tiempo_paralelo;
    double eficiencia = speedup / omp_get_max_threads();

    printf("Speedup = %f\n", speedup);
    printf("Eficiencia = %f\n", eficiencia);

    return 0;
}

