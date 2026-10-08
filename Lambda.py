# lambda is basically a anonymous function

square = lambda x : x**2
print(square(4))

cube = lambda x: x**3
print("cube:",cube(4))

even = lambda x: True if x%2==0 else False
print("even:",even(4))


check = lambda x: "EVEN" if x%2==0 else "ODD"
print("your number is:",check(4))
print("your number is:",check(5))


sum = lambda a,b: a+b
print("sum of two number is:",sum(4,5))

max1 = lambda a,b : a if a>b else b
print("max number is:",max1(5,8))

Min = lambda a,b : a if a<b else b
print("Minimum number is:",Min(4,7))

# SORT IN ASCENDING ORDER
students = [("vikram", 150),("shyam",130),("aran",180)]   #it prioritize capital letters first 
ans = sorted(students, key = lambda x : x[0])
print(ans)  


# SORT IN REVERSE OR DESCENDING ORDER
students = [("vikram", 150),("shyam",130),("aran",180)]   #it prioritize capital letters first 
ans = sorted(students, key = lambda x : x[0],reverse=True)
print(ans)  



# CHECK POSITIVE NEGATIVE AND ZERO
check = lambda  x : "POSITIVE" if x > 0 else "NEGATIVE" if x<0 else "Zero"
print("your number is:",check(0))
print("your number is:",check(3))
print("your number is:",check(-2))


# Find length of string
length = lambda x : len(x)
print("length of string is:",length("VIKRAM"))

# convert a string in uppercase
upper = lambda x : x.upper()
print("your upper string is:",upper("viKRam"))

# convert a string in lowercase
lower = lambda x : x.lower()
print("your lower string is:",lower("ViKRam"))

# reverse a string
reverse = lambda x : x[::-1]
print("your reversed string is:",reverse("Vikram"))


# Palindrome check
palindrome = lambda x : "PALINDROME" if x.lower() == x[::-1] else "NOT PALINDROME"
print(palindrome("vikram"))
print("your palindrome number is:",palindrome("viv"))



# check wheter a string start with a vowel
check = lambda x : "TRUE" if x[0].lower() in "aeiou" else "FALSE"
print(check("Vikram"))


# sort a list in ascending order
# number = [10,40,20,30,60,100]
# ans = sorted(number,key = lambda x:x)
# print("your sorted list is:",ans)


# # SORT A LIST IN DESCENDING ORDER
# number = [10,40,20,30,60,100]
# ans = sorted(number,key = lambda x:x , reverse=True)
# print("your sorted list is:",ans)


# sort number in their last digit using lambda function
number = [11,43,24,35,64,97]
ans = sorted(number,key = lambda x:x%10)
print("your sorted list is:",ans)

# squared list
number = [1,2,3,4,5,6]
square = lambda x : x*x
ans = [square(x) for x in number]
print("squared list",ans)

# sort string according to their length using lambdaa function
string = ["Vikram","Shyam","kAran"]
ans = sorted(string,key = lambda x:len(x))
print("sorted str acc to length:",ans)

# sort string by their last character using lambda function
string = ["Vikram","Shyam","kAran"]
ans = sorted(string,key = lambda x:x[-1])
print("sort string by the last character:",ans)


# SORT TUPLE BY USING 2ND VALUES
tup = [
    ("vikram",20),("karan",200),("vijay",130)
]
ans = sorted(tup,key = lambda x:x[1])
print("sorted using 2nd values",ans)


# REVERSE 
tup = [
    ("vikram",20),("karan",200),("vijay",130)
]
ans = sorted(tup,key = lambda x:x[1],reverse=True)
print("sorted using 2nd values",ans)

# SORT A DICTIONARY BY VALUES 
data = {
    "A" : 50,
    "B" : 20,
    "C" : 30,
    "D" : 40
}
ans = sorted(data.items(), key = lambda x:x[1])
print("sorted dictionary according to values:",ans)



