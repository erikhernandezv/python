"""Programacion Orientada a Objetos en Python
"""

class Person(object):
    """A continuacion se encuentran una variables de clase"""    
    nArm = 0
    Nleg = 0
    hair = True
    cHair = "Default"
    hangry = 0
    
    """Construcytor de la clase"""
    def __init__( self ):
        """Variables de instancia"""
        self.nArm = 2
        self.nLeg = 2
    
    """Metodo que sirve para personalizacion la creacion de las instancias de esta clase."""
    def __new__(cls):
        print("Method new()...")
        return super().__new__(cls)
    
    """Definimos un metodo como propiedad"""
    @property
    def area( self ):
        return 3.161516*(10**2)
    
    """Metodo de clase"""
    @classmethod
    def sleep(cls):
        print("This is a method of class...")
        
    """Metodo estatico"""
    @staticmethod
    def jump():
        print("This is a method of class...")
    
    """Metodo de instancia"""
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

people = Person()
people.sleep()
print("\n")

print(people.area)

class Perro(object):
    def avanzar(self):
        print("Avanzar en 4 patas...")
        
class Perico(object):
    def avanzar(self):
        print("Avanzar en 2 patas...")
        
def mover(animal):
    animal.avanzar()
    
dog = Perro()
perico = Perico()
