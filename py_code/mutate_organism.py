#code for mutations goes here
import random
from create_gene import get_replacement, roll4d6
from transcribe_c import writec 
from organism import Organism

# Distance from a given mutable field in one gene to its corresponding field in the next gene, should not be changed unless
# organism skeleton changes
genelength = 95
# Dictionary to hold offest from gene start to the mutable field we wish to change
d20 = {1:0, 2:3, 3:5, 4:24, 5:29, 6:33, 7:36, 8:41, 9:43, 10:47, 11:52, 12:56, 13:60, 14:64, 15:70, 16:74, 17:78, 18:81}


# Used to calculate the inital byte offset into an organism at which the first mutable field exists
def calc_header(file_location): 
    f = open(file_location+"organism.cpp", 'r')
    count = 0
    for i in range(16):
        temp = f.readline()
        count += len(temp)
    count += 4
    f.close()
    return count
 

# Creates a new randomized gene at the pivot point in the genesequence
def create_gene(org, pivot, file_location, pressure):
    newgene = roll4d6()
    newsequence = org.genesequence[:pivot]+newgene+org.genesequence[pivot:]
    org.genesequence = newsequence
    writec(file_location, org.genesequence, pressure)

# Removes a gene who begins at index "start" in the genesequence
def delete_gene(org, start, file_location, pressure):
    newsequence = org.genesequence[:start]+org.genesequence[start+17:]
    org.genesequence = newsequence
    writec(file_location, org.genesequence, pressure)


# Copies the gene at index source to index dest in the genesequence
def copy_gene(org, source, dest, file_location, pressure):
    newstring = org.genesequence[source:source+17]
    newstring = org.genesequence[:dest]+newstring+org.genesequence[dest:]
    org.genesequence = newstring
    writec(file_location, org.genesequence, pressure)
    

# Mutates a gene with either point mutations or gene mutations
# takes an organism, the number of mutations to do, the percent chance of deletion if gene mutation
#(100 - weight is percent chance of adding a gene on gene mutation), the selective pressure for the organism,
# and the maximum genes this organism can have
def mutate(org, num_mutations, weight, pressure, max_genes):
    file_location = org.folder

    # Loop to mutate x number of times
    for x in range(num_mutations):

        # Variable setting
        length = len(org.genesequence)
        index = 9 #random.randint(0, length-1)
        shift = 0 # For shifting offset in the case of offset being after ) or ]
        
        # The case for gene mutation
        if org.genesequence[index] == "g":
            delete_chance = random.randint(1, 100)

            # Add Gene (copy or create random new one)
            if k > delete_chance and length/17 < max_genes:
                if random.randint(1,2) == 1:
                    num = (len(org.genesequence)/17)+1
                    num = (random.randint(0, num))*17
                    copy_gene(org, index, num, file_location, pressure)
                else:
                    num = (len(org.genesequence)/17)+1
                    num = (random.randint(0, num))*17
                    create_gene(org, num, file_location, pressure)
            
            # Gene has too many gene mutations, so we reroll our index
            elif delete_chance > weight and length/17 > max_genes:
                x = x-1

            # Delete gene, returns dead if we deleted the last gene in an organism
            else:
                delete_gene(org, index, file_location, pressure)
                if org.genesequence == '':
                    return "dead"
        
        # The case for point mutation
        else:
            # Choose replacement for index
            replace_with = get_replacement(index%17)
            # Ammend gene sequence
            if len(org.genesequence)-1 == index:
                org.genesequence = org.genesequence[:index]+replace_with[0]
            else:
                org.genesequence = org.genesequence[:index]+replace_with[0]+org.genesequence[index+1:]
            # Variables for determining byte offset in file
            genenum = index/17
            offset = index%17
            # The case for changing an open paren or an a[, (requires 2 seeks in file)
            if offset in [4, 9]:
                point_mutate(file_location, genenum, offset+(offset/9), replace_with[1], org.genesequence, 1)
            # All other cases, we calculate shift to indicate if the gene index does not match
            # the mutable field location due to a gene not having closed paren or closed bracket
            else:
                if offset in [1, 2, 3, 5, 6, 7]:
                    shift = 0
                if offset in [8, 10, 11, 12]:
                    shift = 1
                if offset in [13, 14, 15, 16]:
                    shift = 2
                point_mutate(file_location, genenum, offset+shift, replace_with[1], org.genesequence, 0)

# Mutates one or two mutable fields in the organism, takes in
# file location, how many genes into the organism the mutation should occur, how many
# mutable fields into that gene the mutation should occur (1-18), the new value at
# that mutable field, the genesequence, and a flag, 1= change 2 fields, 0 = change 1 field
def point_mutate(file_location, gene_number, off, change, sequence, flag):
    header = calc_header(file_location)
    f = open(file_location+"organism.cpp", 'r+')
    # Modifies gene sequence at the top
    f.seek(2)
    f.write(sequence)
    # Modifies the byte in the file correlating to the gene sequence change
    offseter = header+genelength*gene_number+d20[off]
    f.seek(offseter)
    f.write(str(change))
    # If we are at 4 or 9 we close our bracket or paren correctly
    if flag == 1:
        offseter += (d20[off+4]-d20[off])
        f.seek(offseter)
        if str(change) == 'a[':
            f.write(']')
        else:
            f.write(')')
    f.close()

