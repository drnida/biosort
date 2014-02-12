import os 
import random
from shutil import copy

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
    if not os.path.exists('./logs/'):
        os.makedirs('./logs/')
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

# Takes in environment and first successful organism
def Prep_First_Generation(org, env):
    # Start our Bfolder array
    folders = []
    org.folder = "B_1"
    org.is_primeval = False
    folders.append(Bfolder("./habitat/breeder1/", env.kids, org)

    # Radomly create starting random genes
    for x in range(1, env.breeders):
        temporg = Organism(makegene(random.randint(1, env.maxgenes+1)))
        temporg.folder = "B_"+str(x+1)
        temporg.is_primeval = True
        folders.append(Bfolder("./habitat/breeder"+str(i+1)+"/", env.kids), temporg)
        writec(folders[0].location, folders[0].org.genesequence, env.pressure)
        for y in range(0, env.kids):
            temporg = Organism(makegene(random.randint(1, env.maxgenes+1))
            temporg.folder = "P_"+str(y+1)+"_B_"+str(x+1)
            temporg.is_primeval = True
            folders[x].kids[y].org = temporg
            writec(folders[x].kids[y].location, folders[x].kids[y].org.genesequence, env.pressure)

    # Spawn kids off winner
    for x in range(0, env.kids):
        try:
            copy(folders[0].location+"organism.cpp", folders[0].kids[x].location)
        except:
            print "Error copying first gen"
        temporg = Organism(org_list[0].genesequence)
        temporg.folder = "P_"+str(x+1)+"_`B_0"
        temporg.is_primeval = False
        folders[0].kids[x].org = temporg
        mutate(folders[0].kids[x].org, env.mutations+env.adds*x, env.weight, env.pressure, env.maxgenes)

def Start_Gen(folders, env):
    for x in range(env.breeders):
        

def End_Gen(folders, env):
