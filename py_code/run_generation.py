import os 
import random
import set_environment
from mutate_organism import mutate
from transcribe_c import writec
from create_gene import makegene
from organism import Organism
from shutil import copy
from folder import bfolder, pfolder, rfolder
from subprocess import Popen, PIPE, call

def make_list(x): 
    mylist = list(xrange(x)) 
    random.shuffle(mylist) 
    return mylist 
 
# Adds an organism's results to log file. The log file is in the current working 
# directory that was found in the "gen_begin" method. 
def add_organism_log(env, org): 
    logout = "G" + str(env.gennumber) + ','

    if org.avgops >= env.pressure:
        logout += 'F' + ',' 
    else:
        logout += 'S' + ','
    
    logout += str(org.avgops) + ','\
    + str(org.lineage_id) + ','\
    + org.logloc + ','\
    + org.genesequence 
   
    return logout

#def setupgen(env): 
#    for i in range(1, num_organisms+1): 
   #     writec(howmany(10), i) 
  #  log.write(logout)
 #       
#    log.close() 

#def setupgen(env): 
#    for i in range(1, num_organisms+1): 
#        writec(howmany(10), i) 

# Takes in environment and first successful organism
def Prep_First_Generation(org, env):
    # Start our Bfolder array
    folders = []
    rfolders = []
    org.logloc = "B_1"
    org.folder = "./habitat/breeder1/"
    org.is_primeval = False
    folders.append(bfolder("./habitat/breeder1/", env.kids, org))
    call('cp ./habitat/biosort.h ./habitat/breeder1/biosort.h', shell=True)

    for rand in range(env.rands):
        rfolders.append(rfolder("./habitat/random"+str(rand+1)+"/"))
        temporg = makegene(random.randint(1, env.maxgenes+1))
        temporg.folder = rfolders[rand].path
        temporg.logloc = "R_"+str(rand+1)
        temporg.is_primeval = True
        rfolders[rand].org = temporg
        writec(rfolders[rand].path, rfolders[rand].org, env.pressure)
        call('g++ '+rfolders[rand].path+'*.cpp ./habitat/biosort.o -o '+rfolders[rand].path+'organism.out -g', shell = True)

    # Radomly create starting random genes
    for x in range(1, env.breeders):
        temporg = makegene(random.randint(1, env.maxgenes+1)) # Make a random gene
        temporg.is_primeval = True # Came from random, so its primeval
        folders.append(bfolder("./habitat/breeder"+str(x+1)+"/", env.kids, temporg)) # add the folder to the list
        temporg.folder = folders[x].path # set org folder (needed for mutate)
        temporg.logloc = "B_"+str(x+1) # set log output for location
        writec(folders[x].path, folders[x].org, env.pressure) # write out the file
        call('g++ '+ folders[x].path + '*.cpp ./habitat/biosort.o -o ' + folders[x].path + 'organism.out -g', shell = True)
        call('cp ./habitat/biosort.h ./habitat/breeder'+str(x+1)+'/', shell=True) 
 
        for y in range(0, env.kids): # starat spawning kids
            temporg = makegene(random.randint(1, env.maxgenes+1)) # make a random gene
            temporg.folder = folders[x].progeny[y].path # set org folder (created in init of bfolder)
            temporg.logloc = "P_"+str(y+1)+"_B_"+str(x+1) # set log output for location
            temporg.is_primeval = True # came from random, so its primeval
            folders[x].progeny[y].org = temporg # add the org to the folder
            writec(folders[x].progeny[y].path, folders[x].progeny[y].org, env.pressure) # write out the file
            call('g++ '+ folders[x].progeny[y].path + '*.cpp ./habitat/biosort.o -o ' + folders[x].progeny[y].path + 'organism.out -g', shell = True) 

    # Spawn kids off winner
    for x in range(0, env.kids):
        try:
            call("cp " +folders[0].path+"organism.cpp "+ folders[0].progeny[x].path, shell=True) # copy the gene from its parent to the kid
        except:
            print "Error copying first gen"
        temporg = Organism(folders[0].org.genesequence) # create a new organism based off parent
        temporg.folder = folders[0].progeny[x].path # set organism folder
        temporg.logloc = "P_"+str(x+1)+"_B_1" # set log file representation of folder
        temporg.lineage_id = 1
        temporg.is_primeval = False # Did not come from random, not primeval
        folders[0].progeny[x].org = temporg # place org in folder
        mutate(folders[0].progeny[x].org, env.mutations+env.adds*x, env.weight, env.pressure, env.maxgenes) # mutate the gene and write mutation to file
        call('g++ '+ folders[0].progeny[x].path + '*.cpp ./habitat/biosort.o -o ' + folders[0].progeny[x].path + 'organism.out -g', shell = True) 
    
    foldlist = []
    foldlist.append(folders)
    foldlist.append(rfolders)
    return foldlist

