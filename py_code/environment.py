#!/usr/bin/env python

import ConfigParser
import os
from writetoc.py import writec

config = ConfigParser.RawConfigParser()
config.read(['../config.cfg'])

#generation
num_generations = config.get('generation', 'num_generations')
runs_per_generation = config.getint('generation', 'runs_per_generation')

#petri
num_random = config.getint('petri', 'num_random')
num_breeders = config.getint('petri', 'num_breeders')
kids_per_breeder = config.getint('petri', 'kids_per_breeder')

#mutation
num_mutations = config.getint('mutation', 'num_mutations')
num_add_mutations = config.getint('mutation', 'num_add_mutations')

print num_breeders
print kids_per_breeder

if not os.path.isdir(../'habitat'):
    os.mkdir('../habitat')

for x in range(0, num_breeders):
    try:
        os.mkdir("../habitat/breeder" + str(x + 1))
    except:
        pass
for x in range(num_breeders, num_breeders * kids_per_breeder):
    try:
        os.mkdir("../habitat/specimen" + str(x + 1))
    except:
        pass
