#include "biosort.h"
#include <iostream>

using namespace std;

int count = 0;
extern int * a;
extern int i;
extern int count;
int temp[10] = { 5, 9, 1, 3, 2, 8, 6, 4, 0, 7};

int main()
{
	a = temp;

	do
	{
	    r();
	    r();
	    r();
		i = r();
		w(r());

		i = r();
		u(r());

		i = r();
		d(r());
	
		count += 3;
	}while(!is_sorted);

	cout << endl << "ops: " << count << endl;

	return 0;
}
