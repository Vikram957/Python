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
