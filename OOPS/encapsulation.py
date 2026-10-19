# we use double underscore for make attributes and method private
# Encapsulation is an OOP concept in which data and methods are bundled together into a single class, and access to the data is controlled to protect it from unauthorized access.
# there are 3 types of access specifier public protected and private. by default it is in public mode protected doesnt work properly in python we use private
class Animal:
    __name = "lion"
    age = 22

    def __speak(self):
        print("hello I will roar")

obj = Animal()

print(obj.age)
obj.__speak()        #this is in private mode
print(obj.name)      #this will give error because name attribute is in private mode


