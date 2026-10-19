class Animal:
    name = "Lion"

    def speak(self):
        print("hello I Roar")

class Bird:
    name = "Sparrow"

    def speak(self):
        print("Hello I tweet")

obj = Animal()
obj2 = Bird()

# here you can see same funcn or method name but different behaviour this is polymorphism
obj.speak()
obj2.speak()
print()


# method over riding
class Animal:
    def speak(self):
        print("hello i roar")

class Human(Animal):
    def speak(self):        #it override upper method 
        print("hello iam vikram")

obj = Human()
obj.speak()
