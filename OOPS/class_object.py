# only class
class Factory:
    a = 12  #Attribute
    # Method
    def hello():
        print("hello sir") 

print(Factory.a)
Factory.hello()
print()



# object***
class Factory:
    a = "iam attribute"
    def hello(s):
        print("hello iam method")

# object
obj = Factory()     #obj becomes an object who can access anything inside the class till now
print(obj.a)
obj2 = Factory()
obj2.hello()   
print()

# class object and constructor
class Factory:
    def __init__(self,Brand,material,pocket,zip):         #self is a reference/Address to the current object of a class. It is used to access the object's attributes and methods.
        self.Brand = Brand
        self.material = material
        self.pocket = pocket
        self.zip = zip

    def show(self):
        print(self.Brand, self.material ,self.pocket,self.zip)

reebok = Factory("reebok" , "Nylon" , 3,3)
nike = Factory("Nike" ,"Leather" , 4,5 )

print(reebok.material)
nike.show()



# INSTANCE ATTRIBUTES AND CLASS ATTRIBUTES**************************
class Animal:
    gender = "male"    #class attribute is attribute created inside a class without using self keyword

    def __init__(self,name,age):
        self.name = name       #instance attributes is a attribute creating using self keyword
        self.age  = age

    def speak(self):         #A method using a self keyword as parameter is instance method
        print("iam instance method")

    @classmethod
    def clas_method(cls):        #class method used the @classmethod decorator and do not rely on instance specific data
        print(f"{cls.gender} is your gender")    #here cls parameter target the class location no object location like self does
    
    @staticmethod      #In static method we doesnt pass any parameter but we used @staticmethod decorator
    def hello():
        print("hello iam static method")


lion = Animal("lion" , 11)
lion.speak()       #instance method calling
lion.clas_method()    #class method 
lion.hello()     #static method
print()




# make a student registration system ask name , age , number , blood group
class Student:
    def __init__(self,name,age,number,bloodgroup):
        self.name = name
        self.age = age
        self.number = number
        self.bloodgroup = bloodgroup

    def show_details(self):
        print(f"name: {self.name} \nage: {self.age}\nnumber: {self.number}\nbloodgroup: {self.bloodgroup}")


Student1 = Student("vikram",22,983283384,"b+")
Student2 = Student("Abhishek",27,384483,"a+")

Student1.show_details()





