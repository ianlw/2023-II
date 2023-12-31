#include <thread>
#include <iostream>

using namespace std;


void compute_factorial(int number) {
    long long result = 1;
    for (size_t i = 2; i <= number; i++) 
        result *= i;

   std::cout << "Factorial de " << number << " : " << result << std::endl;
   
}

int main() {
    int num1 = 5;
    int num2 = 6;

    // Calcular factorial de dos números simultáneamente.
    thread t1(compute_factorial, num1);
    thread t2(compute_factorial, num2);

    t1.join();
    t2.join();
    system("pause");
    return 0;
}
