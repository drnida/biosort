#/usr/bin/env python 
import random 
import os 
import subprocess 
import shlex 
from subprocess import Popen, PIPE 
from genecreate import howmany
from writetoc import writebody, writeheader, writec 
 
 
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

 
def gen_begin(num_organisms, organism_run_num): 
    folder = os.getcwd() 
    print folder 
    output = '' 
    subprocess.call('g++ -c -o ./habitat/biosort.o ./c_code/biosort.cpp -g', shell = True) 
     
    # Variables for the loops 
    i = 1 
    opcount = 0 
    #gen_end() to write out log file 
    j = 1 
     
    # Runs the loop however many number of organisms is specified 
    for i in range(1, num_organisms+1): 
	# Variables to track information on organism runs 
	opcount_counter = 0 
	total_opcount = 0 
	genesequence = '' 
	speclocation = 'habitat/spec'+str(i) 
        print speclocation 
	subprocess.call('g++ ' + speclocation + '/*.cpp habitat/biosort.o -o ' + speclocation + '/organism.out -g', shell = True) 
	 
	# Runs an organism however many times we want 
	for j in range(organism_run_num):
            command = speclocation + '/organism.out 3 1 2 0 4 5 6'
	    opcount = subprocess.Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True) 
	     
	    # Getting opcount and adding to total 
            firstline = True 
            for line in iter(opcount.stdout.readline, ''): 
                if firstline == True: 
	            opcount_counter = int(line) 
                    firstline = False 
                else: 
                    print line 
                     
	    total_opcount += opcount_counter 
	 
	# Calculating mean number of ops 
	mean_opcount = total_opcount / organism_run_num 
	 
        # Grabbing the gene sequence 
        organism = open(speclocation+'/organism.cpp') 
	genesequence = organism.readline() 
	genesequence = genesequence[2:-3] 
	 
	# Adding organism to log file 
	add_organism_log('./logs/', genesequence, mean_opcount) 
    #gen_end() to write out log file 
 
 
# Adds an organism's results to log file. The log file is in the current working 
# directory that was found in the "gen_begin" method. 
def add_organism_log(folder, genes, ops): 
    log_file = folder + 'log.txt' 
    log = open(log_file, 'a') 
    log.write(genes + "\t" + str(ops) + "\n") 
    log.close() 
 
 
# Returns a list of numbers 0 through X in a random order 
# This is also in pythonTODO 
def make_list(x): 
    mylist = list(xrange(x)) 
    random.shuffle(mylist) 
    return mylist 
 
 
def calcoffset(genesequence): 
    length = len(genesequence); 
    length = length + 5; 
    return length; 
 
def setupgen(num_organisms): 
    for i in range(1, num_organisms+1): 
        writec(howmany(10), 'habitat/test') 
 
 
setupgen(5) 
gen_begin(5, 5) 
