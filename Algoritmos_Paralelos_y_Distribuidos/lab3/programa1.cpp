#include<stdio.h>
#include<omp.h>
int main()
{
	int i, n;
	n = 10;
	#pragma omp parallel shared(n) private (i) num_threads(4)
	{
	#pragma omp for //--clausula para paralelizar el ciclo
		for (i = 0; i < n; i++)
			printf("El hilo %d esta ejecutando el ciclo %d \n", omp_get_thread_num(), i);
	}
	getchar();
	return 0;
}
