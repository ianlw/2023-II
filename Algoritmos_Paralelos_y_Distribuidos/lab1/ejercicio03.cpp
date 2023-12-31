#include <iostream>
#include <thread>
#include <string>
#include <cstdlib>
// #include <windows.h>  //--para poder sleep

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
	std::thread hilo0(imprime, "tin", 10);
	std::thread hilo1(imprime, "ton", 5);

	std::cout << "termino la ejecuci�n de los hilos.." << '\n';
	
	getchar();
	return 0;
}
