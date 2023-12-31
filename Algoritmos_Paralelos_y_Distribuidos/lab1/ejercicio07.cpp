
#include <thread>
#include <cassert>
#include <iostream>

using namespace std;

int counter2 = 0; // para demostrar el error cuando a esta variable 
                  //se accede por mas de un hilo

void unsafe_increment() {
    // No se utiliza contadores atómicos ni exclusión mutua
    // El valor de contador2 podría cambiarse desde múltiples subprocesos, 
    // lo que provocaría una carrera de datos y un incremento inseguro.

    for (size_t j = 0; j < 1000000; j++) {
        ++counter2;
    }
}

void thread_unsafe_counter() {
    // Utiliza un método de incremento inseguro de subprocesos para contar

    std::thread t1(unsafe_increment);
    std::thread t2(unsafe_increment);
    t1.join();
    t2.join();
    assert(counter2 <= 2 * 1000000);
    cout << "Contador inseguro:\t" << counter2 << "\tValor objetivo: 2000000" << endl;
}

int main() {
    thread_unsafe_counter();
    system("pause");
    return 0;
}
