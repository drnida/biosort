#cat all logs together.
# grep -n '*,S,*' logxx.txt > success.txt
#run


#builds key:value dictionaries 
def dict_builder():
	for line in f:
	    gene = line
	    #splits row from csv file into fields
	    ln = gene.split(",")
	    
            #ln0 is gen number
	    #ln1 is success/fail
	    #ln2 is ops count
	    #ln3 is lineage ID
	    #ln4 is directory
	    #ln5 is gene


	    #returns if parser encounters a F in the success/faiure field
	    #parser only produces data for successes
	    if ln[1] == "F":
		print "Remove failures from log file"
		print "use grep -n '*,S,*' logxx.txt > success.txt"
		return 0 

	    #counts the occurances of a specific gene
	    if ln[5] in gene_count:
		gene_count[ln[5]] += 1
	    else:
		gene_count[ln[5]] = 1

	    #sums op counts for a generation
	    if ln[0] in gen_op_sum:
		gen_op_sum[ln[0]] += int(ln[2])
	    else:
		gen_op_sum[ln[0]] = int(ln[2])

	    #counts number of individuals in a generation
	    if ln[0] in n_per_gen:
		n_per_gen[ln[0]] += 1
	    else:
		n_per_gen[ln[0]] = 1

	    #creates list of all generations in which a given lineage ID occured
	    if ln[3] in id_vs_gen:
		id_vs_gen[ln[3]].append(ln[0][1:])
	    else:
		id_vs_gen[ln[3]] = [ln[0][1:]]



def lineage_vs_generations():
	try:
	   l = open("lineage_vs_generation.txt", 'w')
	except:
	   print "unable to open lineage_vs_generation.txt"
	   return 0

        l.write("lineageID,number_of_gen_survived,first_gen_seen,last_gen_seen\n")
	#prints "lineageID,number of gen survived by lineage, first gen seen, last gen seen"
	for lineage in id_vs_gen:
	    first_gen = int(id_vs_gen[lineage][0])
	    last_gen = int(id_vs_gen[lineage][0])

	    
	    for x in id_vs_gen[lineage]:
		if int(x) < first_gen:
		    first_gen = int(x)
		if int(x) > last_gen:
		    last_gen = int(x)
	    
	    l.write( lineage +',' + str(last_gen - first_gen) +','+ str(first_gen) +','+ str(last_gen) + '\n')
	l.close()



def ave_vs_generation():
	try:
	  l = open("ave_vs_gen.txt", 'w')
	except:
	  print "unable to open 'ave_vs_gen.txt'"
	  return 0

	l.write("generation,ave_ops_per_gen\n")

	#prints "generation,ave ops per generation"
	for gen in gen_op_sum:
	    #print str(gen) + "," + str(gen_op_sum[gen]) + "," +str(n_per_gen[gen])
	    ave = int(gen_op_sum[gen])/int(n_per_gen[gen])
	    l.write( gen[1:] + ',' + str(ave) +'\n')

	l.close()


def gene_lifespan():
	try:
	    l = open("gene_lifespan.txt", 'w')
	except:
	    print "Unable to open gene_lifespan.txt"
	    return 0

	l.write("gen_survived\n")
	max_gen = 0
        orgtotal = 0
	#Number of generations a given gene survived
	for gene in gene_count:
	    l.write(str(gene_count[gene]) + '\n') 
	    orgtotal += 1
	    if gene_count[gene] > max_gen:
		max_gen = gene_count[gene]

	l.write("Longest living gene (generations): " + str(max_gen) +'\n')
	l.write("Total number of successful genes: " + str(orgtotal) +'\n')
	l.close()	   



     
try:
    f = open("success.txt", 'r')
except:
    print "unable to open success.txt"

gene_count = {}
gen_op_sum = {}
n_per_gen = {}
id_vs_gen = {}
 
dict_builder()
ave_vs_generation()
lineage_vs_generations()
gene_lifespan()


 
