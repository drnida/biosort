from create_gene import translategene  

#Creates and returns the string containign the header for an organism's C++ file
def writeheader(genesequence, pressure): 
    header = '/*'+genesequence+'*/\n#include <iostream>\nusing namespace std;\n#include "../biosort.h"\nint Pressure = 0;\nextern int s;\nextern int v;\nint count=0;\nint * a;\nextern int i;\n'\
            '\nint main(int argc,char ** argv)\n{\ns=argc-1;\na=new int[s];\nbuild(argv);' 
    return header 
 

#Creates the string for the whole organism C++ file then writes it out
def writebody(fileout, genesequence, pressure): 
    writeout = writeheader(genesequence, pressure) #writeout holds the string to write to the file
    writeout += 'do{' 
    tok = translategene(genesequence) #tok holds the list of tokens for the mutable fields of the file
    num = len(tok)/19 #num is the amount of genes in the sequence 
    counter = tok[-1] #counter is the number of operations done by a single sequence (not counting operations performed within an if statement)
    del tok[-1] #Removes the counter

    #For each gene, adds the code for running that gene to the write out string
    for j in range(num): 
            i = j*19 
            writeout += '\ni=m('+tok[1+i]+tok[2+i]+tok[3+i]+'\n);\nv=a[i];\nif(('+tok[4+i]+' m('+tok[5+i]+' '+tok[6+i]+' '+tok[7+i]+\
            '\n)'+tok[8+i]+')'+tok[9+i]+'\n('+tok[10+i]+' m('+tok[11+i]+' '+tok[12+i]+' '+tok[13+i]+\
            '\n)'+tok[14+i]+'))\n{\n'+tok[15+i]+'(m('+tok[16+i]+' '+tok[17+i]+' '+tok[18+i]+'\n'+\
            '));}\n'; 

    #Adds the code for the end of the file
    writeout +='count +='+counter+';}while(!is_sorted()&& count<Pressure);\ncout << count << endl;\ndelete [] a;\nreturn 0;}' 
    
    #Writes out the string to the file
    fileout.write(writeout) 
    return 

#Driver for writing out the file
def writec(folder, org, pressure):
    filename = folder+'organism.cpp' 
    fileout = open(filename, 'w+') 
    writebody(fileout, org.genesequence, pressure) 
    fileout.close() 
    return

