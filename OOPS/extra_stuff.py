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


# def uppercase(func):
#     def wrapper():
#         for i in range(3):
#             func()
            
#     return wrapper


# @uppercase
# def greet():
#      print("hello students")


# greet()




def check_access(func):
    def wrapper():
        role = input("enter your role:")
        if role.lower() == "admin":
            func()
        else:
            print("Access Denied")
    return wrapper
        


@check_access
def dashboard():
    print("welcome to dashboard")



dashboard()