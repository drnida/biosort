from transcribe_c import writec
from subprocess import Popen, PIPE, call

def testgene(org, arraylist, env):
    #Creates organism.cpp file and compiles it
    writec("./habitat/" +org.folder, org, env.pressure)
    call('g++ ./habitat/' + org.folder + '*.cpp ./habitat/biosort.o -o ./habitat/' + org.folder + 'organism.out -g', shell = True) 
    

    total_opcount = 0 #Sum of all individual opcounts   
    #Runs an organism x times where x is the number of runs per generation
    for i in range(env.runs):
        array = ' '.join(str(x) for x in arraylist[i]) #Pulls array to sort from the given arraylist.
        command = './habitat/' + org.folder + 'organism.out '+str(env.pressure)+' '+array #Command to run organism on array from the command line
        fileout = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True) #Retrieves the operations performed by the C++ before it ended 
      
        # Gets opcount and adds to total_opcount 
        ops = fileout.stdout.readline() 
        org.ops.append(int(ops)) 
      
        if org.ops[i] >= env.pressure:
            org.ops[i] += env.penalty

        total_opcount += org.ops[i]
        
     
    # Calculates mean number of ops 
    org.avgops = total_opcount / env.runs 
    return
