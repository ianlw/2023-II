#include <iostream>
#include <thread>
using namespace std;

void escribeMensaje()
{//--función que ejecutará el hilo
	std::cout << "Hola mundo..." << '\n';
}

int main()
{
	//-- Crea y planifica el hilo para ejecutar escribeMensaje 
	std::thread hilo0(escribeMensaje);
	
	system("pause");
	return 0;
}
