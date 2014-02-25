import os 
import random
from shutil import copy
import folder
from subprocess import Popen, PIPE

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
        temporg = Organism(makegene(random.randint(1, env.maxgenes+1))) # Make a random gene
        temporg.folder = folders[x].path # set org folder (needed for mutate)
        temporg.logloc = "B_"+str(x+1) # set log output for location
        temporg.is_primeval = True # Came from random, so its primeval
        folders.append(Bfolder("./habitat/breeder"+str(i+1)+"/", env.kids), temporg) # add the folder to the list
        writec(folders[0].location, folders[0].org.genesequence, env.pressure) # write out the file
        for y in range(0, env.kids): # starat spawning kids
            temporg = Organism(makegene(random.randint(1, env.maxgenes+1)) # make a random gene
            temporg.folder = folders[x].progeny[y].path # set org folder (created in init of bfolder)
            temporg.logloc = "P_"+str(y+1)+"_B_"+str(x+1) # set log output for location
            temporg.is_primeval = True # came from random, so its primeval
            folders[x].progeny[y].org = temporg # add the org to the folder
            writec(folders[x].progeny[y].location, folders[x].progeny[y].org.genesequence, env.pressure) # write out the file

    # Spawn kids off winner
    for x in range(0, env.kids):
        try:
            copy(folders[0].location+"organism.cpp", folders[0].progeny[x].path) # copy the gene from its parent to the kid
        except:
            print "Error copying first gen"
        temporg = Organism(org_list[0].genesequence) # create a new organism based off parent
        temporg.folder = folders[0].progeny[x].path # set organism folder
        temporg.logloc = "P_"+str(x+1)+"_`B_0" # set log file representation of folder
        temporg.is_primeval = False # Did not come from random, not primeval
        folders[0].kids[x].org = temporg # place org in folder
        mutate(folders[0].kids[x].org, env.mutations+env.adds*x, env.weight, env.pressure, env.maxgenes) # mutate the gene and write mutation to file
    
    return folders

def Run_Gen(folders, env):
    arraylist = []
    for run in range(env.runs):
        arraylist.append(make_list(env.arraysize))
        array = ' '.join(str(arraylist[run]))
        labtable = [None for x in range(env.breeders*env.kids)]
        for bnum in range(env.breeders):
            command = "./habitat/"+folders[bnum]+"organism.out "+array
            labtable[bnum] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True))
            for pnum in range(env.kids):
                command = "/habitat/"+folders[bnum].progeny[pnum]+"organism.out "+array
                labtable[env.breeders+env.kids*(bnum-1)+(pnum-1)] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True))
    
        for i in range(env.breeders+env.breeders*env.kids):
            firstline = True
            for line in iter(labtable[i].stdout.readline, ''):
                if firstline == True:
                    if i in range(env.breeders):
                        folders[i].org.ops.append(int(line))
                    else:
                        bnum = ((i-env.breeders)//env.kids)+1
                        folders[bnum].progeny[i-env.breeders-(bnum*env.kids)+1.org.ops.append(int(line))
                    firstline = False

    # Time to sum the ops for the gen
    for bnum in range(env.breeders):
        count_ops(folders[bnum].org, env)
        for pnum in range(env.kids):
            count_ops(folders[bnum].progeny[pnum].org, env)


def count_ops(org, env):
    total_opcount = 0
    for run in range(env.runs):
        total_opcount += org.ops[i]
    org.avgops = total_opcount/env.runs
            

def Log_Gen(folders, env):

def Setup_Gen(folders, env):
   #Sort by avg ops
   #Set new pressure
   #Put orgs in correct folders for breeders
   #Spawn kids
