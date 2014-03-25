#code for mutations goes here
import random
from create_gene import get_replacement, roll4d6
from transcribe_c import writec 
from organism import Organism



# Creates a new randomized gene at the pivot point in the genesequence
def create_gene(org, pivot, file_location):
    newgene = roll4d6()
    newsequence = org.genesequence[:pivot]+newgene+org.genesequence[pivot:]
    org.genesequence = newsequence

# Removes a gene who begins at index "start" in the genesequence
def delete_gene(org, start, file_location):
    newsequence = org.genesequence[:start]+org.genesequence[start+17:]
    org.genesequence = newsequence


# Copies the gene at index source to index dest in the genesequence
def copy_gene(org, source, dest, file_location):
    newstring = org.genesequence[source:source+17]
    newstring = org.genesequence[:dest]+newstring+org.genesequence[dest:]
    org.genesequence = newstring
    

# Mutates a gene with either point mutations or gene mutations
# takes an organism, the number of mutations to do, the percent chance of deletion if gene mutation
#(100 - weight is percent chance of adding a gene on gene mutation),
# and the maximum genes this organism can have
def mutate(org, num_mutations, weight, max_genes):
    file_location = org.folder

    # Loop to mutate num_mutations number of times
    for mutation_num in range(num_mutations):

        # Variable setting
        length = len(org.genesequence) #Length of the genesequence
        index = random.randint(0, length-1) #The index of the gene sequence to mutate
        
        # The case for gene mutation
        if org.genesequence[index] == "g":
            delete_chance = random.randint(1, 100)

            # Add Gene (copy or create random new one)
            if weight > delete_chance and length/17 < max_genes:
                if random.randint(1,2) == 1:
                    num = (len(org.genesequence)/17)+1
                    num = (random.randint(0, num))*17
                    copy_gene(org, index, num, file_location)
                else:
                    num = (len(org.genesequence)/17)+1
                    num = (random.randint(0, num))*17
                    create_gene(org, num, file_location)
            
            # Gene has too many gene mutations, so we reroll our index
            elif delete_chance > weight and length/17 > max_genes:
                mutation_num = mutation_num-1

            # Delete gene
            else:
                if len(org.genesequence) > 17:
                    delete_gene(org, index, file_location)
        
        # The case for point mutation
        else:
            # Choose replacement for index
            replace_with = get_replacement(index%17)
            # Ammend gene sequence
            if len(org.genesequence)-1 == index:
                org.genesequence = org.genesequence[:index]+replace_with[0]
            else:
                org.genesequence = org.genesequence[:index]+replace_with[0]+org.genesequence[index+1:]
            
