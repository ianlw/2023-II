#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include "omp.h"

#define MAX_SIZE_VISIBLE 100
int main(int argc, char* argv[])
{
	int* a;
	unsigned long long int size, i;
	double start, end;
	double parallel, sequential;
	int n, j;
	// Es necesario tener dos argumentos en la línea de comandos
	// de lo contrario se interrumpirá el programa y mostrará
	// un mensaje explicando el uso del mismo.
	if (argc <= 2)
	{
		printf("Faltan argumentos, el uso correcto es :\n\ tseq[tamaño de lista][numero a buscar] \n");
		return 1;
	}
	// Transformamos los argumentos en numeros
	size = strtoull(argv[1], NULL, 10);
	n = atoi(argv[2]);
	printf("Elementos en la lista : %llu \n Número a buscar : %d \n", size, n);
	// Alojando dinamicamente un arreglo para guardar los valores
	// aleatorios .
	a = (int*)malloc(size * sizeof(unsigned long long int));
	// Generacion de numeros aleatorios .
	printf("Generando numeros aleatorios en la lista . . . \n");
	srand(time(NULL));
	for (i = 0; i < size; i++)
	{
		a[i] = rand() % 1000;
	}
	if (size < MAX_SIZE_VISIBLE)
	{
		for (i = 0; i < size; i++)
		{
			printf(" %llu : %d \n", i, a[i]);
		}
	}
	else
	{
		printf("Lista demasiado grande para mostrarse en pantalla. \n");
		{
			//Inicio de busqueda secuencial
			printf("Buscando . . . \n");
			j = 0;
			start = omp_get_wtime();
			for (i = 0; i < size; i++)
			{
				if (a[i] == n)
				{
					// Impresion de resultados
					printf("%d se encuentra en la posicion %llu \n", n, i);
					j = 1;
				}
			}
		}
		if (!j)
		{
			printf("No se encontró el numero \n");
		}
		end = omp_get_wtime();
		printf("Procesamiento secuencial %f \n", end - start);
		sequential = end - start;
		j = 0;
		start = omp_get_wtime();
		int i;
		#pragma omp parallel for default(none) firstprivate(size, n, a) private(i) shared(j)
		for (i = 0; i < size; i++)
		{
			if (a[i] == n)
			{
				// Impresion de resultados
				printf("%d se encuentra en la posicion	%llu \n", n, i);
				j = 1;
			}
		}
		if (!j)
		{
			printf("No se encontro el numero \n");
		}
		end = omp_get_wtime();
		printf("Procesamiento paralelo %f \n", end - start);
		parallel = end - start;
		printf("\n\n Tamaño n tSecuencial	n tParalelo \n");
		printf("Resultado : %llu nt %f nt %f \n", size, sequential, parallel);
		//Liberando la memoria reservada
		free(a);
		return 0;
	}
}
