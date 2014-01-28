import os 
import random

def make_list(x): 
    mylist = list(xrange(x)) 
    random.shuffle(mylist) 
    return mylist 
 


def gen_begin(env, generation):  
    output = '' 
     
    # Variable for the loop 
    i = 1 
    opcount = 0 
    #gen_end() to write out log file 
     
    # Runs the loop however many number of organisms is specified 
    #for i in range(1, env.breeders+1): 
	#testgene("./habitat/breeder"+i, 
	
    # Grabbing the gene sequence 
    #organism = open(speclocation+'/organism.cpp') 
	#genesequence = organism.readline() 
	#genesequence = genesequence[2:-3] 
	 
	# Adding organism to log file 
	#add_organism_log(env, genesequence, mean_opcount, generation) 
    #gen_end() to write out log file 
 
 
# Adds an organism's results to log file. The log file is in the current working 
# directory that was found in the "gen_begin" method. 
def add_organism_log(env, org, generation): 
    log_file = './logs/log.txt' 
    log = open(log_file, 'a')
    logout = "G" + str(generation) + '\t'
    if org.avgops > env.pressure:
        logout += 'F' + '\t' 
    else:
        logout += 'S' + '\t'
    
    logout += str(org.avgops) + '\t'\
    + org.folder + '\t'\
    + org.genesequence + '\n' 
    
    log.write(logout)
        
    log.close() 



def setupgen(env): 
    for i in range(1, num_organisms+1): 
        writec(howmany(10), i) 
