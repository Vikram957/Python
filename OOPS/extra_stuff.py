# DECORATORS
# def my_decorator(say_hello):
#     def wrapper():
#         print("before function run")
#         say_hello()
#         print("after functn run")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("hello")

# say_hello()



# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__} executed in {end-start:.5f} seconds")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(5)

# slow_function()


def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def greet():
    return "hello students"

print(greet())



