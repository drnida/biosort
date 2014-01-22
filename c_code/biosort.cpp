#include "biosort.h"

int v;
extern int count;
int * a;
int i;
static int random_index = 0;
static int random_num[512] = {
8, 4, 2, 2, 0, 7, 6, 4, 8, 0, 2, 5, 6, 5, 6, 5, 0, 1, 8, 6, 
1, 8, 7, 4, 3, 4, 5, 7, 9, 1, 9, 9, 5, 3, 2, 8, 1, 0, 2, 1, 
2, 6, 8, 8, 2, 5, 5, 4, 6, 5, 0, 7, 5, 0, 1, 9, 6, 8, 8, 8, 
0, 9, 7, 7, 3, 1, 5, 4, 1, 0, 7, 4, 6, 5, 4, 0, 0, 0, 4, 8, 
7, 7, 8, 3, 9, 1, 4, 5, 0, 2, 3, 0, 2, 3, 7, 5, 4, 5, 1, 6, 
5, 8, 2, 1, 5, 6, 4, 8, 6, 8, 6, 6, 5, 6, 9, 6, 8, 3, 2, 8, 
5, 7, 8, 9, 0, 7, 4, 7, 2, 7, 3, 7, 7, 5, 1, 3, 3, 5, 3, 2, 
5, 1, 8, 3, 8, 7, 9, 6, 2, 3, 4, 9, 1, 4, 9, 3, 1, 5, 2, 4, 
5, 5, 3, 2, 2, 4, 5, 8, 1, 8, 0, 7, 2, 8, 2, 0, 7, 1, 6, 9, 
7, 0, 0, 8, 4, 9, 3, 7, 7, 6, 1, 2, 3, 7, 4, 8, 1, 2, 6, 5, 
2, 8, 4, 4, 6, 6, 4, 5, 7, 2, 4, 4, 2, 6, 4, 8, 8, 0, 8, 5, 
8, 1, 9, 3, 8, 5, 3, 2, 9, 9, 7, 2, 9, 1, 8, 5, 7, 5, 0, 6, 
7, 6, 3, 2, 3, 7, 2, 1, 9, 0, 8, 7, 2, 7, 3, 2, 2, 6, 4, 2, 
8, 1, 6, 7, 4, 6, 3, 1, 3, 5, 0, 1, 4, 3, 5, 7, 2, 7, 0, 2, 
0, 8, 1, 4, 5, 4, 8, 9, 1, 3, 3, 9, 6, 1, 6, 1, 8, 1, 4, 1, 
9, 6, 4, 3, 9, 9, 0, 2, 9, 0, 4, 1, 0, 7, 7, 7, 2, 5, 8, 5, 
8, 2, 4, 7, 3, 2, 0, 3, 6, 6, 7, 5, 3, 1, 8, 2, 3, 0, 6, 4, 
2, 0, 7, 4, 8, 4, 1, 2, 9, 9, 7, 0, 3, 3, 9, 7, 7, 9, 2, 3, 
5, 9, 0, 0, 3, 0, 5, 8, 2, 1, 2, 4, 4, 9, 8, 4, 3, 1, 6, 4, 
1, 5, 6, 4, 8, 5, 3, 7, 4, 8, 3, 2, 7, 3, 4, 2, 4, 9, 0, 8, 
1, 2, 3, 5, 3, 3, 9, 8, 5, 5, 3, 8, 2, 1, 4, 0, 7, 8, 9, 3, 
6, 2, 5, 5, 6, 0, 0, 2, 1, 0, 0, 2, 5, 5, 7, 0, 1, 8, 9, 6, 
5, 4, 6, 7, 5, 0, 9, 2, 0, 9, 6, 8, 1, 3, 4, 7, 5, 6, 1, 7, 
6, 4, 9, 3, 9, 9, 4, 0, 7, 3, 8, 5, 9, 6, 2, 4, 7, 4, 7, 7, 
3, 5, 6, 4, 8, 2, 4, 4, 8, 7, 3, 6, 1, 2, 2, 3, 3, 6, 5, 3, 
1, 6, 8, 0, 2, 2, 4, 9, 6, 3, 9, 9};



void w(int to_index)
{
	int temp = a[to_index];
	a[to_index] = a[i];
	a[i] = temp;

	count += 3;
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
        if(j > s - 1)
        {
            a[s - 1] = a[0];
            j = 0;
            count += 3;
        }
	    else
	    {
            a[j - 1] = a[j++];
            count += 3;
        }
        count += 2;
    }

    if(j > s - 1)
    {
        a[s - 1] = a[0];
        j = 0;
        count += 3;
    }
	else
	{
        a[j - 1] = a[j++];
        count += 3; 
    }
    a[to_index] = temp;

    count += 5;
}

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
        if(j < 0)
        {
            a[0] = a[s-1];
            j = s - 1;
            count += 3;
        }
	    else
	    {
            a[j + 1] = a[j--];
            count += 3;
        }
    }

    if(j < 0)
    {
        a[0] = a[s-1];
        j = s - 1;
        count += 3;
    }
	else
	{
        a[j + 1] = a[j--];
        count += 3;
    }

    a[to_index] = temp;

    count += 5;
}

int m(int input)
{
    input %= s;
    if(input < 0)
        input += s;
    return input;
}


int r()
{
	count += 2;
	if(random_index == 511)
	{
		random_index = 0;
		++count;
	}
	return random_num[random_index++];
}

int R()
{
    int r_num;
    do
    {
    	count += 2;
	    if(random_index == 511)
    	{
	    	random_index = 0;
		    ++count;
    	}
    	r_num = random_num[random_index++];
    }while(!r_num);
	return r_num;
}

bool is_sorted()
{
	int index = 0;
	
	while(a[index] == index && ++index != s - 1) 
		count += 2;
	if(index < s - 1)		
		return false;
	return true;
}
