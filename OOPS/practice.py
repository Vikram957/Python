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
        