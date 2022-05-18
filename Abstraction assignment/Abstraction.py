from abc import ABC, abstractmethod


class Payment(ABC):
    #definition of a regular method
    def cost(self, amount):
        print("That costs {} USD".format(amount))
        
    #definition of an abstract method
    @abstractmethod
    def altCurrency(self, amount):
        pass

#child class of Payment
class canadaPurchase(Payment):
    #defines the abstract method from the Payment() parent class
    def altCurrency(self, amount):
        conversion = (amount * 1.29) #converts USD to CAD
        print("That costs {} CAD".format(conversion))


obj = canadaPurchase()  #Creating a new object from the canadaPurchase() child class
obj.cost(10)            #calling a parent method
obj.altCurrency(10)     #calling a child method
