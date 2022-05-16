

class Insect:
        lengthmm = 0
        color = ''
        genus = 'Unknown'
        species = 'Unknown'

        def __init__(self, lengthmm, color, genus, species):
            self.lengthmm = lengthmm
            self.color = color
            self.genus = genus
            self.species = species

        def reproduce(self):
            return print("Lay eggs in a safe place so that they can hatch later")












if __name__ == '__main__':
    
    lunaMoth = Insect(178,'Green','Actias','luna')
    lunaMoth.reproduce()
