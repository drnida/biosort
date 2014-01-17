# hey look a change

import random
import os
import subprocess
import genecreate.py




#body should look as follows
#do{
#i=___; //1) 0-9 or r()
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

def writeheader(genesequence):
    header = '/*'+geneqequence+'*/\n#include "biosort.h"\nlong long Pressure = 100000000;\nlong long count=0;\nextern int * a;\nextern int i;\n'\
    'int temp[16] = {5, 9, 3, 2, 6, 1, 4, 16, 12, 8, 7, 11, 10, 13, 15, 14};\n\nlong long main()\n{\na=temp;\n'
    return header


#Writes the do while loop for the .cpp programs (organisms)
def writebody(organism, genesequence):
        writeout = writeheader(genesequence)
        tokens = translategene(genesequence)
        num = len(tokens)/17
        length = len(tok)
        counter = tok[length-1]
        del tok[-1]
	for j in range(num):
		i = j*17
		writeout += 'do{\ni='+tok[1+i]+';\nv=a[i];\nif(('+tok[2+i]+' '+tok[3+i]+' '+tok[4+i]+' '+tok[5+i]+\
		'\n'+tok[6+i]+'%S)'+tok[7+i]+'\n('+tok[8+i]+' '+tok[9+i]+' '+tok[10+i]+' '+tok[11+i]+\
		'\n'+tok[12+i]+'%S))\n{\n'+tok[13+i]+'(('+tok[14+i]+' '+tok[15+i]+' '+tok[16+i]+'\n'+\
                ')%S)}\n';
        writeout +='count +='+counter+'}while(!sorted(a[])&& count<Pressure)\nreturn count;'
        organism.write(writeout)
	return

#Creates one file
def writec(genesequence, foldernum):
        folder = '../habitat/spec'+str(foldernum)
        if not os.path.isdir(folder):
            os.makedirs(folder)
	filename = folder+'/organism.cpp'
	organism = open(filename, 'w+')
	writebody(organism, genesequence)
	organism.close()
	return

def gen_begin(num):
    output = ''
    subprocess.call('g++ -c -o ../habitat/biosort.o ../c_code/biosort.cpp')
    i = 1
    opcount = 0
    for i in range(num):
        subprocess.call('g++ ../spec'+num+'/*.cpp ../biosort.o')
        opcount = subprocess.call('./a.out')
        organism = open('../habitat/spec'+num+'/organism.cpp')
        genesequence = organism.readline()
        geneseqence = genesequence[2:-2]
        print genesequence
        print opcount
    #gen_end() to write out log file
	
	

# Returns a list of numbers 0 through X in a random order
# This is also in pythonTODO
def make_list(x):
    mylist = list(xrange(x))
    random.shuffle(mylist)
    return mylist

teststring = howmany(10)
print teststring
writec(teststring, 1)
gen_begin(1)
