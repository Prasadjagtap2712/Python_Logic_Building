class GrandFather:
    relation = "GRANDFATHER"
    def __init__(self):
        self.Gname = "Baban"
        self.Gage = 72

class Father:
    relation = "FATHER"
    def __init__(self):
        self.Fname = "Sahadev"
        self.Fage = 52

class Child(GrandFather,Father):
    relation = "CHILD"
    def __init__(self):
        GrandFather.__init__(self)
        Father.__init__(self)
        self.Cname = "Prasad"
        self.Cage = 22
    
    def dispChild(self):
        print("Grandfather Name: ",self.Gname)
        print("Grandfater Age: ",self.Gage)
        print("Father Name: ",self.Fname)
        print("Father Age : ",self.Fage)
        print("Child Name: ",self.Cname)
        print("Child Age: ",self.Cage)
obj = Child()
obj.dispChild()
