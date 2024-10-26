#include <iostream>
#include <thread>
#include <string>
#include <cstdlib>
// #include <windows.h>  //--para poder usar sleep
#include <unistd.h>  //--para poder usar sleep

using namespace std;

void imprime(string palabra, long tiempo)
{
	for (int i = 1; i <= 100; i++)
	{
		std::cout << palabra << '\n';
		sleep(tiempo); //--duerme en milisegundos
	}
}

int main()
{
	// Crea y ejecuta hilo0 e hilo1
	std::thread hilo0(imprime, "tin", 1);
	std::thread hilo1(imprime, "ton", 0.8);

	hilo0.join();
	hilo1.join();

	std::cout << "termino la ejecución de los hilos.." << '\n';
	getchar();
	return 0;
}
