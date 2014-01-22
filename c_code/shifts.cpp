#include <iostream>

using namespace std;

const int s = 5;
int a[5] = {0, 1, 2, 3, 4};
int i;
int count = 0;

void u(int);
void d(int);
void display();

int main()
{
    int to_index;
    cout << "\nEnter source index: ";
    cin >> i;
    cout << "\nEnter destination index: ";
    cin >> to_index;

    cout << "\nOriginal array: ";
    display();

    u(to_index);

    cout << "\nResulting array: ";
    display();
}

void display()
{
    cout << "{";
    for(int j = 0; j < s; ++j)
    {
        cout << " " << a[j];
        if(j == s - 1)
            cout << "}\n";
        else
            cout << ",";
    }
}
/*
void u(int to_index)
{
	int temp = a[to_index];
	a[to_index] = a[i];
	int j = i;

    cout << "Steps:\n";

	while(j != to_index)
	{
	    display(); //DISPLAY
		if(j == 0)
		{
			a[j] = a[s - 1];
			j = s - 1;
			count += 4;
		}
		else
		{
	        a[j--] = a[j - 1];
	        count += 5;
        }
    }
    display(); //DISPLAY
	a[j + 1] = temp;
	count += 5;
	display(); //DISPLAY
}
*/
void d(int to_index)
{
    if(i == to_index)
    {
        ++count;
        return;
    }

    int j = i;
	int temp = a[j--];
	
	while(j != to_index)
	{
	    display(); //DISPLAY
        if(j < 0)
        {
            a[0] = a[s-1];
            j = s - 1;
        }
	    else
            a[j + 1] = a[j--];
    }

    display(); //DISPLAY
    if(j < 0)
    {
        a[0] = a[s-1];
        j = s - 1;
    }
	else
        a[j + 1] = a[j--];
    display(); //DISPLAY
    a[to_index] = temp;
    display(); //DISPLAY



/*	while(j != to_index)
	{
        display(); //DISPLAY
		if(j == s - 1)
		{
			a[j] = a[0];
			j = 0;
			count += 4;
		}
		else
		{
		    a[j++] = a[j + 1];
	        count += 5;
        }
    }
*/
    count += 5;
}

void u(int to_index)
{
    if(i == to_index)
    {
        ++count;
        return;
    }

    int j = i;
	int temp = a[j++];
	
	while(j != to_index)
	{
	    display(); //DISPLAY
        if(j > s - 1)
        {
            a[s - 1] = a[0];
            j = 0;
        }
	    else
            a[j - 1] = a[j++];
    }

    display(); //DISPLAY
    if(j > s - 1)
    {
        a[s - 1] = a[0];
        j = 0;
    }
	else
        a[j - 1] = a[j++];
    display(); //DISPLAY
    a[to_index] = temp;
    display(); //DISPLAY

    count += 5;
}

