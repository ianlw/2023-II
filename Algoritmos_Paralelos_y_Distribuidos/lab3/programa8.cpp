#include<stdio.h>
#include<omp.h>

int main()
{
	int n, i, a, b;
	#pragma omp parallel shared (a,b) private(i)
	{
		#pragma omp single
		{
			a = 10;
			printf("Esto fue ejecutado por el hilo %d \n", omp_get_thread_num());
			printf("Esto fue ejecutado por el hilo %d \n", omp_get_thread_num());
			printf("Esto fue ejecutado por el hilo %d \n", omp_get_thread_num());
			printf("Esto fue ejecutado por el hilo %d \n", omp_get_thread_num());
			printf("Esto fue ejecutado por el hilo %d \n", omp_get_thread_num());

		} //--una barrera es insertada automáticamente aquí
		#pragma omp for
		for (i = 0; i < 10; i++)
			printf("Ejecutado %d desde for en el hilo %d \n", i,
				omp_get_thread_num());
	}
	getchar();
	return 0;
}
