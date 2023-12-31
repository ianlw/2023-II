#include <iostream>
#include <thread>
#include <vector>

using namespace std;

int N;
int contador_general = 0;

void ElementosVector(vector<int>& Vector)
{
    // Solicitar tamaño del vector 
    cout << "Ingrese el tamaño del vector: ";
    cin >> N;

    // Darle al vector el tamaño N 
    Vector.resize(N);

    // Solicitar los elementos del vector 
    std::cout << "\nIngrese los elementos del vector" << std::endl;

    for (int i = 0; i < N; i++)
    {
        std::cout << "Elemento " << i << ": ";
        std::cin >> Vector[i];
    }
}

void sumaVector(std::vector<int> Ventor)
{
    int contador = 0;
    for (int i = 0; i < Ventor.size(); i++)
    {
        contador = contador + Ventor[i];
    }
    contador_general += contador;
}

int main()
{

    /*
     * std::vector<int> A = {10, 20, 40, 60, 80};
     * std::vector<int> B = {10, 20, 40, 60, 80};
     * std::vector<int> C = {10, 20, 40, 60, 80};
     */

    // Declarar los tre vectores
    vector<int> A;
    vector<int> B;
    vector<int> C;

    // Establecer los elements}os de los vectores 
    cout << "Vector 1 \n";
    ElementosVector(A);
    cout << "\nVector 2 \n";
    ElementosVector(B);
    cout << "\nVector 3 \n";
    ElementosVector(C);

    // Manejo de hilos
    thread t1(sumaVector, A);
    thread t2(sumaVector, B);
    thread t3(sumaVector, C);
    t1.join();
    t2.join();
    t3.join();

    cout << "Suma de todos los vectores: " << contador_general << "\n" << std::endl;

    return 0;
}
