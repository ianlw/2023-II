#include <iostream>
#include <omp.h>
using namespace std;
int main()
{
    int i;

#pragma omp parallel num_threads(3), private(i)
    {
       
        std::cout << "Imprime ciclo...!\n" << std::endl;

        for (i = 0; i < 10; i++)
        {
            std::cout << "unsaac " << i <<  std::endl;
        }
    }
    std::cout << "Fin de la impresión de ciclos...!\n" << std::endl;
    getchar();
    return 0;
}
