#include <iostream>
#include <thread>
#include <vector>

// Función para sumar los elementos de un rango del arreglo
void sumRange(const std::vector<int>& arr, int start, int end, int& result) {
    int partialSum = 0;
    for (int i = start; i < end; ++i) {
        partialSum += arr[i];
    }
    result = partialSum;
}

int main() {
    // Arreglos de ejemplo
    std::vector<int> arr1 = {1, 2, 3, 4, 5};
    std::vector<int> arr2 = {6, 7, 8, 9, 10};

    // Número de elementos en cada arreglo
    int N = arr1.size();

    // Dividir los arreglos en dos partes iguales
    int mid = N / 2;

    // Variables para almacenar los resultados parciales
    int result1, result2;

    // Crear dos hilos para sumar las partes de los arreglos de forma paralela
    std::thread thread1(sumRange, std::ref(arr1), 0, mid, std::ref(result1));
    std::thread thread2(sumRange, std::ref(arr2), 0, mid, std::ref(result2));

    // Esperar a que ambos hilos terminen
    thread1.join();
    thread2.join();

    // Sumar los resultados parciales para obtener la suma total
    int totalSum = result1 + result2;

    // Imprimir el resultado
    std::cout << "La suma total es: " << totalSum << std::endl;

    return 0;
}
