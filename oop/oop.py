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
        super().__init__(breed, color)# super() method calls the parent constructor in our case  Animal
        self.name = name
    def __str__(self):
        return f"{self.name},{self.breed},{self.color}"
    
dog1 = Dog("JACK", "ROT", "Black")
print(dog1)