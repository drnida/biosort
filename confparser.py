
import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

num_of_gen = config.getint('generation', 'NUMGEN')
runs_per_gen = config.getint('generation', 'RUNGEN')

num_of_breed = config.getint('breed', 'NUMBREED')
off_per_breed = config.getint('breed', 'OFFPERBREED')
mut_per_gene = config.getint('breed', 'MUTPERGENE')

print num_of_gen
print runs_per_gen

print num_of_breed
print off_per_breed
print mut_per_gene




