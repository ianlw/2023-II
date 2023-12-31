#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
int main(void) {
    int i;
    int x;
    x = 44;
    #pragma omp parallel for private(x)
    for (i = 0; i <= 10; i++) {
        x = i;
        printf("Nro. de hilo: %d     x: %d\n", omp_get_thread_num(), x);
    }
    printf("el valor de x es %d\n", x);
    getchar();
}
