#!/usr/bin/env python

class Organism:
    def __init__(self, sequence):
        self.genesequence = sequence #Gene sequence that makes up this organism
        self.avgops = 0 #Holds the average ops to sort arrays in the current generation
        self.ops = [] #The array to hold individual opcounts per run of the current generation
        self.survival = 0 #
        self.folder = "N" #Folder this organism is currently housed in ie habitat/breeder1/progeny1/
        self.logloc = "N" #Log shorthand for folder location ie P_1_B_1
        self.is_primeval = True #Flag to tell if this organism is random and has not sorted (for logging)
        self.lineage_id = 0 #every time is_primeval is set to false
                            #(every time a totally random gene
                            #gets to become a breeder) it gets a unique
                            #id number.  This serves as its lineage id.
                            #All of its offspring should get the same
                            #id number in perpetuity.
