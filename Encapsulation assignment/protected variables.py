class Private():
    #initializing a class that has a private variable with the value of "stuff"
    #this __init__ method will be run every time the Private() class is instantiated
    def __init__(self):
        self.__privateVar = "Stuff"
        self._protectedVar = "cake"

    def editVar(self, value):
        self.__privateVar = value

    def printVar(self):
        print(self.__privateVar)

priv = Private()        #creating an object from the Private() class
priv.printVar()         #calling a method to print a private variable
priv.editVar("junk")    #calling a method to edit a private variable
priv.printVar()         #calling a method to print the (now changed) value of a private variable

print("================")

print(priv._protectedVar)       #printing the value of a protected variable
priv._protectedVar = "pies"     #changing the value of a protected variable
print(priv._protectedVar)       #printing the changed value of a protected variable
