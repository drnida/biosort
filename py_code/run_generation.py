import os 
import random
import set_environment
import sys
from mutate_organism import mutate
from transcribe_c import writec
from create_gene import makegene
from organism import Organism
from shutil import copy
from folder import bfolder, pfolder, rfolder
from subprocess import Popen, PIPE, call

#Returns a random array of ints to be sorted
def make_list(x): 
    mylist = list(xrange(x)) 
    random.shuffle(mylist) 
    return mylist 
 
# Returns string containing organism's log output. 
def add_organism_log(env, org): 
    logout = "G" + str(env.gennumber) + ','

    #Determines if organism sorted or not
    if org.avgops >= env.pressure:
        logout += 'F' + ',' 
    else:
        logout += 'S' + ','
    
    logout += str(org.avgops) + ','\
    + str(org.lineage_id) + ','\
    + org.logloc + ','\
    + org.genesequence 
   
    return logout


#For spawning a progeny off of a breeder, folder should be progeny folder, orgfrom should be
#the breeder to be spawned from, kidnum is the folder index corresponding to the progeny folder, 
#breedernum is the folder index corresponding to the breeder folder
def make_kid(env, folder, orgfrom, kidnum, breedernum):
    org = Organism(orgfrom.genesequence) # create a new organism based off parent
    org.folder = folder.path # set organism folder
    org.logloc = "P_"+str(kidnum+1)+"_B_"+str(breedernum+1) # set log file representation of folder
    org.lineage_id = orgfrom.lineage_id
    org.is_primeval = False # Did not come from random, not primeval
    folder.org = org # place org in folder
    mutate(folder.org, env.mutations+env.adds*kidnum, env.weight, env.maxgenes) # mutate the gene and write mutation to file
    writec(folder.path, folder.org)
    if env.debug == True:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -g -O0', shell = True) 
    else:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -O0', shell = True) 

#Makes a pure random organism, folder is the folder into which the random will be placed, num
#is the random's folder index
def make_random(env, folder, num):
    org = makegene(random.randint(1, env.maxgenes+1))
    org.folder = folder.path
    org.logloc = "R_"+str(num)
    org.is_primeval = True
    folder.org = org
    writec(folder.path, folder.org)
    if env.debug == True:
        call('g++ '+folder.path+'*.cpp ./habitat/biosort.o -o '+folder.path+'organism.out -g -O0', shell = True)
    else:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -O0', shell = True) 

#Makes a random breeder, folder corresponds to the breeder folder, num is the breeder folder index
def make_random_breeder(env, folder, num):
    org = makegene(random.randint(1, env.maxgenes+1)) # Make a random gene
    org.is_primeval = True # Came from random, so its primeval
    org.folder = folder.path # set org folder (needed for mutate)
    org.logloc = "B_"+str(num) # set log output for location
    folder.org = org
    writec(folder.path, folder.org) # write out the file
    if env.debug == True:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -g -O0', shell = True)
    else:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -O0', shell = True)
    call('cp ./habitat/biosort.h ./habitat/breeder'+str(num)+'/', shell=True) 

#Makes a random progeny, folder is the folder into which the progeny is placed, num is the
#folder index for that folder, parent_num is the parent's folder index
def make_random_kid(env, folder, num, parent_num):
    org = makegene(random.randint(1, env.maxgenes+1)) # make a random gene
    org.folder = folder.path # set org folder (created in init of bfolder)
    org.logloc = "P_"+str(num+1)+"_B_"+str(parent_num+1) # set log output for location
    org.is_primeval = True # came from random, so its primeval
    folder.org = org # add the org to the folder
    writec(folder.path, folder.org) # write out the file
    if env.debug == True:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -g -O0', shell = True) 
    else:
        call('g++ '+ folder.path + '*.cpp ./habitat/biosort.o -o ' + folder.path + 'organism.out -O0', shell = True) 


#Takes in environment and first successful organism, creates the first generation's
#setup, and returns the folders to be used to run the first generation.
def Prep_First_Generation(org, env):
    # Start our Bfolder array
    folders = [] #To hold breeder and progeny folders
    rfolders = [] # To hold random folders
    
    #Sets the first sorter's information and places the .h file into breeder 1
    #so that organism files in the progeny folders can compile correctly
    org.logloc = "B_1" 
    org.folder = "./habitat/breeder1/"
    org.is_primeval = False
    folders.append(bfolder("./habitat/breeder1/", env.kids, org))
    call('cp ./habitat/biosort.h ./habitat/breeder1/biosort.h', shell=True)

    #Creates random files
    for rand in range(env.rands):
        rfolders.append(rfolder("./habitat/random"+str(rand+1)+"/"))
        make_random(env, rfolders[rand], rand+1)

    #Radomly create starting random genes
    for breeder in range(1, env.breeders):
        folders.append(bfolder("./habitat/breeder"+str(breeder+1)+"/", env.kids, None)) # add the folder to the list
        make_random_breeder(env, folders[breeder], breeder+1)
 
        for kid in range(0, env.kids): # starat spawning kids
            make_random_kid(env, folders[breeder].progeny[kid], kid, breeder)

    #Spawn kids off winner
    for kid in range(0, env.kids):
        try:
            call("cp " +folders[0].path+"organism.cpp "+ folders[0].progeny[kid].path, shell=True) # copy the gene from its parent to the kid
        except:
            print "Error copying first gen"
        make_kid(env, folders[0].progeny[kid], folders[0].org, kid, 0)
   
    #Put both lists into one to return just one item
    foldlist = []
    foldlist.append(folders)
    foldlist.append(rfolders)
    return foldlist

