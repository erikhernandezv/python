"""Programacion Orientada a Objetos en Python
"""

class Person(object):
    nArm = 0
    Nleg = 0
    hair = True
    cHair = "Default"
    hangry = 0
    
    def __init__( self ):
        self.nArm = 2
        self.nLeg = 2
    
    def sleep():
        pass
    
    def eat(self):
        self.hangry=5


class Man(Person):
    name="Default"
    sex="M"
    
    def changeName( self, nameSelf ):
        self.name = nameSelf
    
class Woman ( Person ):
    name="Defecto"
    sex="F"
    
erik = Man()
erik.eat()

print( erik.hangry )