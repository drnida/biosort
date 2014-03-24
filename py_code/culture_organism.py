from transcribe_c import writec
from subprocess import Popen, PIPE
import subprocess


#Imporatnt, next step is to separate this up into 2 functions
#One to set up the file and compile it
#The other to run it
#This is so that we can run a setup loop in rungen and then a test loop
#After that set up the loops in rungen and create a system to tell if they shoul be randomized or mutated from another organism










def testgene(org, arraylist, env):
    #Creates organism.cpp file and compiles it
    writec("./habitat/" +org.folder, org, env.pressure)
    subprocess.call('g++ ./habitat/' + org.folder + '*.cpp ./habitat/biosort.o -o ./habitat/' + org.folder + 'organism.out -g', shell = True) 
    

    total_opcount = 0 #Sum of all individual opcounts   
    #Runs an organism x times where x is the number of runs per generation
    for i in range(env.runs):
        array = ' '.join(str(x) for x in arraylist[i]) #Pulls array to sort from the given arraylist.
        command = './habitat/' + org.folder + 'organism.out '+array #Command to run organism on array from the command line
        fileout = subprocess.Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True) #Retrieves the operations performed by the C++ before it ended 
      
        # Gets opcount and adding to total_opcount 
        ops = fileout.stdout.readline() 
        org.ops.append(int(ops)) 
      
        if org.ops[i] >= env.pressure:
            org.ops[i] += env.penalty

        total_opcount += org.ops[i]
        
     
    # Calculating mean number of ops 
    org.avgops = total_opcount / env.runs 
    print "Ops: " + str(org.avgops)
    return
