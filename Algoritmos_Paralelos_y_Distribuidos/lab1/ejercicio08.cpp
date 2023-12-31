#include <atomic>
#include <thread>
#include <iostream>
#include <mutex>

using namespace std;

std::atomic<int> counter(0); // contador at�mico

int counter3 = 0; // para demostrar el incremento seguro de un contador compartido
mutex mu;

void safe_increment_atomic() {
    // usa un contador at�mico

    for (int j = 0; j < 1000000; j++) {
        ++counter;
    }
}

// Uso de exclusi�n mutua
// Si no bloquea la secci�n de incremento del c�digo, habr� una carrera de datos
// para incrementar y actualizar el contador, lo que provocar� una actualizaci�n 
// falsa del contador.
void safe_increment_lock() {
    for (size_t j = 0; j < 1000000; j++) {
        
        mu.lock();
        ++counter3;
        mu.unlock();
    }
}

void thread_safe_counter() {
    // Utiliza un m�todo de incremento seguro para contar con hilos

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
