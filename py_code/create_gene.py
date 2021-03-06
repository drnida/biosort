#/usr/bin/env python
#The following dictionaries are used to 1) create random genes and 2) Map gene sequence to tokens
import random
from organism import Organism


#These are the dictionaries used to create and parse gene sequences
#Language of Gene Sequence:
#S -> G+
#G -> 'g'<d1><d4><d7><d2><d3><d4><d7><d5><d2><d3><d4><d7><d6><d3><d4><d7>

#Comments represent the what index % 17 maps to for each dictionary
#1
d1 = {'0':'  0', '1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'r':'r()'}
#4,9
d2 = {'p':' (', 'b':'a['}
#5,10,14
d3 = {'0':'  0', '1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'r':'r()','i':'  i','v':'  v'}
#2,6,11,15
d4 = {'-':' -', '+':' +', '*':' *', 'N':'//', '%':' %', '/':' /'}
#8
d5 = {'=':'==', '!':'!=', 'L':'<=', 'G':'>=', '<':' <', '>':' >'}
#13 (Not for mapping gene sequence, but used to randomize in the same way as the other 5)
d6 = {'w':'w', 'u':'u', 'd':'d'}
#This is a special case for 3, 7, 12, and 16 that doesnt allow mod or divide by 0
d7 = {'1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'R':'R()'}


#Used to point mutate a given index, the num is the index mod 17 (does not have a
#case for 0 because the mutation for 'g' is handled in a different way
def get_replacement(num):
    if num == 1:
        temp = random.choice(d1.keys())
        return [temp, d1[temp]]
    if num in [4, 9]:
        temp = random.choice(d2.keys())
        return [temp, d2[temp]]
    if num in [3, 7, 12, 16]:
        temp = random.choice(d7.keys())
        return [temp, d7[temp]]
    if num in [5, 10, 14]:
        temp = random.choice(d3.keys())
        return [temp, d3[temp]]
    if num in [2, 6, 11, 15]:
        temp = random.choice(d4.keys())
        return [temp, d4[temp]]
    if num == 8:
        temp = random.choice(d5.keys())
        return [temp, d5[temp]]
    if num == 13:
        temp = random.choice(d6.keys())
        return [temp, d6[temp]]



# Takes in a gene sequence and returns a list of tokens with the opcount for one loop as the last token
def translategene(astring):
    newstring = ''
    count = 0
    for i, c in enumerate(astring):
        j = i/17
        k = i%17
        if k == 0:
            count += 6
            if j == 0:
                newstring+='g'
            if j > 0:
                newstring+=';g'
        elif k == 1:
            newstring+=(';'+d1[c])
        elif k in [4,9]:
            newstring+=(';'+d2[c])
        elif k in [3,7,12,16]:
            newstring+=(';'+d7[c])
        elif k in [5,10,14]:
            newstring+=(';'+d3[c])
        elif k in [2,6,11,15]:
            if c != 'N':
                count += 1
            newstring+=(';'+d4[c])
        elif k == 8:
            if astring[i-4] == 'p':
                newstring+=';)'
            else:
                newstring+=';]'
            newstring+=(';'+d5[c])
        elif k == 13:
            if astring[i-4] == 'p':
                newstring+=';)'
            else:
                newstring+=';]'
            newstring+=(';'+c)
    newstring += ';'+str(count)
    tokens = newstring.split(';')
    return tokens

#Creates a randomized single gene using the dictionary rules
def roll4d6():
    genesequence = ''
    for i in range(0, 17):
        if i == 0:
            genesequence += 'g'
        elif i == 1:
            genesequence += random.choice(d1.keys())
        elif i in [4,9]:
            genesequence += random.choice(d2.keys())
        elif i in [5,10,14]:
            c = random.choice(d3.keys())
            while i == 14 and c == 'v':
                c = random.choice(d3.keys())
            genesequence += c
        elif i in [3,7,12,16]:
            genesequence += random.choice(d7.keys())
        elif i in [2,6,11,15]:
            genesequence += random.choice(d4.keys())
        elif i == 8:
            genesequence += random.choice(d5.keys())
        elif i == 13:
            genesequence += random.choice(d6.keys())
    return genesequence

#Makes a gene sequence, num genes long
def makegene(num):
    newstring = ''
    for i in range(num):
        newstring += roll4d6()
    org = Organism(newstring)
    return org
