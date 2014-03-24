#!/usr/bin/env python

import ConfigParser
import os
import subprocess

#Class Environment defines an object containing a number of program parameters which can be passed to various
#functions to conveniently access program configurations
class Environment:
    def __init__(self, ge, ru, ra, br, ki, mu, ad, pr, ma, ar, pe, na, we, bu, ls):
        self.gens = ge #Number of generations before the program terminates
        self.runs = ru #Number of runs per generation
        self.rands = ra #Number of permanently random organisms to maintain
        self.breeders = br #Number of breeders
        self.kids = ki #Number of kids per breeder
        self.mutations = mu #Number of baseline mutations
        self.adds = ad #Number of successive additional mutations for each child
        self.pressure = pr #Current pressure (reduced when better organisms come along)
        self.maxgenes = ma #Maximum number of genes per organism
        self.arraysize = ar #Size of array to be sorted
        self.penalty = pe #Penalty added if organism does not meet pressure
        self.name = na #Name of program run
        self.weight = we #Percentage chance to delete rather than add when doing gene mutation (50 is even chances)
        self.buff = (float(bu)/100.0)+1.0 #Percentage of buffer to meet in order to reduce pressure (default 50)
        self.gennumber = 0 #Counter to track generation number
        #logging functionality
        self.lineage_counter = 1 #A unique stamp on a randomly generated organisms which becomes a breeder (and all future kids)
        self.lognum = 0 #The current number to append to the present logfile (in case of logsize being exceeded)
        self.current_log_size = 0 #Current logfile size
        self.logsize = ls #Size of logfiles in bytes

def CreateEnvironment():

    config = ConfigParser.RawConfigParser()
    if not os.path.exists("./config.cfg"):
        exit("Please copy the config.cfg.dist file to the main biosort directory as config.cfg")
       
    config.read(['./config.cfg'])

    #generation
    num_generations = config.getint('generation', 'num_generations')
    runs_per_generation = config.getint('generation', 'runs_per_generation')

    #petri
    num_random = config.getint('petri', 'num_random')
    num_breeders = config.getint('petri', 'num_breeders')
    kids_per_breeder = config.getint('petri', 'kids_per_breeder')

    #mutation
    num_mutations = config.getint('mutation', 'num_mutations')
    num_add_mutations = config.getint('mutation', 'num_add_mutations')

    #pressure
    start_pressure = config.getint('pressure', 'start_pressure')
    penalty = config.getint('pressure', 'penalty')
    buff = config.getint('pressure', 'buffer')

    #genes
    gene_max = config.getint('genes', 'gene_max')

    #array
    array_size = config.getint('array', 'array_size')

    #sim name
    name = config.get('name', 'sim_name')

    #probability
    weight = config.getint('probability', 'weight');

    #logging
    logsize = config.getint('logging', 'logsize');

    env = Environment(num_generations, runs_per_generation, num_random, num_breeders, kids_per_breeder, num_mutations, num_add_mutations, start_pressure, gene_max, array_size, penalty, name, weight, buff, logsize)

    #Creates habitat folder where organisms will exist
    if not os.path.isdir('./habitat'):
        os.mkdir('./habitat')

    #Compiles object code
    subprocess.call('g++ -c -o ./habitat/biosort.o ./c_code/biosort.cpp -g', shell = True) 

    #Creates appropriate directories for random organisms
    for rand in range(1, num_random+1):
        try:
            os.mkdir("./habitat/random"+str(rand))
        except:
            pass

    #Creates appropriate directories for breeders
    for x in range(1, num_breeders+1):
        try:
            os.mkdir("./habitat/breeder" + str(x))
        except:
            pass
        #Creates appropriate directories for progeny
        for y in range(1, kids_per_breeder+1):
            try:
                os.mkdir("./habitat/breeder" + str(x)+ "/progeny" + str(y))
            except:
                pass
    return env #Return the env object which can be passed for ease of access