#Runs a generation, takes in breeder folder list, random folder list, and environment,
#returns the list of unsorted arrays fed to the organisms (for logging purposes)
def Run_Gen(folders, rfolders, env):
    arraylist = []
    for run in range(env.runs):
        arraylist.append(make_list(env.arraysize))
        array = ' '.join(str(x) for x in arraylist[run])
        labtable = [None for x in range(env.breeders+env.breeders*env.kids+env.rands)]
        
        for rand in range(env.rands):
            command = rfolders[rand].path+"organism.out "+str(env.pressure)+" "+array
            labtable[env.breeders+env.breeders*env.kids+rand] = Popen(command, stdin = PIPE, stdout= PIPE, stderr = PIPE, bufsize = 1, shell = True)

        for bnum in range(env.breeders):
            command = folders[bnum].path+"organism.out "+str(env.pressure)+" "+array
            labtable[bnum] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True)
            for pnum in range(env.kids):
                command = folders[bnum].progeny[pnum].path+"organism.out "+str(env.pressure)+" "+array
                labtable[env.breeders+env.kids*(bnum)+(pnum)] = Popen(command, stdin = PIPE, stdout = PIPE, stderr = PIPE, bufsize = 1, shell = True)

        for subject in range(env.breeders+(env.breeders*env.kids)+env.rands):
            ops = labtable[subject].stdout.readline()
#Comment these!!!!!!!!!!!!!!!!!!!!!!
            if subject in range(env.breeders):
                folders[subject].org.ops.append(int(ops))
            elif subject in range(env.breeders+env.breeders*env.kids):
                bnum = ((subject-env.breeders)//env.kids)
                folders[bnum].progeny[subject-env.breeders-(bnum*env.kids)].org.ops.append(int(ops))
            else:
                rand = subject-(env.breeders+env.breeders*env.kids)
                rfolders[rand].org.ops.append(int(ops))

    #Sums the ops for a generation
    for rand in range(env.rands):
        count_ops(rfolders[rand].org, env)
    
    for bnum in range(env.breeders):
        count_ops(folders[bnum].org, env)
        for pnum in range(env.kids):
            count_ops(folders[bnum].progeny[pnum].org, env)

    return arraylist

#Comment this!!!!!!!!!!!!!!!!!!!!!11
def count_ops(org, env):
    total_opcount = 0
    for run in range(env.runs):
        total_opcount += org.ops[run]
    org.avgops = total_opcount/env.runs
    org.ops = []
            
#Comment this!!!!!!!!!!!!!!!!!!!!!!!!!!!
def Log_Gen(folders, rfolders, arrays, env):
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
        log_file = './logs/log' + str(env.lognum) + '.txt' 
        if not os.path.exists('./logs/'):
            os.makedirs('./logs/')
        log = open(log_file, 'a')
        env.current_log_size = 0 #then reset logfile size
        log.write(''.join(env.loglist)) #write the log
        env.lognum += 1 #increment logfile
        log.close() 
    env.loglist.append(logout)
    env.current_log_size += len(logout) #fix logfile size
    sys.stdout.write("Generation: %s\r" % env.gennumber)
    sys.stdout.flush()


def Setup_Gen(folders, rfolders, arraylist, env):
   #Sort by avg ops
   labtable = []
   for bnum in range(env.breeders):
       labtable.append(folders[bnum].org)
       for pnum in range(env.kids):
           labtable.append(folders[bnum].progeny[pnum].org)
   for rand in range(env.rands):
       labtable.append(rfolders[rand].org)

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
       make_random(env, rfolders[rand], rand)
     
   for bnum in range(env.breeders):  
        folders[bnum].org = labtable[bnum]
        folders[bnum].org.folder = folders[bnum].path
        folders[bnum].org.logloc = "B_"+str(bnum+1)
        writec(folders[bnum].path, folders[bnum].org)
        if env.debug == True:
            call("g++ "+folders[bnum].path+"*.cpp ./habitat/biosort.o -o "+folders[bnum].path+"organism.out -g -O0", shell = True) 
        else:
            call("g++ "+folders[bnum].path+"*.cpp ./habitat/biosort.o -o "+folders[bnum].path+"organism.out -O0", shell = True) 

   #Spawn kids
   for bnum in range(env.breeders):
       if folders[bnum].org.is_primeval == False:
           for pnum in range(env.kids):
                make_kid(env, folders[bnum].progeny[pnum], folders[bnum].org, bnum, pnum)
       else:
           make_random_breeder(env, folders[bnum], bnum)
           for pnum in range(env.kids):
                make_random_kid(env, folders[bnum].progeny[pnum], pnum, bnum)
