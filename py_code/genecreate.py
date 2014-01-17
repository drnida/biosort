#!/usr/bin/env python
#The following dictionaries are used to 1) create random genes and 2) Map gene sequence to tokens
import random

#array index mods to 1
d1 = {'0':'  0', '1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'r':'r()'}
#2,7
d2 = {'p':' (', 'b':'a['}
#3,5,8,10,12,14
d3 = {'0':'  0', '1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'r':'r()','i':'  i','v':'  v'}
#4,9,13
d4 = {'-':' -', '+':' +', '*':' *', 'N':'//', '%':'%', '/':'/'}
#6
d5 = {'=':'==', '!':'!=', 'L':'<=', 'G':'>=', '<':' <', '>':' >'}
#11 (Not for mapping gene sequence, but used to randomize in the same way as the other 5)
d6 = {'w':'w'}
#This is a special case for 5, 10, and 14 that doesnt allow mod or divide by 0
d7 = {'1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'R':'R()'}

# Takes in a gene sequence and returns an array of tokens with the opcount for one loop as the last token
def translategene(astring):
	newstring = ''
        count = 0
	for i, c in enumerate(astring):
		j = i/15
		k = i%15
		if k == 0:
                        count += 6
			if j == 0:
				newstring+='g'
			if j > 0:
				newstring+=';g'
		elif k == 1:
			newstring+=(';'+d1[c])
		elif k in [2,7]:
			newstring+=(';'+d2[c])
		elif k in [3,5,8,10,12,14]:
			newstring+=(';'+d3[c])
		elif k in [4,9,13]:
                        if c != 'N':
                            count += 1
			newstring+=(';'+d4[c])
		elif k == 6:
			if astring[i-4] == 'p':
				newstring+=';)'
			else:
				newstring+=';]'
			newstring+=(';'+d5[c])
		elif k == 11:
			if astring[i-4] == 'p':
				newstring+=';)'
			else:
				newstring+=';]'
			newstring+=(';'+c)
	newstring += ';'+str(count)
        tokens = newstring.split(';')
	return tokens

def roll4d6():
	genesequence = ''
        nozero = False
	for i in range(0, 15):
		if i == 0:
			genesequence += 'g'
		elif i == 1:
			genesequence += random.choice(d1.keys())
		elif i in [2,7]:
			genesequence += random.choice(d2.keys())
		elif i in [3,8,12]:
			genesequence += random.choice(d3.keys())
                elif i in [5,10,14]:
                        if nozero == True:
                            genesequence += random.choice(d7.keys())
                            nozero = False
                        else:
                            genesequence += random.choice(d3.keys())
		elif i in [4,9,13]:
			c = random.choice(d4.keys())
                        if c in ['/','%']:
                            nozero = True
                        genesequence += c
		elif i == 6:
			genesequence += random.choice(d5.keys())
		elif i == 11:
			genesequence += random.choice(d6.keys())
	return genesequence


def howmany(num):
	newstring = ''
	for i in range(num):
		newstring += roll4d6()
	return newstring
