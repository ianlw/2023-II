#include <iostream>
#include <vector>
#include <sstream>
#include <string>

// Función para ingresar una fila de la matriz
void ingresarFila(std::vector<int>& fila, int columnas) {
    bool entrada_invalida = true;
        std::cout << "Ingrese " << columnas << " elementos separados por espacios: ";
    while (entrada_invalida) {
        std::string fila_input;
        std::getline(std::cin, fila_input); // Leer una línea completa
        
        std::stringstream ss(fila_input);
        int elemento;
        int elementos_leidos = 0;
        
        while (ss >> elemento) {
            fila.push_back(elemento);
            elementos_leidos++;
        }
        
        if (elementos_leidos == columnas) {
            entrada_invalida = false;
        } else {
            std::cout << "Error: Debe ingresar exactamente " << columnas << " elementos." << std::endl;
            fila.clear(); // Limpiar la fila si la entrada es incorrecta
        }
    }
}

// Función para ingresar la matriz
void ingresarMatriz(std::vector<std::vector<int>>& matriz, int filas, int columnas) {
    matriz.resize(filas, std::vector<int>(columnas, 0));
    for (int i = 0; i < filas; i++) {
        std::vector<int> fila;
        ingresarFila(fila, columnas);
        matriz[i] = fila;
    }
}

// Función para imprimir la matriz
void imprimirMatriz(const std::vector<std::vector<int>>& matriz) {
    std::cout << "Matriz ingresada por el usuario:" << std::endl;
    for (const auto& fila : matriz) {
        for (int elemento : fila) {
            std::cout << elemento << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    int filas, columnas;
    
    std::cout << "Ingrese el número de filas de la matriz: ";
    std::cin >> filas;
    
    std::cout << "Ingrese el número de columnas de la matriz: ";
    std::cin >> columnas;
    
    std::cin.ignore(); // Ignorar el salto de línea después de ingresar el número de columnas
    
    std::vector<std::vector<int>> matriz;
    
    ingresarMatriz(matriz, filas, columnas);
    
    imprimirMatriz(matriz);
    
    return 0;
}
