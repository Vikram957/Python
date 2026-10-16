# import calendar
# year = int(input("enter year:"))
# month = int(input("enter month:"))

# cal = calendar.month(year,month)
# print(cal)


# Write a Python program to swap two variables without temp variable.
# a = int(input('enter value of a:'))
# b = int(input("enter value of b:"))
# a,b = b,a
# print("value of a is:",a)
# print("value of b is:",b)



# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
for n in range(2,11):
    for i in range(2,n):
        if n % i ==0:
            break
    else:
        print(n)


# factorial
n = 5
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)


