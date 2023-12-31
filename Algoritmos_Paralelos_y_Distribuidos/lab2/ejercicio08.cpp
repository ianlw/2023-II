#include <iostream>
#include <omp.h>
#include <vector>

using namespace std;

int i;
void sumar(vector<int> vector)
{
    int contador = 0;
    for (i = 0; i < vector.size(); i++)
    {
        contador += vector[i];
    }
    cout << "suma del vector" << contador << endl;
}

int main()
{
    vector<int> A = {10, 20, 40, 60, 80};
    vector<int> B = {30, 50, 70, 90, 10};
    #pragma omp parallel num_threads(2) shared(A)
    {
        sumar(A);
        // sumar(B);
    }

    // printf("Este es el hilo %d de un total de %d\n", tid, nth);
    getchar();
    return 0;
}
