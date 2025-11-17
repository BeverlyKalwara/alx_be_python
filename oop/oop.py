#inheritance
class Animal:
    #class attributes bound to the class
    def __init__(self, breed, color):#constructor
        #instance atributes - bound to the attribute
        self.breed = breed
        self.color = color
    def __str__(self):
        return f"{self.breed}, {self.color}"
    
class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(breed, color)# super() method calls the parent constructor in our case  Animal and inherits everything
        self.name = name
    def __str__(self):
        return f"{self.name},{self.breed},{self.color}"
    #def __init__(self, name, breed):
    #    Animal.__init__(self, breed, color="unknown")# calling animal directly inherits only a specific attribute, and in this case breed alone
    #    self.name = name
    #def __str__(self):
    #    return f"{self.name},{self.breed}"
#dog1= Dog("JACK", "ROT")
#  
dog2 = Dog("JACK", "ROT", "Black")
print(dog2)