
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, end = " ")
        print(self.lastname)

fname = input("Enter first name: ")
lname = input("Enter last name: ")

obj = Person(fname,lname)
obj.printname()
