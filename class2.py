a = int(input("enter your 1st number: "))
b = float(input("enter your 2nd number: "))
c = input("enter your value: ")

print(type(a))
print(type(b))
print(type(c))

print(f"addition of a and b is: {a+b}")
print()
print(f"subtraction of a and b is: {a-b}")
print()
print(f"multiplication of a and b is:{a*b}")
print()
print(f"power of a acc to b is: {a**b}")
print()
print(f"a modulo b is: {a%b}")

age = int(input("enter your age:"))

if age>=18:
    print("you can vote")

else:
    print("you cant vote")

num1 = int(input("enter your 1st number: "))
num2 = int(input("enter your 2nd number: "))
num3 = int(input("enter your 3rd number: "))

if num1>num2 and num1>num3:
    print("number 1 is greater which is: ",num1)

elif num2>num1 and num2>num3:
    print("number 2 is greater which is: ",num2)

elif num1==num2==num3:
    print("all no are equal")

else:
    print(f"number 3 is greater which is:{num3}")


CALCULATOR
a = int(input("enter your 1st number:"))
b = int(input("enter your 2nd number:"))
op = input("enter your operator")

if op == "+":
    print(a+b)

elif op == "-":
    print(a-b)

elif op == "*":
    print(a*b)

elif op =="/":
    print(a/b)

elif op == "%":
    print(a%b)

elif op =="**":
    print(a**b)

else:
    print("please enter valid operator")


CHECK EVEN ODD
num = int(input("plz enter your number:"))

if num % 2 ==0:
    print("your number is even")

else:
    print("your number is odd")



MARKS
marks = int(input("plz enter your marks"))
citizen = input("enter your citizenship")

if marks >=90 and marks<=100:
    print("grade A+",marks)

    if citizen =="Indian":
        print("you are indian:") 

elif marks>=70 and marks<90:
    print("grade A")

elif marks>=50 and marks<70:
    print("grade B")

elif marks >= 33 and marks<50:
    print("grade C")

elif marks>0 and marks<33:
    print("failed")

else:
    print("plz enter positive marks")



SIGNAL
signal = input("enter signal color:")

if signal == 'red' or signal == 'RED':
    print("Stop")

elif signal =='green' or signal =='GREEN':
    print("You can go")

elif signal == 'yellow' or signal =='YELLOW':
    print("you have to ready ")

else:
    print("plz enter valid signal color")


TICKET PRICE ACCORDING TO AGE
age = int(input("enter your age: "))

if age>=1 and age<=5:
    print("ticket is free for baby")

elif age>5 and age<=18:
    print(" you are teen so,half ticket price")

elif age>18 and age<=60:
    print(" you are adult so,you have to pay full amount")

else:
    print("ticket is discounted for old peoples")


USER AUTHENTICATION
userName = 'Vikram'
passWord = '1234'
userName1 = input("enter username:")
passWord2 = str(input("enter password:"))

if userName == userName1 and passWord == passWord2:
    print("Access Granted")

else:
    print("Access Denied")

CHECK LEAP YEAR

year = int(input("enter year:"))

if year % 4==0 and year % 100 !=0 or year % 400==0:
    print("your year is leap year")

else:
    print("your year is not a leap year")



Write a Python program to check whether a string starts with vowel or not.

ch = input("enter character you want to check vowel or not: ")

if ch == 'A' or ch == 'a' or ch =='e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch =='O' or ch =='u' or ch =='U':
    print("you have entered a vowel")

else:
    print("you have entered consonant")


Calculate income tax for the input income by adhering to the Indian rules.

income = int(input("enter your income: "))
if income == 0:
    print("you are unemployed you cant pay tax,first find job and then pay tax (:")

elif income <=250000 and income>0:
    print("your income is less than 250000 so,zero percent tax applied on you:")

elif income >250000 and income<500000:
    print("your income is more than 250000 so,10% tax applied on you")

