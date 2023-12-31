#include<iostream>
#include<vector>
#include<thread>

using namespace std;

void f(std::vector<int> v);

int main()
{
	//int s1;
	std::vector<int> pares = { 10, 20, 40, 60, 80 };
	std::vector<int> impares = { 1, 3, 5, 7, 9 };

	/* Lanza dos threads t0 y t1 */
	std::thread t0(f, pares);
	std::thread t1(f, impares);

	/* Espera que finalicen */
	t0.join();
	t1.join();

	system("pause");
}
void f(std::vector<int> v)
{
	for (std::vector<int>::iterator it = v.begin();	it != v.end(); ++it)
	{
		std::cout << *it << std::endl;
	}
}
