# hey look a change

import random
import os

#The following dictionaries are used to 1) create random genes and 2) Map gene sequence to tokens

#array index mods to 1
d1 = {'0':'  0', '1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'r':'r()'}
#2,7
d2 = {'p':' (', 'b':'a['}
#3,5,8,10,12,14
d3 = {'0':'  0', '1':'  1', '2':'  2', '3':'  3', '4':'  4', '5':'  5', '6':'  6', '7':'  7', '8':'  8', '9':'  9', 'r':'r()','i':'  i','v':'  v'}
#4,9,13
d4 = {'-':' -', '+':' +', '*':' *', '/':' /', '%':' %', 'N':'//'}
#6
d5 = {'=':'==', '!':'!=', 'L':'<=', 'G':'>=', '<':' <', '>':' >'}
#11 (Not for mapping gene sequence, but used to randomize in the same way as the other 5)
d6 = {'w':'w', 'u':'u', 'd':'d'}


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

#body should look as follows
#do{
#i=___; //1) 0-9 or r()
#v=a[i];
#if((__ ___ __ ___//1) ( or a[ which sets 1 on next line 2) 0-9, r(), i, or v 3) *, /, -, % or // 4) 0-9, r(), i or v
#_ %S)__ // 1) ) or ] defined by 1 of last line 2) logical op
#(__ ___ __ ___ //1) ( or a[ which defines 1 on the next line 2) 0-9, r(), i, or v 3) *, +, -, /, %, or // 4) 0-9, r(), i, or v
#_ %S))//1) ) or ] defined by 1 on last line
#{
#_(( ___ __ ___// 1) W, U, or D 2) 0-9, r(), i, or v 3) +, -, /, %, or // 4) 0-9, r(), i, or v
#)%S)
#}
#after genes finish
#count += ops;
#}while(not_sorted(a[])&& count <SelectivePressure);

def writeheader():
    header = '#include "biosort.h"\n\nint count=0;\nextern int * a;\nextern int i;\nextern int count;\n'\
    'int temp[16] = {5, 9, 3, 2, 6, 1, 4, 16, 12, 8, 7, 11, 10, 13, 15, 14};\n\nint main()\n{\na=temp;\n'
    return header


#Writes the do while loop for the .cpp programs (organisms)
def writebody(organism, tok, num):
        genesequence = writeheader()
        length = len(tok)
        counter = tok[length-1]
        del tok[-1]
	for j in range(num):
		i = j*17
		genesequence += '\ni='+tok[1+i]+';\nv=a[i];\nif(('+tok[2+i]+' '+tok[3+i]+' '+tok[4+i]+' '+tok[5+i]+\
		'\n'+tok[6+i]+'%S)'+tok[7+i]+'\n('+tok[8+i]+' '+tok[9+i]+' '+tok[10+i]+' '+tok[11+i]+\
		'\n'+tok[12+i]+'%S))\n{\n'+tok[13+i]+'(('+tok[14+i]+' '+tok[15+i]+' '+tok[16+i]+'\n'+\
                ')%S)}\n';
        organism.write('do{'+genesequence+'count +='+counter+'}while(!sorted(a[])&& count<Pressure)\nreturn opcount;')
	return

#Creates one file
def writec(astring, foldernum):
        folder = 'Petri_Dish_'+str(foldernum)
        if not os.path.isdir(folder):
            os.makedirs(folder)
	filename = folder+'/organism.cpp'
	organism = open(filename, 'w+')
	tokens = translategene(astring) #Creates string of tokens out of gene sequence
	num = len(tokens)/17 #Number of genes
	writebody(organism, tokens, num) #Writes the body of the c++ file given the tokens
	
	return
	
def roll4d6():
	genesequence = ''
	for i in range(0, 15):
		if i == 0:
			genesequence += 'g'
		elif i == 1:
			genesequence += random.choice(d1.keys())
		elif i in [2,7]:
			genesequence += random.choice(d2.keys())
		elif i in [3,5,8,10,12,14]:
			genesequence += random.choice(d3.keys())
		elif i in [4,9,13]:
			genesequence += random.choice(d4.keys())
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

teststring = howmany(10)
print teststring
writec(teststring, 1)
