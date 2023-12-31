#include<iostream>
#include<stdio.h>
#include<omp.h>
#include<ctime>
#define TAM 10000
int main()
{
	int sum = 0;
	int n, TID, sumLocal, i;
	int a[TAM];
	n = TAM;
	//--Cargar un vector con números aleatorios
	srand(time(0)); //se establece el número semilla
	for (int x = 0; x < TAM; x++) {
		a[x] = rand() % 10000;
	}//for
	#pragma omp parallel shared (n, a, sum) private (TID, sumLocal )
	{
		TID = omp_get_thread_num();
		sumLocal = 0;
		#pragma omp for
		for (i = 0; i < n; i++)
			sumLocal += a[i];
		#pragma omp critical
		{
			sum += sumLocal;
			printf("TID=%d : sumLocal=%d sum=%d \n", TID, sumLocal, sum);
		}
	}//Fin de la región paralela
	printf("Valor de suma despues de la region paralela : %d", sum);
	getchar();
	return 0;
}
