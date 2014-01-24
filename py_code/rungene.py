
from writetoc import writec

def testgene(folder, genesequence, runs, arraylist):
    writec(folder, genesequence)

    opcount_counter = 0 
    total_opcount = 0 
    genesequence = '' 
    subprocess.call('g++ ' + folder + '/*.cpp habitat/biosort.o -o ' + folder + '/organism.out -g', shell = True) 
     
    # Runs an organism however many times we want 
    for i in range(organism_run_num):
        array = ' '.join(arraylist[i])
        command = folder + '/organism.out '+array
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
	 
    return ops