# find the key havinng maximum value in a dictionary
data = {
    "A" : 50,
    "B" : 20,
    "C" : 30,
    "D" : 40
}
ans = max(data.items(), key = lambda x:x[1])
print("maximum value in dictionary is:",ans)








# PRACTICE FROM PRACTICE SHEET*********************************************

# Basic Lambda Practice
# 1.Create a lambda function that takes one number and returns its square.
square = lambda x : x**2, print(square(3))

# 2.Create a lambda function that takes one number and returns its cube.
cube = lambda x : x **3, print(cube(4))

# 3. Create a lambda function that takes two numbers and returns their sum.
sum = lambda x,y : x+y 
print(sum(3,6))

# 4. Create a lambda function that takes two numbers and returns their larger value.
lar = lambda x,y : x if x > y else y
print(lar(3,6))

# 5. Create a lambda function that checks whether a number is even.
even = lambda x : True if x % 2 == 0 else False
print(even(66))



# Lambda with sorted()

# 6. Sort this list in ascending order using lambda
students = [("Vman", 80), ("Riya", 95), ("Rohan", 70)]
result = sorted(students , key = lambda x : x[0])
print(result)


# 7. Sort the same student list by marks in descending order.
students = [("Vman", 80), ("Riya", 95), ("Rohan", 70)]
result = sorted(students , key = lambda x : x[1])
print(result)


# 8. Sort the student list alphabetically by student name.
students = [("Vman", 80), ("Riya", 95), ("Rohan", 70)]
students.sort(key = lambda x : x[0])
print(students)


# 7. Sort the same student list by marks in descending order.
students = [("Vman", 80), ("Riya", 95), ("Rohan", 70)]
result = sorted(students , key = lambda x : x[1], reverse=True)
print(result)


# 8. Sort the student list alphabetically by student name.
students = [("Vman", 80), ("Riya", 95), ("Rohan", 70)]
students.sort(key = lambda x : x[0])
print(students)


# 9. Sort this list of tuples by the second value in descending order
data = [("A", 180), ("B", 95), ("C", 100)]
ans = sorted(data , key = lambda x : x[1] , reverse=True)
print(ans)


# 10. Sort a list of words according to their length using lambda
words = ["Python", "AI", "Machine", "Data", "Programming"]
ans = sorted(words , key = lambda x : len(x))
print(ans)



# Interview / Logic Practice

# 22. Write a lambda function to check whether a string starts with the letter 'A'.
ans = lambda x : True if x[0].upper()=="A" else "False"    #if you dont want small "a" then just remove .upper() function
print(ans("Vikram"))
print(ans("Akash"))
print(ans("akash"))


#23 Write a lambda function that returns 'Pass' if marks are 40 or more, otherwise 'Fail'.
marks = lambda x : "Pass" if x >= 40 else "Fail"
print(marks(33))
print(marks(43))


# Given employees = [("Aman", 25000), ("Riya", 35000), ("Rohan", 30000)], sort employees by salary from highest to lowest.

employees = [("Aman", 25000), ("Riya", 35000), ("Rohan", 30000)]
result = sorted(employees , key = lambda x : x[1], reverse = True)
print(result)


# 25.Explain the difference between a normal def function and a lambda function with one example of each.
# In Python, both def and lambda are used to create functions. 
# The main difference is that def is used to create regular functions, while lambda is used to create small, anonymous functions with a single expression.

# Normal function using def
def sum(a,b):
    return a+b
print(sum(3,5))

# lambda function
sum = lambda x,y : x+y
print(sum(3,5))


# Challenge
# 26. Given products = [("Laptop", 55000), ("Mouse", 800), ("Keyboard", 1500), ("Monitor", 12000)], sort the products by price from highest to lowest using sorted() and lambda.

products = [("Laptop", 55000), ("Mouse", 800), ("Keyboard", 1500), ("Monitor", 12000)]
ans = sorted(products,key = lambda x : x[1],reverse=True)
print(ans)