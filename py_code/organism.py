#!/usr/bin/env python

class Organism:
    def __init__(self, sequence):
        self.genesequence = sequence
        self.avgops = 0
        self.ops = [] 
        self.survival = 0
        self.folder = "N"
        self.logloc = 0
        self.is_primeval = True
        self.lineage_id = 0 #every time is_primeval is set to false
                            #(ie. every time a totally random gene
                            #gets to become a breeder) it gets a unique
                            #id number.  This serves as its lineage id.
                            #All of its offspring should get the same
                            #id number in perpetuity.
