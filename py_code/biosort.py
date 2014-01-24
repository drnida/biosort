#/usr/bin/env python 
 
import os 
import shlex 
from genecreate import makegene
from rungen import make_list 
from rungene import testgene

offset = {1:0, 2:3, 3:5, 4:24, 5:28, 6:31, 7:33, 8:38, 9:40, 10:44, 11:48, 12:51, 13:53, 14:58 , 15:64, 16:68, 17:71, 18:73}
 
 
#body should look as follows 
#do{ 
#i=___ __ ___; //1) 0-9 or r() 2) maths 3) 1-9 or R() 
#v=a[i]; 
#if((__ ___ __ ___//1) ( or a[ which sets 1 on next line 2) 0-9, r(), i, or v 3) *, /, -, % or // 4) 0-9, r(), i or v 
#_ %S)__ // 1) ) or ] defined by 1 of last line 2) logical op 
#(__ ___ __ ___ //1) ( or a[ which defines 1 on the next line 2) 0-9, r(), i, or v 3) *, +, -, /, %, or // 4) 0-9, r(), i, or v 
#_ %S))//1) ) or ] defined by 1 on last line 
#{ 
#_(( ___ __ ___// 1) W, U, or D 2) 0-9, r(), i, or v 3) +, -, /, %, or // 4) 0-9, r(), i, or v 
#)%S) 
#} 
#after genes finish 
#count += ops; 
#}while(not_sorted(a[])&& count <SelectivePressure); 
 
 
#Writes the do while loop for the .cpp programs (organisms) 

#Creates one file 

 

 
# Returns a list of numbers 0 through X in a random order 
# This is also in pythonTODO 

 
def calcoffset(genesequence): 
    length = len(genesequence); 
    length = length + 5; 
    return length; 
 
def setupgen(num_organisms): 
    for i in range(1, num_organisms+1): 
        writec(howmany(10), 'habitat/test') 
 

# This will take in a class object containin the environment parameters
def Start(env):
    ops = 0
    while ops not in (1, env.pressure):
        arraylist = []
        for i in range(env.runs):
            arraylist.append(make_list(env.arraysize))
        ops = testgene("../habitat/breeder1", makegene(env.maxgenes), arraylist, env)

 

