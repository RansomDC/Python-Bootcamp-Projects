

#parent class
class Organism:
    name = "unknown"
    species = "unknown"
    legs = None     #None is a special data type that is not any data type.
    arms = None
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}\n".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

#Child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homo sapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape"
        return msg

class Dog(Organism):
    name = 'spot'
    species = 'Canis familiaris'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and licks your face"
        return msg

class Bacterium(Organism):
    name = 'Strep'
    species = 'streptococcus pyogenes'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def infect(self):
        msg = "\nWhen in the lungs of another organism, cause sickness"
        return msg


if __name__ == '__main__':
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.infect())

