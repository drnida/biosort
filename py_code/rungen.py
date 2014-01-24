import subprocess 

def make_list(x): 
    mylist = list(xrange(x)) 
    random.shuffle(mylist) 
    return mylist 
 


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



def setupgen(env): 
    for i in range(1, num_organisms+1): 
        writec(howmany(10), i) 
