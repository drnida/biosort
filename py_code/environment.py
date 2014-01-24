#!/usr/bin/env python

import ConfigParser
import os
import subprocess

class Environment:
    def __init__(self, ge, ru, ra, br, ki, mu, ad, pr, ma, ar, pe, na):
        self.gens = ge
        self.runs = ru
        self.rands = ra
        self.breeders = br
        self.kids = ki
        self.mutations = mu
        self.adds = ad
        self.pressure = pr
        self.maxgenes = ma
        self.arraysize = ar
        self.penalty = pe
        self.name = na

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

    #genes
    gene_max = config.getint('genes', 'gene_max')

    #array
    array_size = config.getint('array', 'array_size')

    #sim name
    name = config.get('name', 'sim_name')

    print num_breeders
    print kids_per_breeder

    env = Environment(num_generations, runs_per_generation, num_random, num_breeders, kids_per_breeder, num_mutations, num_add_mutations, start_pressure, gene_max, array_size, penalty, name)

    if not os.path.isdir('./habitat'):
        os.mkdir('./habitat')

    subprocess.call('g++ -c -o ./habitat/biosort.o ./c_code/biosort.cpp -g', shell = True) 

    for x in range(0, num_breeders):
        try:
            os.mkdir("./habitat/breeder" + str(x + 1))
        except:
            pass
    for x in range(num_breeders, (num_breeders + num_breeders * kids_per_breeder)):
        try:
            os.mkdir("./habitat/specimen" + str(x + 1))
        except:
            pass
    return env
