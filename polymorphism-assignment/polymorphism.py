

#creates the parent class
class Emulatedvideogame():
    graphics = "advanced"
    releaseDate = ""
    startButton = "Enter"

    def begin(self):
        #gives the most basic command you may need to do to begin a game session on an emulated game
        return print("to start, press {}".format(self.startButton))

#creates a child class
class Metalgear(Emulatedvideogame):
    genre: "Action"
    startButton = "Start"
    numberOfWeapons = 12
    characterChoices = 2

    def begin(self):
        #adjusts what you need to do for the game Metalgear to start an emulated session
        return print("to start, hold {}".format(self.startButton))

#creates a child class
class Forza(Emulatedvideogame):
    genre: "Simulator"
    startButton = "X"
    numberOfCars = 25
    dynamicLighting = True

    def begin(self):
        #adjusts what you need to do for the game Forza to start an emulated session
        return print("to start, rub your head while lightly caressing {}".format(self.startButton))
    






if __name__ == '__main__':
    #three calls to the various classes and child classes to call the polymorphic begin() method.
    test = Emulatedvideogame()
    test.begin()

    fart = Metalgear()
    fart.begin()

    toots = Forza()
    toots.begin()
