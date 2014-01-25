#include <cstdlib>

extern int s; //The size of the array

//Proves a random, non-zero number modded by s
int R();

//Proves a random number modded by s
int r();

//Safely mods a number (output always positive)
int m(int);

//Swaps current a[i] with a [to_index]
void w(int to_index);

//Moves a[i] to a[to_index], shifts up if needed
void u(int to_index);

//Moves a[i] to a[to_index], shifts down if needed
void d(int to_index);

//Tests whether array is sorted
bool is_sorted();

//Constructs array from command line args
void build(char**);

//Provides random int
int xor_shift();
