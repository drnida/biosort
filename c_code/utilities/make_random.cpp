#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

int main()
{
	srand(time(NULL));
	cout << endl;
	for(int i = 0; i < 512; ++i)
	{
		if(!(i % 20))
			cout << endl;
		cout << rand() % 10 << ", ";
	}
}
