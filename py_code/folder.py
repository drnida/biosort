
class bfolder:
    __init__(self, pa, num_kids, org):
        self.path = pa
        self.org = org
        self.progeny = []
        for x in range(num_kids):
            self.progeny.append(new pfolder(pa+"/progeny/"+x)) 

class pfolder:
    __init__(self, pa):
        self.path = pa
        self.org = None

