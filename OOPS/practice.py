# Basic OOPs questions
# Q1. Student Class
# - Create a Student class.
# - Add attributes name, age, and marks.
# - Create three student objects.
# - Display the details of each student.
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print(f"student name is: {self.name}, age is: {self.age}, marks is: {self.marks}")


student1 = Student("Vikram" , 22 , 89)
student2 = Student("Pulkit" , 21 , 88)
student3 = Student("sawan" , 24 , 85)

student1.show_details()
student2.show_details()
student3.show_details()
print()


# Car Class
# - Create a Car class with attributes brand, model, and speed.
# - Add a method accelerate() that increases speed by 10.
# - Add a method brake() that decreases speed by 10.
# - Make sure speed never becomes negative.

class Car:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        print("speed increases by 10")
        self.speed += 10

    def brake(self):
            if self.speed >0:
                print("speed decreases by 10")
                self.speed-=10
            else:
                print("vehicle is not moving")

bmw = Car("BMW" , 2026 , 0)
bmw.accelerate()
print(bmw.speed)

bmw.brake()
print(bmw.speed)

bmw.brake()
print(bmw.speed)

print()


# Bank Account
# - Create a BankAccount class with account_holder and balance.
# - Implement deposit(amount).
# - Implement withdraw(amount).
# - Prevent withdrawals that exceed the available balance.

class BankAccount:
    def __init__(self,account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,deposit_amt):
        self.balance += deposit_amt
        print("money deposited")
        print("updated balance:",self.balance)

    def withdraw(self,withdraw_amt):
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt
            print("money withdraw successfully")
            print("available balance is:",self.balance)
        else:
            print("insufficiant balance")

vikram = BankAccount("Vikram" , 1000)
vikram.withdraw(500)
vikram.deposit(1000)
print()



# Q7. Inheritance — Vehicle

# Create a parent class Vehicle with:
# - brand
# - speed
# - A method display_info()
# Create two child classes:
# - Car
# - Bike
class Vehicle:
    def __init__(self,brand , speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"brand is: {self.brand} , speed is: {self.speed}")


class Car(Vehicle):
    def __init__(self, brand, speed,color):
        super().__init__(brand, speed)
        self.color = color

    def display_info(self):
            print(f"car brand is: {self.brand} , speed is: {self.speed} , color is:{self.color}")

class Bike(Vehicle):
    def __init__(self, brand, speed,tyre):
        super().__init__(brand, speed)
        self.tyre = tyre

    def display_info(self):
            print(f"car brand is: {self.brand} , speed is: {self.speed} , tyre is:{self.tyre}")


bmw = Car("BMW",50,"black")
bmw.display_info()
print()




# Method Overriding — Animals
# Create a parent class Animal with a method sound().
# Create child classes:
# - Dog
# - Cat
# - Cow
# Override sound() in each child class to return the appropriate sound.
    
class Animal:
     def sound(self):
          print("some sound")

class Dog(Animal):
     def sound(self):
          print("Dog barks")

class Cat(Animal):
     def sound(self):
          print("Cat makes sound meow meow")

class Cow(Animal):
     def sound(self):
          print("iam cow i make some sound")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()
print()


    
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Aman")

s1.school = "XYZ School"

print(s1.school)
print(s2.school)
print(Student.school)