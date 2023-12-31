#include <iostream>
#include <omp.h>
int main()
{
#pragma omp parallel
	{
		std::cout << "Hola Mundo...!\n" << std::endl;
	}

	std::cout << "Adios...!\n" << std::endl;
	getchar();
	return 0;
}
