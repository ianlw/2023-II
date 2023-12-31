#include <atomic>
#include <thread>
#include <iostream>
#include <mutex>

using namespace std;

std::atomic<int> counter(0); // contador atómico

int counter3 = 0; // para demostrar el incremento seguro de un contador compartido
mutex mu;

void safe_increment_atomic() {
    // usa un contador atómico

    for (int j = 0; j < 1000000; j++) {
        ++counter;
    }
}

// Uso de exclusión mutua
// Si no bloquea la sección de incremento del código, habrá una carrera de datos
// para incrementar y actualizar el contador, lo que provocará una actualización 
// falsa del contador.
void safe_increment_lock() {
    for (size_t j = 0; j < 1000000; j++) {
        
        mu.lock();
        ++counter3;
        mu.unlock();
    }
}

void thread_safe_counter() {
    // Utiliza un método de incremento seguro para contar con hilos

    // using safe_increment_lock will also work
    std::thread t1(safe_increment_atomic);
    std::thread t2(safe_increment_atomic);
    t1.join();
    t2.join();
    cout << "Contador seguro:\t" << counter << "\tValor objetivo: 2000000" << endl;
}


int main() {
    thread_safe_counter();
    // system("pause");
    return 0;
}
