#include <omp.h> 
#include <stdio.h> 
#include <time.h> 
// #include <Windows.h>  
#include <unistd.h>  
#define N 4
double calculo(int veces)
{
    sleep(veces);
    // Sleep(veces);
    return(1);
}

int    i, A[N], nth = -1;
double total;
int main()
{ //--Inicializacion vector de tamaño de tareas   
    for (i = 0; i < N; i++)
        A[i] = 1;
    
    clock_t t;
    t = clock();
    total = 0.0;
    //--probar schedule(static, 4) (dynamic)
    #pragma omp parallel for schedule(runtime) reduction (+:total)
    for (i = 0; i < N; i++)
        total += calculo(A[i]);
    t = clock() - t;
    nth = omp_get_max_threads();
    printf("\n\n Tiempo de ejecucion con %d hilos = %1.3f s\n\n Total= %.2f\n\n", nth,
        ((float)t) / CLOCKS_PER_SEC, total);
    getchar();
    return 0;
}
