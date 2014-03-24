#Folders to hold breeders
class bfolder:
    def __init__(self, pa, num_kids, org):
        self.path = pa #The path name of this folder ie habitat/breeder1/
        self.org = org #Organism currently occupying this folder
        self.progeny = [] #Folder list holding all of this breeder's progeny
        for x in range(num_kids):
            self.progeny.append(pfolder(pa+"progeny"+str(x+1)+"/")) 

#Folders to hold progeny
class pfolder:
    def __init__(self, pa):
        self.path = pa #The path name of this folder ie habitat/breeder1/progeny1/
        self.org = None #Organism currently occupying this folder

#folders to hold randoms
class rfolder:
    def __init__(self, pa):
        self.path = pa #The path name of this folder ie habitat/random1/
        self.org = None #Organism currently occupying this folder
