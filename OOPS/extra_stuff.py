# DECORATORS
def my_decorator(say_hello):
    def wrapper():
        print("before function run")
        say_hello()
        print("after functn run")
    return wrapper
@my_decorator
def say_hello():
    print("hello")

say_hello()