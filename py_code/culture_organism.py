from transcribe_c import writec
from subprocess import Popen, PIPE
import subprocess


#Imporatnt, next step is to separate this up into 2 functions
#One to set up the file and compile it
#The other to run it
#This is so that we can run a setup loop in rungen and then a test loop
#After that set up the loops in rungen and create a system to tell if they shoul be randomized or mutated from another organism
def testgene(org, arraylist, env):
    writec("./habitat/" +org.folder, org, env.pressure)

    opcount_counter = 0 
    total_opcount = 0  
    subprocess.call('g++ ./habitat/' + org.folder + '/*.cpp ./habitat/biosort.o -o ./habitat/' + org.folder + 'organism.out -g', shell = True) 
     
    # Runs an organism however many times we want 
    for i in range(env.runs):
        array = ' '.join(str(x) for x in arraylist[i])
        command = './habitat/' + org.folder + 'organism.out '+array
        opcount = subprocess.Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True) 
      
        # Getting opcount and adding to total 
        firstline = True
        for line in iter(opcount.stdout.readline, ''): 
            if firstline == True: 
                org.ops.append(int(line)) 
                print "Ops: " + line
                firstline = False 
            else: 
                print line 
        if org.ops[i] >= env.pressure:
            if env.penalty != -1:
                org.ops[i] += env.penalty
            else:
                pass # should kill organism

        total_opcount += org.ops[i]
        
     
	# Calculating mean number of ops 
	org.avgops = total_opcount / env.runs 
	 
    return
