#include <iostream>
#include <vector>
#include <sstream>
#include <string>

int main() {
    int filas, columnas;
    
    std::cout << "Ingrese el número de filas de la matriz: ";
    std::cin >> filas;
    
    std::cout << "Ingrese el número de columnas de la matriz: ";
    std::cin >> columnas;
    
    std::vector<std::vector<int>> matriz(filas, std::vector<int>(columnas, 0)); // Crear una matriz de tamaño especificado y llenarla con ceros
    
    std::cin.ignore(); // Ignorar el salto de línea después de ingresar el número de columnas
    
    for (int i = 0; i < filas; i++) {
        bool entrada_invalida = true;
        while (entrada_invalida) {
            std::string fila_input;
            std::cout << "Ingrese " << columnas << " elementos para la fila " << i + 1 << ": ";
            std::getline(std::cin, fila_input); // Leer una línea completa
            
            std::stringstream ss(fila_input);
            int elemento;
            int elementos_leidos = 0;
            
            while (ss >> elemento) {
                matriz[i][elementos_leidos] = elemento;
                elementos_leidos++;
            }
            
            if (elementos_leidos == columnas) {
                entrada_invalida = false;
            } else {
                std::cout << "Error: Debe ingresar exactamente " << columnas << " elementos." << std::endl;
            }
        }
    }
    
    // Imprimir la matriz
    std::cout << "Matriz ingresada por el usuario:" << std::endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            std::cout << matriz[i][j] << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
