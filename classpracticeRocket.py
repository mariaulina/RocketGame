from random import randint
class Rocket():

    def __init__(self, name, x, y):
        self.name = name
        self.x=x
        self.y=y

    def MoveUp (self, h):
        if h> 1000000:
            raise RuntimeError ("You are far away from home. Please, stop moving and come back!")

        self.y += h
        print ('The rocket {} is on {} height!'.format (self.name, h))

    def MoveDown (self, h):
        if self.y == 0:
            raise RuntimeError ("Rocket is already on the Earth")

        if self.y <= h:
            self.y=0
            print ("Welcome home! {} just have landed!".format(self.name))

        else:
            self.y -= h
            print("Keep moving! {} is on {} height!".format(self.name, self.y))

def Flight (RocketName):
        h= randint(0, 100000)
        RocketName.MoveUp(h)
        h= randint(0, 100000)
        RocketName.MoveDown(h)


Apolo = Rocket('apolo', 0, 0)
Souz =Rocket('Souz', 0, 0)

Flight(Apolo)
Flight(Souz)
