#include <iostream>
#include <ostream>
#include <vector>
#include <thread>

using namespace std;

int NroFilas, NroColumnas;
int sumFilas, sumColumnas;

void SumFilas(vector<vector<int>> matriz)
{
    cout << "---------------" << endl;
    cout << " Suma de filas"<< endl;
    cout << "---------------" << endl;
    for (int i = 0; i < NroFilas; i++)
    {
        cout << "Fila " << i + 1 << endl;
        sumFilas = 0;
        for (int j = 0; j < NroColumnas; j++)
        {
            sumFilas += matriz[i][j];
            std::cout << matriz[i][j] << " ";
        }
        std::cout << "suma = " << sumFilas << "\n" << std::endl;
    }
}

void SumColumnas(vector<vector<int>> matriz)
{
    cout << "----------------" << endl;
    cout << "Suma de columnas" << endl;
    cout << "----------------" << endl;
    for (int i = 0; i < NroColumnas; i++)
    {
        cout << "Columna " << i + 1 << endl;
        sumColumnas = 0;
        for (int j = 0; j < NroFilas; j++)
        {
            sumColumnas += matriz[j][i];
            std::cout << matriz[j][i] << endl;
        }
        std::cout << "Suma de columna = " << sumColumnas << "\n"<< std::endl;
    }
}
vector<vector<int>> CrearMatriz()
{
    cout << "Ingrese el número de filas de la matriz: ";
    std::cin >> NroFilas;

    std::cout << "Ingrese el número de columnas de la matriz: ";
    std::cin >> NroColumnas;

    vector<vector<int>> matriz(NroFilas, vector<int>(NroColumnas, 0));

    // Solicitar al usuario que ingrese los elementos de la matriz
    for (int i = 0; i < NroFilas; i++)
    {
        for (int j = 0; j < NroColumnas; j++)
        {
            std::cout << "Matriz --> fila = " << i << " columna = " << j << " : ";
            std::cin >> matriz[i][j];
        }
    }
    return matriz;
    // return matriz;
}
int main()
{
    vector<vector<int>> matriz = CrearMatriz();
    cout << "-----------" << endl;
    cout << "Matriz" << endl;
    cout << "-----------" << endl;

    for (int i = 0; i < NroFilas; i++)
    {
        sumFilas = 0;
        for (int j = 0; j < NroColumnas; j++)
        {
            sumFilas += matriz[i][j];
            std::cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
    // SumFilas(matriz);
    thread t1(SumFilas, matriz);
    thread t2(SumColumnas, matriz);
    t1.join();
    t2.join();
    return 0;
}
