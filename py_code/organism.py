#!/usr/bin/env python

class Organism:
    def __init__(self, sequence):
        self.genesequence = sequence
        self.avgops = 0
        self.ops = [] 
        self.survival = 0
        self.folder = "N"
        self.is_primeval = True
