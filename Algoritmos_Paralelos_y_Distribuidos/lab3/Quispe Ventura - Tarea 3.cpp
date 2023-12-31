#include <cstdio>
#include <iostream>
#include <omp.h>

using namespace std;

void secuencial(int n)
{
    double TInicioSecuencial = omp_get_wtime();
    int sumaSecuencial = 0;

    // Cálculo SECUENCIAL de la suma de los n primeros números
    for (int i = 1; i <= n; i++)
    {
        sumaSecuencial += i;
    }
    double TFinSecuencial = omp_get_wtime();
    cout << "Suma secuencial: " << sumaSecuencial << endl;
    cout << "Tiempo secuencial: " << TFinSecuencial - TInicioSecuencial << " segundos" << endl;
}

void paralelo(int n)
{
    double TInicioParalelo = omp_get_wtime();
    long long sumaParalelo = 0;

    // Cálculo PARALELO De la suma de los n primeros números
    #pragma omp parallel for num_threads(8) schedule(dynamic, 2) reduction(+ : sumaParalelo) // Se usa dynamic porque no se sabe el valor de n hasta la ejecución
    for (int i = 1; i <= n; i++)
    {
        sumaParalelo += i;
    }
    double TFinParalelo = omp_get_wtime();

    cout << "Suma paralela: " << sumaParalelo << endl;
    cout << "Tiempo paralelo: " << TFinParalelo - TInicioParalelo << " segundos" << endl;
}

int main()
{
    int n;
    // Ingresar por teclado un número entero positivo n.
    cout << "Ingrese un número entero positivo n: ";
    cin >> n;

    while (n <= 0)
    {
        cout << "El número ingresado debe ser un entero positivo.\n";
        cout << "Ingrese un número entero positivo n: ";
        cin >> n;
    }

    secuencial(n);
    paralelo(n);

    getchar();
    return 0;
}
