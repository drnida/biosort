#!/usr/bin/env python

import ConfigParser
import os
import subprocess

class Environment:
    def __init__(self, ge, ru, ra, br, ki, mu, ad, pr, ma, ar, pe, na, we, bu):
        self.gens = ge #number of gens to run
        self.runs = ru #number of runs per gen
        self.rands = ra #number of random things to run NYI
        self.breeders = br #number of breeders
        self.kids = ki #number of kids per breeder
        self.mutations = mu #number of baseline mutations to run
        self.adds = ad #number of mutations to add per kid
        self.pressure = pr #current pressure (reduced when better organism comes along)
        self.maxgenes = ma #number of genes maximum
        self.arraysize = ar #size of array to be sorted
        self.penalty = pe #penalty added if organism does not meet pressure
        self.name = na #name of program run
        self.weight = we #percentage chance to delete rahther than add when doing gene mutation
        self.buff = (bu/100)+1 #% of buffer to meet in order to reduce pressure (default 50)
        self.gennumber = 0
        #logging functionality
        self.lineage_counter = 1
        self.lognum = 0
        self.current_log_size = 0
        self.logsize = 

def CreateEnvironment():

    config = ConfigParser.RawConfigParser()
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
    weight = config.get('probability', 'weight');

    env = Environment(num_generations, runs_per_generation, num_random, num_breeders, kids_per_breeder, num_mutations, num_add_mutations, start_pressure, gene_max, array_size, penalty, name, weight, buff)

    if not os.path.isdir('./habitat'):
        os.mkdir('./habitat')

    subprocess.call('g++ -c -o ./habitat/biosort.o ./c_code/biosort.cpp -g', shell = True) 

    for x in range(1, num_breeders+1):
        try:
            os.mkdir("./habitat/breeder" + str(x))
        except:
            pass
        for y in range(1, kids_per_breeder+1):
            try:
                os.mkdir("./habitat/breeder" + str(x)+ "/progeny" + str(y))
            except:
                pass
    return env
