#include<stdio.h>
#include<omp.h>

void func(int num)
{
	printf("En la funcion no %d que se ejecuta 1\n", num);
	printf("En la funcion no %d que se ejecuta 2\n", num);
	printf("En la funcion no %d que se ejecuta 3\n", num);
	printf("En la funcion no %d que se ejecuta 4\n", num);
}
void funcA()
{
	printf("funcA: esta section es ejecutada por el hilo %d\n",
		omp_get_thread_num());
}

void funcB()
{
	printf("funcB: esta section es ejecutada por el hilo %d\n",
		omp_get_thread_num());
}


int main()
{
	int i, n;
	n = 10;
	#pragma omp parallel shared(n) private (i)
	{
		#pragma omp sections
		{
			#pragma omp section
			(void)funcA();
			#pragma omp section
			(void)funcB();
			#pragma omp section
			(void)func(3);
		}
	}
	getchar();
	return 0;
}
