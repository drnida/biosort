import os

#Eventually it'd be lovely if we could break the python code
#into 3 files:
    #1) file i/o
        #-this would include all the template code and would be invoked
        # when a new gene needed to be created (rather than a point mutation)
        #-This would also handle populating c-files with the array to be sorted
    #2) gene modification
        #-specifically for single mutations and the algorithms that select
        # what to mutate
    #3) tournament operation

#Global Python Variables:
Generation = 0;
Opcutoff = 0;

#G(generation number)
#BO(opcount)g(genesequence)
#O(opcount)g(genesequence)

def selectcodon(genesequence):
	length = len(genesequence)
	random.randrange(0,length)
	#access dictionary to find where index exists in c code bytewise
	return #whatever


#When to log
#Types of logging
#How should each log look?
def logfile(afile, filepath, opcount)
	if os.path.getsize(filepath) == 0:
		return
	else:
		newstring = afile.readline()
		newstring = newstring[2:-2]
		afile.truncate()
		log = open("logfile.txt", "a+")
		return

#Per run info
def runlog():
	


def writeheader(afile, genesequence):
	afile.write('/*'+genesequence+'*/\n') # Writes out the gene sequence to a header comment
	afile.write('#include "../header.h"\n')
	afile.write('int i, v, S, count;\n')
	afile.write('int a[]={blah};\n')
	afile.write('int main()\n{\n')
	return

	
def writec(astring, foldernum): #TODO: Finish this
	newfile = 'File'+foldernum+'/foo.cpp'
	file = open(newfile, 'r+')
	logfile(file, newfile)#Checks if file contains data, if so copies out gene sequence and clears file
	writeheader(file, astring)#Writes the file header
	newstring = translate(astring) #Creates string of tokens out of gene sequence
	tokens = newstring.split(' ') #Creates array of tokens
	num = len(tokens)%18 #Number of genes
	writebody(file, tokens, num) #Writes the body of the c++ file given the tokens
	writetail(file)#Writes out the end of the c++ file
	return

def pointmutate(file, offset, changeto, incoffset, incchange)#Should work to overwrite chars, can try r+b mode to write binary? TODO: Make a Run->Run version
	file.seek(incoffset)
	file.write(incchange)
	file.seek(offset)
	file.write(changeto)



#compare function that compares the fitness of all the organisms - Also match based on rank - Command line args to alter lambda
#Things to be able to modify tournament based on:
#Number of Winners, Runs per Generation(Average success over x generations wins), Kids per Winners, Generation Limit (When reached, would you like to continue?)
#3 winners of mutations
#write to c
#File IO - write file from gene sequence
#Modify gene sequence (if it modifies single byte, call pointmutate, if it modifies a whole gene, rewrite file)
#Append to log file
#Generate random array



#Data sets
#Per organism, we need:
#-> Gene Sequence, opincrement (count of all operations not performed in a placement function), SelectivePressure
#<- opcount (Fitness), IsDead?
#Python Exclusive: Ranking
	
#*[]()\|
