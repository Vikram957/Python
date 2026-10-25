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
