import os


#Global Python Variables:
Generation = 0; #generation number
Opcutoff = 0; #number of ops before an organism is killed off



#G(generation number)
#BO(opcount)g(genesequence)
#O(opcount)g(genesequence)

# Returns a list of numbers 0 through X in a random order
def make_list(x):
    mylist = list(xrange(x))
    random.shuffle(mylist)
    return mylist



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
