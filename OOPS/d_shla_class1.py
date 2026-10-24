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
# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Lion(Animal):
#     def __init__(self, name, age,gender):
#         super().__init__(name, age)
#         self.gender = gender
#     def show(self):
#         print(f"name is:{self.name} age is:{self.age} gender is:{self.gender}")

# class Tiger(Lion):
#     def __init__(self, name, age, gender,weight):
#         super().__init__(name, age, gender)
#         self.weight = weight

#     def show(self):
#         print(f"name is:{self.name} age is:{self.age} gender is:{self.gender} weight is:{self.weight}")



    

# lion = Lion("Lion",10,"Male")
# lion.show()
# print()

# tiger = Tiger("Tiger",11,"male",240)
# tiger.show()

# # encapsultaion
# class Car:
#     __color = "Red"
#     brand = "Tata"

#     def show(self):
#         print(self.color,self.brand)

# car = Car()
# print(car.brand)
# car.color()


class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} engine started")

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)
        self.color = color

    def start_engine(self):
        print(f"{self.brand} engine started")

class Bike(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"{self.brand} engine started")

car = Car("BMW","Black")
bike = Bike("Ninja",2025)

bike.start_engine()
car.start_engine()


# ATM PROGRAM
class BANK:
    def __init__(self, initial_amt):
        self.__balance = initial_amt


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposit amount is: {amount}. total balance is: {self.__balance}")

        else:
            print("deposit must be positive")

    def withdraw(self,amount):
        if amount > 0 and self.__balance >=amount:
            self.__balance -= amount
            print(f"withdraw amount is: {amount}. new balance {self.__balance}")

        else:
            print("invalid withdraw amount")

    def get_balance(self):
        return self.__balance



account1 = BANK(10000)

account1.deposit(1000)

account1.get_balance()

account1.withdraw(2000)

account1.get_balance()




# POLYMORPHISM*********************************
# Compile time polymorphism  
# class Calculator:
#     def add(self,a,b,c):       #function overloading
#         return a + b +c

#     def add(self,a,b):
#         return a + b

# calc = Calculator()
# calc.add(2,2)
# calc.add(2,2,2)




# USING KWARG*******************************
class Calculator1:
    def add(self, *numbers):
        return sum(numbers)

    def add(self,*numbers):
        return sum(numbers)

calc1 = Calculator1()
calc1.add(1,2,3)
calc1.add(1,2,3,4)
calc1.add(1,2)



# RUNTIME POLYMORPHISM  /// METHOD OVER-RIDING
class Animal:
    def speak(self):
        print("hello i roar")

class Human(Animal):
    def speak(self):        #it override upper method 
        print("hello iam vikram")

obj = Human()
obj.speak()

obj1 = Animal()
obj1.speak()



# method overloading
# dunder method// magic methods
class Number:
    def __init__(self,value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

a = Number(40)
b = Number(30)

print(b - a)






# DUCK TYPING**************************
class Bird:
    def fly(self):
        print("bird is flying")

class Airplane:
    def fly(self):
        print("airplane is flying")

class Fish:
    def swim(self):
        print("fish is swimming in the water")


for i in Bird() , Airplane() , Fish():
    i.fly()




class Google_pay:
    def Pay(self,amt):
        print("paid using google pay",amt)


class phone_pay:
    def Pay(self,amt):
        print("paid using phone pay",amt)


class paytm:
    def Pay(self,amt):
        print("paid using paytm",amt)


def check_out(payement):
    payement.pay(1000)


check_out(Google_pay())
check_out(phone_pay())
check_out(paytm())







class Email:
    def send(self,msg):
        print("Email :",msg)

class SMS:
    def send(self,msg):
        print("SMS :",msg)

class WhatsApp:
    def send(self,msg):
        print("WhatsApp:",msg)

def notify(service):
    service.send("ordered placed")


notify(Email())
notify(WhatsApp())
notify(SMS())




# MRO*************
class A:
    def show(self):
        print("i'am class A method")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d = D()
d.show()
print(D.mro())



# static method
class Student:

    @staticmethod
    def add(a,b):
        return a + b

s1 = Student()
print(s1.add())



# class Method
class Student1:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student1.show_school()



class Student2:
    school = "abcd"

    @classmethod
    def change_school(cls,name):
        cls.school = name

Student2.change_school("XYZ School")
print(Student2.school)










