#code for mutations goes here
import random
from create_gene import get_replacement, roll4d6
from transcribe_c import writec 
from organism import Organism

pressure = 1000
genelength = 95
d20 = {1:0, 2:3, 3:5, 4:24, 5:29, 6:33, 7:36, 8:41, 9:43, 10:47, 11:52, 12:56, 13:59, 14:64, 15:70, 16:74, 17:78, 18:81}



def calc_header(file_location): 
    f = open(file_location+"organism.cpp", 'r')
    count = 0
    for i in range(16):
        temp = f.readline()
        count += len(temp)
    count += 4
    f.close()
    return count
 

def create_gene(org, pivot, file_location):
    newgene = roll4d6()
    newsequence = org.genesequence[:pivot]+newgene+org.genesequence[pivot:]
    org.genesequence = newsequence
    writec(file_location, org.genesequence, pressure)

def delete_gene(org, start, file_location):
    newsequence = org.genesequence[:start]+org.genesequence[start+17:]
    org.genesequence = newsequence
    writec(file_location, org.genesequence, pressure)

def copy_gene(org, source, dest, file_location):
    newstring = org.genesequence[source:source+17]
    newstring = org.genesequence[:dest]+newstring+org.genesequence[dest:]
    org.genesequence = newstring
    writec(file_location, org.genesequence, pressure)
    



def mutate(org, num_mutations, weight):
    file_location = org.folder
    for x in range(num_mutations):
        i = random.randint(0, len(org.genesequence)-1)
        j = 0 # for shifting offset in the case of offset being after ) or ]
        if org.genesequence[i] == "g":
            k = random.randint(1, 100)
            if k > weight:
                if random.randint(1,2) == 1:
                    num = (len(org.genesequence)/17)+1
                    num = (random.randint(0, num))*17
                    copy_gene(org, i, num, file_location)
                else:
                    num = (len(org.genesequence)/17)+1
                    num = (random.randint(0, num))*17
                    create_gene(org, num, file_location)
            else:
                delete_gene(org, i, file_location)
        else:
            replace_with = get_replacement(i%17)
            if len(org.genesequence)-1 == i:
                org.genesequence = org.gensequence[:i]+replace_with[0]
            else:
                org.genesequence = org.genesequence[:i]+replace_with[0]+org.genesequence[i+1:]
            genenum = i/17
            offset = i%17
            if offset in [4, 9]:
                point_mutate(file_location, genenum, offset+(offset/9), replace_with[1], org.genesequence, 1)
            else:
                if offset in [1, 2, 3, 5, 6, 7]:
                    j = 0
                if offset in [8, 10, 11, 12]:
                    j = 1
                if offset in [13, 14, 15, 16]:
                    j = 2
                point_mutate(file_location, genenum, offset+j, replace_with[1], org.genesequence, 0)


def point_mutate(file_location, gene_number, off, change, sequence, flag):
    header = calc_header(file_location)
    f = open(file_location+"organism.cpp", 'r+')
    # modifies gene sequence at the top
    f.seek(2)
    f.write(sequence)
    # modifies the byte in the file correlating to the gene sequence change
    offseter = header+genelength*gene_number+d20[off]
    f.seek(offseter)
    f.write(str(change))
    #if we are at 4 or 9 we close our bracket or paren correctly
    if flag == 1:
        offseter += (17)
        f.seek(offseter)
        if str(change) == 'a[':
            f.write(']')
        else:
            f.write(')')
    f.close()

string = "g0+Rb9%9!pr%4u0-6g7-3b5/9!p7/5u6-2g1*1p0%7Gbi*2u5-3g9-3b2%3!pi/4d8%3"
org = Organism(string)
org.folder = "./test/"
writec(org.folder, string, 1000)
writec("./test1", string, 1000)
mutate(org, 3, 50)
#for byteinfile in range(0, 96):
#    offset = calc_header("./test/")+genelength*(byteinfile/17)+d20[byteinfile%17]
#    f = open("./test/organism.cpp", 'r+')
#    f.seek(offset)
#    f.write('?')
#    f.close()
