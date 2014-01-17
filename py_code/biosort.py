#/usr/bin/env python
import random
import os
import subprocess
from subprocess import Popen, PIPE
from genecreate import howmany, translategene, roll4d6 




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
    header = '/*'+genesequence+'*/\n#include <iostream>\nusing namespace std;\n#include "../biosort.h"\nlong long Pressure = 10000000;\nextern int v;\nint count=0;\nextern int * a;\nextern int i;\n'\
    'int temp[10] = {5, 9, 3, 2, 6, 1, 4, 8, 7, 0};\n\nint main()\n{\na=temp;\n'
    return header


#Writes the do while loop for the .cpp programs (organisms)
def writebody(organism, genesequence):
        writeout = writeheader(genesequence)
        writeout += 'do{'
        tok = translategene(genesequence)
        num = len(tok)/17
        length = len(tok)
        counter = tok[length-1]
        del tok[-1]
	for j in range(num):
		i = j*17
		writeout += '\ni='+tok[1+i]+';\nv=a[i];\nif(('+tok[2+i]+' '+tok[3+i]+' '+tok[4+i]+' '+tok[5+i]+\
		'\n'+'%s'+tok[6+i]+')'+tok[7+i]+'\n('+tok[8+i]+' '+tok[9+i]+' '+tok[10+i]+' '+tok[11+i]+\
		'\n'+'%s'tok[12+i]+'))\n{\n'+tok[13+i]+'(('+tok[14+i]+' '+tok[15+i]+' '+tok[16+i]+'\n'+\
                ')%s);}\n';
        writeout +='count +='+counter+';}while(!is_sorted()&& count<Pressure);\ncout << count; \nfor(int j = 0; j < 10; j++){cout << a[i];}\nreturn 0;}'
        organism.write(writeout)
	return

#Creates one file
def writec(genesequence, foldernum):
        folder = 'habitat/spec'+str(foldernum)
        if not os.path.isdir(folder):
            os.makedirs(folder)
	filename = folder+'/organism.cpp'
	organism = open(filename, 'w+')
	writebody(organism, genesequence)
	organism.close()
	return

def gen_begin(num):
    folder = os.getcwd()
    print folder
    output = ''
    subprocess.call('g++ -c -o ./habitat/biosort.o ./c_code/biosort.cpp -g', shell = True)
    i = 1
    opcount = 0
    for i in range(num):
        speclocation = 'habitat/spec'+str(num)
        subprocess.call('g++ '+speclocation+'/*.cpp habitat/biosort.o -o '+speclocation+'/organism.out -g', shell = True)
        opcount = subprocess.Popen(speclocation+'/organism.out',stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1)
        organism = open(speclocation+'/organism.cpp')
        genesequence = organism.readline()
        genesequence = genesequence[2:-3]
        print genesequence
        print opcount.stdout.read()
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
