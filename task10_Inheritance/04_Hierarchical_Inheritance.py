# Hierarchical Inheritance

# Base Class
class Animal:
    def animal(self):
        print("I'm an Animal")

# Derived Class
class Cat(Animal):
    def cat(self):
        print("I'm a cat Meow Meow!")

# Derived Class
class Dog(Animal):
    def dog(self):
        print("I'm a dog Brak Bark!")


cat = Cat()
dog = Dog()

cat.animal()
cat.cat()


dog.animal()
dog.dog()