elif income >500000 and income <1000000:
    print("your income is more than 250000 so, 20% tax applied on you")

elif income >1000000 and income < 1800000:
    print("your income is more than 1000000 so,30% tax applied on you")

elif income < 0:
    print("income cant be negative, please enter valid income ")

else:
    print("your salay is more than 1800000 so,32% tax applied on you")



WAP to display the last digit of a number. (Don’t use indexing for this) 
a = int(input("enter number:"))
if a<10:
    print(a)

else:
    a %=10
    print(a)
    

WAP to print the day based on the number input.

day = int(input("enter day:"))

if day == 1:
    print("day 1 is monday")

elif day ==2:
    print("day 2 is tuesday")

elif day == 3:
    print("day 3 is wednesday")

elif day == 4:
    print("day 4 is thursday")

elif day == 5:
    print("day 5 is friday")

elif day == 6:
    print("day 6 is saturday")

elif day == 7:
    print("day 7 is sunday")

else:
    print("please enter number between 1 to 7")


WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user.
Using percentage print which grade the student has scored.

maths = int(input("enter maths marks:"))
english = int(input("enter enlish marks:"))
physics= int(input("enter hindi marks:"))
chem = int(input("enter chemistry marks:"))

obtMarks = maths + english + physics + chem
totalMarks = 400

per = (obtMarks/totalMarks)*100

if per >90:
    print("you got A+ grade")

elif per>=75 and per<90:
    print("you got A grade")

elif per >= 50 and per <75:
    print("you got B grade")

elif per >33 and per<50:
    print("you got c grade")

else:
    print("you have scored less than 33 percent that means you failed ")


WAP to check using the sides of a triangle to tell if it is equilateral triangle or not.
a = int(input("enter side a:"))
b = int(input("enter side b:"))
c = int(input("enter side c:"))

if a == b == c:
    print("your triangle is equilateral")

else:
    print("your triangle is not equilateral")


USERNAME AND PASSWORD AUTHENTICATION
userName = "Vikram"
passWord = "1234"

if userName == "Vikram":
    if passWord =="123":
        print("login successfully")
    else:
        print("password is incorrect")
else:
    print("username is incorrect")


BALANCE WITHDRAW PROGRAM

balance = 10000
withdraw = 10000

if balance > 0:
    if withdraw <=balance:
        print("withdraw successfully")
        balance = balance - withdraw
        print(f"total amt left in acc is {balance}")

    else:
        print("withdraw amt is grater than available balance")

else:
    print("Balance is not sufficiant")


balance = 10000
deposit = 200

if deposit > 0:
    print("deposit is successfull")
    balance += deposit
    print(f"total amout after deposit is:{balance}")

else:
    print("deposit cant be 0 or negative")


balance = 10000
print(" 1. for deposit")
print("2. for withdrawal")


choice = int(input("enter choice 1 or 2:"))

if choice ==1:
     deposit = float(input("enter amt to deposit:"))
     if deposit > 0:
          balance +=deposit
          print("total amt after deposit" , balance)
          
     else:
         print("not enough deposit amt")
         

elif choice == 2:
     withdraw = float(input("enter withdrawal amount: "))
     if withdraw > 0:
          if withdraw <= balance:
               print("withdrawal successfully (:")
               balance -= withdraw
               print("remaining amt is" , balance)

          else:
               print("withdrawal amt is greater")

else:
     print("invalid choice")




# TRAIN TICKET BOOK

age = int(input("enter your age"))
ticket = input("do you want to book ticket? yes or no")

if ticket=='yes':
     if age>=18:
          print("ticket is booked for adult")
     else:
          print("ticket is booked for child")


else:
     print("ticket is cancelled")


BANK LOAN ELIGIBILITY 
salary = float(input("enter your monthly salary:"))
creditScore = int(input("enter your credit score:"))

if salary>= 25000:
     if creditScore >= 700:
          print("loan approved")
     else:
          print("credit score is too low")

else:
     print("salary is too low")




