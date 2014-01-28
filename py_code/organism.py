#!/usr/bin/env python

class Organism:
    def __init__(self, sequence):
        self.folder = ''
        self.genesequence = sequence
        self.avgops = 0
        self.ops = [] 
        self.survival = 0