def Run_Gen(folders, rfolders, env):
    arraylist = []
    for run in range(env.runs):
        arraylist.append(make_list(env.arraysize))
        array = ' '.join(str(x) for x in arraylist[run])
        labtable = [None for x in range(env.breeders+env.breeders*env.kids+env.rands)]
        
        for rand in range(env.rands):
            #call("g++ "+rfolders[rand].path+"*.cpp ./habitat/biosort.o -o "+rfolders[rand].path+"organism.out -g", shell = True)
            command = rfolders[rand].path+"organism.out "+array
            labtable[env.breeders+env.breeders*env.kids+rand] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True)

        for bnum in range(env.breeders):
            #call("g++ "+folders[bnum].path+"*.cpp ./habitat/biosort.o -o "+folders[bnum].path+"organism.out -g", shell = True) 
            command = folders[bnum].path+"organism.out "+array
            labtable[bnum] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True)
            for pnum in range(env.kids):
                #call("g++ "+folders[bnum].progeny[pnum].path+"*.cpp ./habitat/biosort.o -o "+folders[bnum].progeny[pnum].path+"organism.out -g", shell = True) 
                command = folders[bnum].progeny[pnum].path+"organism.out "+array
                #                               bnum-1  pnum-1
                labtable[env.breeders+env.kids*(bnum)+(pnum)] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True)



        for subject in range(env.breeders+(env.breeders*env.kids)+env.rands):
            firstline = True
            for line in iter(labtable[subject].stdout.readline, ''):
                if firstline == True:
                    if subject in range(env.breeders):
                        #print "Ops: "+str(line)
                        folders[subject].org.ops.append(int(line))
                    elif subject in range(env.breeders+env.breeders*env.kids):
                        #print "Ops: "+str(line)
                        bnum = ((subject-env.breeders)//env.kids)
                        folders[bnum].progeny[subject-env.breeders-(bnum*env.kids)].org.ops.append(int(line))
                    elif subject in range(10, 13):
                        rand = subject-(env.breeders+env.breeders*env.kids)
                        rfolders[rand].org.ops.append(int(line))
                    firstline = False
   # Time to sum the ops for the gen
    for rand in range(env.rands):
        count_ops(rfolders[rand].org, env)

    for bnum in range(env.breeders):
        count_ops(folders[bnum].org, env)
        for pnum in range(env.kids):
            count_ops(folders[bnum].progeny[pnum].org, env)

    return arraylist


def count_ops(org, env):
    total_opcount = 0
    #print org.ops
    for run in range(env.runs):
        total_opcount += org.ops[run]
    org.avgops = total_opcount/env.runs
    org.ops = []
            

def Log_Gen(folders, rfolders, arrays, env):
    for elem in folders:
        print elem.path
        print elem.org.logloc
        for subelem in elem.progeny:
            print subelem.path
            print subelem.org.logloc
    
    logout = ""
    for elem in folders: #for breeder folders
        if elem.org.is_primeval == False: #log
            logout += add_organism_log(env, elem.org) + '\n'
    for elem in folders:
        for subelem in elem.progeny: #for progeny folders
            if subelem.org.is_primeval == False: #log
                logout += add_organism_log(env, subelem.org) + '\n'
    for elem in rfolders:
        if elem.org.is_primeval == False: #log
            logout += add_organism_log(env, elem.org) + '\n'
    #adds arrays to logfile
    for elem in arrays:
        logout += 'A{'
        for number in elem:
            logout += str(number) + ','
        logout = logout[:-1] + '}\n'
    logout += "Pressure: " + str(env.pressure) + '\n'
    
    #if adding this log would make log file too big
    if len(logout) + env.current_log_size >= env.logsize:
        env.current_log_size = 0 #then reset logfile size
        env.lognum += 1 #then increment logfile
    log_file = './logs/log' + str(env.lognum) + '.txt' 
    if not os.path.exists('./logs/'):
        os.makedirs('./logs/')
    log = open(log_file, 'a')
    log.write(logout)
    log.close() 
    env.current_log_size += len(logout) #fix logfile size

def Setup_Gen(folders, rfolders, arraylist, env):
   #Sort by avg ops
   labtable = []
   for rand in range(env.rands):
       labtable.append(rfolders[rand].org)

   for bnum in range(env.breeders):
       labtable.append(folders[bnum].org)
       for pnum in range(env.kids):
           labtable.append(folders[bnum].progeny[pnum].org)

   labtable.sort(key=lambda subject: env.pressure if subject.avgops> env.pressure else subject.avgops, reverse = False)

 
   #set primeval status and call log function
   for x in range(env.breeders):
       if labtable[x].avgops < env.pressure:
           if labtable[x].is_primeval == True:
               labtable[x].is_primeval = False
               labtable[x].lineage_id = env.lineage_counter
               env.lineage_counter += 1
       else:
           break
   Log_Gen(folders, rfolders, arraylist, env)
   env.gennumber += 1
   
   #Set new pressure
   num = labtable[env.breeders-1].avgops*env.buff
   if num < env.pressure:
       env.pressure = num
   #Put orgs in correct folders for breeders
   #spawn randoms
   for rand in range(env.rands):
       rfolders[rand].org = makegene(random.randint(1, env.maxgenes+1))
       rfolders[rand].org.location = rfolders[rand].path
       rfolders[rand].org.logloc = "R_"+str(rand+1)
       writec(rfolders[rand].path, rfolders[rand].org, env.pressure)
       call('g++ '+rfolders[rand].path+ '*.cpp ./habitat/biosort.o -o ' + rfolders[rand].path + 'organism.out -g', shell = True)


   for bnum in range(env.breeders):  
            folders[bnum].org = labtable[bnum]
            folders[bnum].org.folder = folders[bnum].path
            folders[bnum].org.logloc = "B_"+str(bnum+1)
            writec(folders[bnum].path, folders[bnum].org, env.pressure)
            call('g++ '+folders[bnum].path+ '*.cpp ./habitat/biosort.o -o ' + folders[bnum].path + 'organism.out -g', shell = True)
   #Spawn kids
   for bnum in range(env.breeders):
       if folders[bnum].org.is_primeval == False:
            for pnum in range(env.kids):
                folders[bnum].progeny[pnum].org = Organism(folders[bnum].org.genesequence)
                folders[bnum].progeny[pnum].org.folder = folders[bnum].progeny[pnum].path
                folders[bnum].progeny[pnum].org.logloc = "P_"+str(pnum+1)+"_B_"+str(bnum+1)
                copy(folders[bnum].path+"organism.cpp", folders[bnum].progeny[pnum].path)
                mutate(folders[bnum].progeny[pnum].org, env.mutations+env.adds*x, env.weight, env.pressure, env.maxgenes) # mutate the gene and write mutation to file
                folders[bnum].progeny[pnum].org.lineage_id = folders[bnum].org.lineage_id
                folders[bnum].progeny[pnum].org.is_primeval = False
       else:
           folders[bnum].org = makegene(random.randint(1, env.maxgenes+1))
           folders[bnum].org.location = folders[bnum].path
           folders[bnum].org.logloc = "B_"+str(bnum+1)
           writec(folders[bnum].path, folders[bnum].org, env.pressure) # write out the file
           call('g++ '+ folders[bnum].path + '*.cpp ./habitat/biosort.o -o ' + folders[bnum].path + 'organism.out -g', shell = True) 
           for pnum in range(env.kids):
                folders[bnum].progeny[pnum].org = makegene(random.randint(1, env.maxgenes+1))
                folders[bnum].progeny[pnum].org.folder = folders[bnum].progeny[pnum].path
                folders[bnum].progeny[pnum].org.logloc = "P_"+str(pnum+1)+"_B_"+str(bnum+1)
                writec(folders[bnum].progeny[pnum].path, folders[bnum].org, env.pressure) # write out the file
                call('g++ '+ folders[bnum].progeny[pnum].path + '*.cpp ./habitat/biosort.o -o ' + folders[bnum].progeny[pnum].path + 'organism.out -g', shell = True) 
                
