#include <iostream>
#include <omp.h>
using namespace std;
int main()
{
#pragma omp parallel num_threads(1)
    {
        std::cout << "Imprime ciclo...!\n" << std::endl;
        
        int i; //--variable local
        for (i = 0; i < 10; i++)
        {
            std::cout << "unsaac " << i << std::endl;
        }
    }
    std::cout << "Fin de la impresión de ciclos...!\n" << std::endl;
    getchar();
    return 0;
}
