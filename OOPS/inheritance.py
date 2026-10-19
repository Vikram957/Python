class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"your name is {self.name} \nyour age is {self.age}") 

class Human(Animal):
    def __init__(self, name, age,number,bloodgroup):      #super() is used to access the parent classes methods, commonly used in inheritance
        super().__init__(name, age)      #whenever we call the super function it calls the parent class here Animal
        self.number = number
        self.bloodgroup = bloodgroup

    def show(self):       #here both method names are same here concept of polymorphism one name many forms
        print(f"your name is {self.name}\n your age is: {self.age} \n your number is:{self.number} \n your bloodgroup is: {self.bloodgroup}")



# multilevel inheritance
class Robot(Human):
    def __init__(self, name, age, number, bloodgroup,imei):
        super().__init__(name, age, number, bloodgroup)
        self.imei = imei

    def show(self):       #here both method names are same here concept of polymorphism one name many forms
            print(f"your name is {self.name}\n your age is: {self.age} \n your number is:{self.number} \n your bloodgroup is: {self.bloodgroup} \n imei number is:{self.imei}")


obj = Animal("lion" , 12)
obj1 = Human("vikram",22,38738,"b+")
obj2 = Robot("peter" , 1,1234,"N/A",343234)

obj1.show()
print()
obj2.show()


