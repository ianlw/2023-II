#include<stdio.h>
#include<omp.h>
#define TAM 10000
int main()
{
	int n, i;
	int ic = 0;
	n = TAM;
	#pragma omp parallel shared (n, ic) private (i)
	for (i = 0; i < n; i++)
	{
		#pragma omp atomic //--acceso exclusivo al contador
		ic += 1;
	}//fin de la región paralela
	printf("Contador : %d \n", ic);
	getchar();
	return 0;
}
