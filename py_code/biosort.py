#/usr/bin/env python 
 
import os 
import shlex 
from create_gene import makegene
from run_generation import make_list, add_organism_log 
from culture_organism import testgene
import random
from set_environment import CreateEnvironment

 
 
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

 

def setupgen(num_organisms): 
    for i in range(1, num_organisms+1): 
        writec(howmany(10), 'habitat/test') 
 

# This will take in a class object containin the environment parameters
def Start(env):
    ops = 0
    org = ''
    while ops not in range(1, env.pressure+1):
        org = makegene(random.randint(1, env.maxgenes+1))
        org.folder = "breeder1"
        arraylist = []
        for i in range(env.runs):
            arraylist.append(make_list(env.arraysize))
        testgene(org, arraylist, env)
        add_organism_log(env, org, 0)
        ops = org.avgops

Start(CreateEnvironment()) 
