#/usr/bin/env python 
 
from create_gene import makegene
from run_generation import make_list, Prep_First_Generation, Setup_Gen, Run_Gen 
from culture_organism import testgene
import random
from set_environment import CreateEnvironment
import subprocess
import time 
 

#Function that takes in the environment given by the config file and begins running the
#program. First it finds a single organism that sorts in the given pressure threshold
#And then populates the first generation off that. It then runs the number of generations
#the environment requests and ends the program by saving the logs and config file to a
#directory with the program run name and a timestamp for its end.
def Start(env):
    ops = 0 #Counter for operations performed by organism before completing
    org = '' #Variable to hold the first organism

    #Creates an organism and runs it, repeats until an organism is found
    #which sorts within the given pressure threshold.
    while ops not in range(1, env.pressure+1):
        org = makegene(random.randint(1, env.maxgenes+1))
        org.folder = "breeder1/"
        arraylist = []#List populated with a number of random arrays of ints of the size
                      #requested by the environment. Arraylist contains x number of these arrays
                      #where x is the number of runs per generation.
        for i in range(env.runs):
            arraylist.append(make_list(env.arraysize))
        testgene(org, arraylist, env)#Function to test a gene without logging to see if it sorts
                                     #within the given pressure threshold.
        ops = org.avgops

    #Once an organism that sorts under pressure is found, program begins generation 1.
    org.lineage_id = env.lineage_counter#Lineage ID is the number given to any organism if it was
                                        #produced randomly and earned a breeder spot. This lets the
                                        #log file trace back where a specific organism came from
                                        #initially.
    env.lineage_counter += 1
    foldlist = Prep_First_Generation(org, env)#Foldlist holds the folders containing the organisms
                                              #to start Generation 1 with. It contains 2 indexes,
                                              #the nonrandom folders are index 0, the random folders
                                              #are index 2.
    folders = foldlist[0]
    rfolders = foldlist[1]
    arraylist = Run_Gen(folders, rfolders, env)#Array list used in each generation is returned for
                                               #logging purposes. Logging cannot be done until a 
                                               #certain point in the Setup for the next gen.
    #Loop to run all generations requested
    for x in range(env.gens):
        Setup_Gen(folders, rfolders, arraylist, env)
        arraylist = Run_Gen(folders, rfolders, env)

    #Once program is finished, all log files are placed into a new subfolder named using
    #the run name and a timestamp. This folder contains all the logs and the config file
    #used for the run.
    path = env.name + str(int(time.time())) + "/"
    try:
        subprocess.call("mkdir ./logs/" + path, shell = True)
    except:
        pass
    subprocess.call("mv ./logs/log* ./logs/" + path, shell = True)
    subprocess.call("cp ./config.cfg ./logs/" + path, shell = True)



#This kicks off the program by deleting all previous log files
#If any are left (If the previous run finished, the logs should already)
#be saved to a new directory, and as such should not be deleted.
#It then creates the environment from the config file and runs the program.
subprocess.call("rm ./log/log*", shell = True)
Start(CreateEnvironment()) 
