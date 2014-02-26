
class bfolder:
    def __init__(self, pa, num_kids, org):
        self.path = pa
        self.org = org
        self.progeny = []
        for x in range(num_kids):
            self.progeny.append(pfolder(pa+"progeny"+str(x+1)+"/")) 

class pfolder:
    def __init__(self, pa):
        self.path = pa
        self.org = None

