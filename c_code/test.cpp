#include <iostream>

using namespace std;

int r();

int main()
{
    int even = 0;
    int odd = 0;
    int num;

    for(int i = 0; i < 10000000; ++i)
    {
        num = r();
        cout << endl << num;
        if(num % 2)
            ++even;
        else
            ++odd;
    }

    cout << endl << "even: " << even;
    cout << endl << "odd: " << odd;

	return 0;
}

int r()
{
    static unsigned long y = 1234567890;
    y ^= (y << 9);
    y ^= (y >> 5);
    return (y ^= (y << 1));
}
