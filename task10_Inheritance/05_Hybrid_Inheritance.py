# Hybrid Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating.")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        print(f"{self.name} is walking.")

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)
        
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)
        
    def meow(self):
        print(f"{self.name} is meowing.")

d = Dog("Buddy")
c = Cat("Kitty")

d.eat()
d.walk()
d.bark()

c.eat()
c.walk()
c.meow()
