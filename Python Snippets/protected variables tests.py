class Private():
    #initializing a class that has a private variable with the value of "stuff"
    #this __init__ method will be run every time the Private() class is instantiated
    def __init__(self):
        self.__privateVar = "Stuff"

    def editVar(self, value):
        self.__privateVar = value

    def printVar(self):
        print(self.__privateVar)

priv = Private()        #creating an object from the Private() class
priv.printVar()         #calling a method to print a private variable
priv.editVar("junk")    #calling a method to edit a private variable
priv.printVar()         #calling a method to print the (now changed) value of a private variable


print("================")


class Protected():
    def __init__(self):
        self._protectedVar = "cake"


obj = Protected()           #creating an object from the Protected() class
print(obj._protectedVar)    #printing the value of a protected variable
obj._protectedVar = "pies"  #changing the value of a protected variable
print(obj._protectedVar)    #printing the changed value of a protected variable
