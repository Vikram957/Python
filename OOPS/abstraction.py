# in python we use the abc module to define abstract classes and methods

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod    
    def sound(self):  #if we make abstract method in parent class then it is must to have this method in all child class which is derived from this class other wise it will give error
        pass

class Dog(Animal):
    def sound(self):
        print("i make woof")
    def hello(self):
        print('iam dog and i woof')

class Cat(Animal):
    def sound(self):
        print("hello i make meow sound")

obj = Dog()
obj.sound()