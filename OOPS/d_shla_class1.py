# class Student:
#     def __init__(self,name,marks):   #constructor
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(f"name: {self.name}, marks: {self.marks}")
# info = Student("vikram",88)
# info.display()




# class Car:
#     def __init__(self, Brand,Model):
#         self.Brand = Brand
#         self.Model = Model

#     def display(self):
#         print(f"Brand={self.Brand}, Model= {self.Model}")

# car = Car("Tesla",2026)
# car.display()
# print()



# # INHERITANCE***********************
# class Animal:       #parent class
#     def speak(self):
#         return "Some sound"
# class Dog(Animal):      #child class
#     def eat(self):
#         return "eat food"
# dog = Dog()
# print(dog.speak())
# print(dog.eat())
# print()


# # SINGLE INHERITANCE
# class Animal:       #parent class
#     def speak(self):
#         return "Some sound"
# class Dog(Animal):      #child class
#     def eat(self):
#         return "eat food"
# dog = Dog()
# print(dog.speak())
# print(dog.eat())
# print()



# # multiple Inheritance
# # one class can derived from multiple base class

# class Father:
#     def skills_father(self):
#         print("Father: Driving")
# class Mother:
#     def skills_mother(self):
#         print('Mother: Cooking')

# class Child(Father, Mother):
#     def skills_child(self):
#         print("Child: Programming")

# C = Child()
# C.skills_father()
# C.skills_mother()
# C.skills_child()
# print()

# # MULTILEVEL Inheritance
# # a child become parent for another child class
# class Grandfather:
#     def property(self):
#         print("Grandfather's Property")

# class Father(Grandfather):
#     def bussiness(self):
#         print("Father's Bussiness")
# class Son(Father):
#     def job(self):
#         print("son's Job")

# s = Son()
# s.property()
# s.bussiness()
# s.job()
# print()



# # Heirarchichal Inheritance
# class Vehicle:
#     def start(self):
#         print("Vehicle Start")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
# class Bike(Vehicle):
#     def ride(self):
#         print("bike riding")

# car = Car()
# bike = Bike()

# car.start()
# car.drive()
# print()

# bike.start()
# bike.ride()
# print()


# # Hybrid Inheritance********8
# class Grandparent:
#     def grandparent_method(self):
#         print("grandparent method")

# class Parent1(Grandparent):
#     def parent1_method(self):
#         print("parent1 method")

# class Parent2(Grandparent):
#     def parent2_method(self):
#         print("Parent2 method")

# class Son(Parent1,Parent2):
#     def son_property(self):
#         print("child method")

# s = Son()

# s.grandparent_method()
# s.son_property()
# s.parent1_method()




# # question practice
# class Student:
#     name = "vikram"
#     age = 12

#     def show(self):
#         print(f"name is:{self.name} your age is:{self.age}")

# obj = Student()
# print(obj.name)
# obj.show()
# print()

# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color

#     def show_car(self):
#         print(f"brand is {self.brand} and color is {self.color}")

# bmw = Car("BMW","Black")
# audi = Car("Audi","white")

# bmw.show_car()
# audi.show_car()



# practice
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Lion(Animal):
    def __init__(self, name, age,gender):
        super().__init__(name, age)
        self.gender = gender
    def show(self):
        print(f"name is:{self.name} age is:{self.age} gender is:{self.gender}")

class Tiger(Lion):
    def __init__(self, name, age, gender,weight):
        super().__init__(name, age, gender)
        self.weight = weight

    def show(self):
        print(f"name is:{self.name} age is:{self.age} gender is:{self.gender} weight is:{self.weight}")



    

lion = Lion("Lion",10,"Male")
lion.show()
print()

tiger = Tiger("Tiger",11,"male",240)
tiger.show()


