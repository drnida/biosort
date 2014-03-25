#include "biosort.h"

int v = 0; //Value at the array index being considered
extern int count; //Current total opcount of this program
int s; //Size of the array to be sorted
extern int * a; //The array to be sorted
int i = 0; //The current index of the array being considered
extern int Pressure;

//Swaps a[i] with a[to_index]
//Please adjust count if you edit this function.
void w(int to_index)
{
	int temp = a[to_index];
	a[to_index] = a[i];
	a[i] = temp;

	count += 3; //3 assignments
}

//Moves a[i] to a[to_index] and shifts up as needed.
//Please adjust count if you edit this function.
void u(int to_index)
{
    if(i == to_index)
    {
        ++count; //1 comparison
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
            count += 3; //2 assignments, 1 math
        }
	    else
	    {
            if(j == 0)
                a[j++] = a[j + 1];
            else
                a[j - 1] = a[j++];
            count += 4; //1 assignment, 1 increment, 1 compare, 1 math
        }
        count += 3; //2 compares, 1 math
    }

    if(j > s - 1)
    {
        a[s - 1] = a[0];
        j = 0;
        count += 3; //2 assignment, 1 math
    }
    else
    {
        if(j == 0)
            a[j++] = a[j + 1];
        else
            a[j - 1] = a[j++];
        count += 4; //1 assignment, 1 increment, 1 compare, 1 math
    }
    a[to_index] = temp;

    count += 8; //3 assignments, 3 compares, 1 increment, 1 math
}

//Moves a[i] to a[to_index] and shifts down as needed.
//Please adjust count if you edit this function.
void d(int to_index)
{
    if(i == to_index)
    {
        ++count; //1 compare
        return;
    }

    int j = i;
    int temp = a[j--];
	
    while(j != to_index)
    {
        if(j < 0)
        {
            a[0] = a[s - 1];
            j = s - 1;
            count += 4; //2 assignments, 2 math
        }
	    else
	    {
            if(j == s - 1)
                a[j--] = a[j - 1];
            else
                a[j + 1] = a[j--];
            count += 5; //1 assignment, 1 decrement, 1 compare, 2 math
        }
        count += 2; //2 compares
    }

    if(j < 0)
    {
        a[0] = a[s - 1];
        j = s - 1;
        count += 4; //2 assignments, 2 math
    }
    else
    {
        if(j == s - 1)
            a[j--] = a[j - 1];
        else
            a[j + 1] = a[j--];
        count += 5; //1 assignment, 1 decrement, 2 math, 1 compare
    }

    a[to_index] = temp;

    count += 7; //3, assignments, 3 compares, 1 decrement
}

//Array safe mod function.  Always returns positive.
//Please adjust count if you edit this function.
int m(int input)
{
    input %= s;
    if(input < 0)
    {
        input += s;
        ++count; //1 math+assignment
    }
    count += 2; //1 math+assignment, 1 compare
    return input;
}

//Returns random number safely modded by array size.
//Please adjust count if you edit this function.
int r()
{
    return m(xor_shift());
}

//Returns random, non-zero number safely modded by array size.
//Please adjust count if you edit this function.
int R()
{
    int temp;
    do
    {
        count += 2; //1 assignment, 1 compare
        temp = m(xor_shift());
    } while (!temp);
    return temp;
}

//Generates one of 2^32 - 1 random numbers.
//Please adjust count if you edit this function.
int xor_shift()
{
    //XOR shift information:
    //"Xorshift RNGs"
    //Dr. George Marsaglia
    //The Florida State University

    count += 6; //3 shifts, 3 xor+assignments
    static unsigned long y = 1234567890; //Only happens once, not counted
    y ^= (y << 9);
    y ^= (y >> 5);
    return (y ^= (y << 1));
}

//Tests if the array is sorted.
//Exits when first unsorted element is encountered.
//Please adjust count if you edit this function.
bool is_sorted()
{
	int index = 0;
	
	while(a[index] == index && ++index != s - 1) 
		count += 5; //1 assignment, 3 compares, 1 math
	count += 2; //1 compare, 1 math (below)
	if(index < s - 1)		
		return false;
	return true;
}

//Build the random array from command line args
//Count does not need to be changed in this function
void build(char** argv)
{
    Pressure = atoi(argv[1]);
    for(int i = 0; i < s; ++i)
    {
        a[i] = atoi(argv[i + 2]);
