from create_gene import translategene  


def writeheader(genesequence, pressure): 
    header = '/*'+genesequence+'*/\n#include <iostream>\nusing namespace std;\n#include "../biosort.h"\nint Pressure = '+str(pressure)+';\nextern int s;\nextern int v;\nint count=0;\nint * a;\nextern int i;\n'\
            '\nint main(int argc,char ** argv)\n{\ns=argc-1;\na=new int[s];\nbuild(argv);' 
    return header 
 

def writebody(organism, genesequence, pressure): 
    writeout = writeheader(genesequence, pressure) 
    writeout += 'do{' 
    tok = translategene(genesequence) 
    num = len(tok)/19 
    length = len(tok) 
    counter = tok[length-1] 
    del tok[-1] 
    for j in range(num): 
            i = j*19 
            writeout += '\ni=m('+tok[1+i]+tok[2+i]+tok[3+i]+'\n);\nv=a[i];\nif(('+tok[4+i]+' m('+tok[5+i]+' '+tok[6+i]+' '+tok[7+i]+\
            '\n)'+tok[8+i]+')'+tok[9+i]+'\n('+tok[10+i]+' m('+tok[11+i]+' '+tok[12+i]+' '+tok[13+i]+\
            '\n)'+tok[14+i]+'))\n{\n'+tok[15+i]+'(m('+tok[16+i]+' '+tok[17+i]+' '+tok[18+i]+'\n'+\
            '));}\n'; 
    writeout +='count +='+counter+';}while(!is_sorted()&& count<Pressure);\ncout << count << endl;\ndelete [] a;\nreturn 0;}' 
    organism.write(writeout) 
    return 

def writec(folder, org, pressure):
    filename = folder+'organism.cpp' 
    organism = open(filename, 'w+') 
    writebody(organism, org.genesequence, pressure) 
    organism.close() 
    return

