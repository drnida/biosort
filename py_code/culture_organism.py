from transcribe_c import writec
from subprocess import Popen, PIPE
import subprocess


#Imporatnt, next step is to separate this up into 2 functions
#One to set up the file and compile it
#The other to run it
#This is so that we can run a setup loop in rungen and then a test loop
#After that set up the loops in rungen and create a system to tell if they shoul be randomized or mutated from another organism
def testgene(folder, genesequence, arraylist, env):
    writec(folder, genesequence, env.pressure)

    opcount_counter = 0 
    total_opcount = 0 
    genesequence = '' 
    subprocess.call('g++ ' + folder + '/*.cpp ./habitat/biosort.o -o ' + folder + '/organism.out -g', shell = True) 
     
    # Runs an organism however many times we want 
    for i in range(env.runs):
        array = ' '.join(str(x) for x in arraylist[i])
        command = folder + '/organism.out '+array
        opcount = subprocess.Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True) 
         
        # Getting opcount and adding to total 
        firstline = True 
        for line in iter(opcount.stdout.readline, ''): 
            if firstline == True: 
                opcount_counter = int(line) 
                print "Ops: " + line
                firstline = False 
            else: 
                print line, 
        if opcount_counter > env.pressure:
            if env.penalty != -1:
                opcount_counter += env.penalty
            else:
                pass # should kill organism

        total_opcount += opcount_counter
        
     
	# Calculating mean number of ops 
	mean_opcount = total_opcount / env.runs 
	 
    return mean_opcount
