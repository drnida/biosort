#!/usr/bin/env python

import ConfigParser
import os
import subprocess

class Environment:
    def __init__(self, ge, ru, ra, br, ki, mu, ad, pr, ma, ar, pe, na, we):
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
        self.weight = we

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

    #probability
    weight = config.get('probability', 'weight');

    env = Environment(num_generations, runs_per_generation, num_random, num_breeders, kids_per_breeder, num_mutations, num_add_mutations, start_pressure, gene_max, array_size, penalty, name, weight)

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
                os.mkdir("./habitat/breeder" + str(x)+ "/specimen" + str(y))
            except:
                pass
    return env
