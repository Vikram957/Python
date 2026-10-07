# QUESTION 1:Take a number from the user and check whether it is positive or negative.
num = int(input("enter your number:"))
if num > 0:
    print("your number is positive")

else:
    print("your number is negative")

# question 2: Check whether a number is even or odd using %.
num = int(input("enter your number to check even or odd:"))
if num % 2 == 0:
    print("your number is even")

else:
    print("your numbr is odd")

# QUESTION 3: TAKE TWO NUMBERS AND PRINT THE GREATER NUMBER.
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))

if a > b:
    print(f"a={a} is greater number than b={b}")

else:
    print(f"b={b} is greater numbr than a={a}")

# QUESTION 4: TAKE AGE AS INPUT AND CHECK WHETHER THE PERSON CAN VOTE OR NOT.
age = int(input("enter your age:"))
if age >= 18:
    print("you can vote")

else:
    print("you cannot vote")

# Check whether a number is divisible by 5.
num = int(input("enter your number:"))
if num % 5 == 0:
    print("your number is divisible by 5")
else:   
    print("your number is not divisible by 5")


# Take three numbers and print the largest number.
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:"))

if a > b and a > c:
    print(f"a={a} is the largest number")
elif b > a and b > c:
    print(f"b={b} is the largest number")
else:
    print(f"c={c} is the largest number")

# Take two numbers and one operator (+, -, *, /) from the user and perform the operation using if-else.
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
op = input("enter oprator like (+,-,*,/):")

if op == "+":
    print(a+b)

elif op =="-":
    print(a-b)

elif op == "*":
    print(a*b)

elif op =="/":
    print(a/b)

else:
    print("invalid operator")








# IF -ELIF -ELSE PRACTICE QUESTIONS **************************************************************************************************************************************8

# QUESTION 1: POSITIVE, NEGATIVE, OR ZERO
num = int(input("enter your number:"))

if num == 0:
    print("your number is zero")

elif num < 0:
    print("your number is negative")

else:
    print("your number is positive")


# QUESTION 2: STUDENT GRADE CHECKER
marks = int(input("enter your marks:"))

if marks >=90:
    print("Grade A")

elif marks >=75 and marks <=89:
    print("Grade B")

elif marks >=50 and marks <=74:
    print("Grade C")

else:
    print("Fail")


# Question 3: TRAFFIC SIGNAL SYSTEM
signal = input("enter signal color:")

if signal == 'red' or signal =='RED':
    print("Stop")

elif signal == 'yellow' or signal == 'YELLOW':
    print("Get Ready")

elif signal == 'green' or signal == 'GREEN':
    print("GO")

else:
    print("Invalid Signal")


# QUESTION 4: DAY TYPE CHECKER**************
day = input("enter day:")

if day == 'saturday' or day =='SATURDAY' or day == 'sunday' or day == 'SUNDAY':
    print(f"{day} is Weekend")

elif day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    print(f"{day} is Weekday")

else:
    print("Invalid day")


# QUESTION 5: TEMPERATURE CHECKER***********
tem = int(input("enter temperature:"))

if tem > 35:
    print("Hot")

elif tem >= 20 and tem<=35:
    print("Normal")

else:
    print("Cold")


# QUESTION 6: MOBILE BATTERY STATUS*************
battery = int(input("enter battery level:"))

if battery > 80:
    print("Fully Charged")

elif battery >= 30 and battery <= 80:
    print("Battery Normal")
else:
    print("Low")

# QUESTION 8: FRUIT AVAILABILITY************
fruit = input("enter fruit name:")

if fruit == 'apple' or fruit == 'banana':
    print("Available")

elif fruit == 'mango':
    print("Out of stock")

else:
    print("Fruit not found")


# QUESTION 9: ELECTRICITY BILL CATEGORY
units = int(input("enter used electricity units:"))

if units <100:
    print("Low Usage")

elif units >=100 and units <= 300:
    print("Medium Usage")

else:
    print("high Usage")





# Nested If-Else Practice Questions*****************************************************************************************************************************
age = int(input("enter age:"))
citizen = input("are you a citizen of our country? yes or no:")

if age >= 18 and citizen == 'yes':
    print("you can vote")

else:
    print("you cant vote")

if age>=18:
    if citizen=='yes':
        print("you can vote")

    else:
        print("you are not citizen of our country so, you cannot vote ")

else:
    print("your age is below 18 so,you cannot vote")


# QUESTION 2: SCHOOL STUDENT PASS OR NOT*********************************
marks = int(input("enter marks:"))
attendance = int(input("enter attendance percentage:"))

if marks >= 35:
    if attendance > 75:
        print("Student Passed")

    else:
        print("Low attendance")

else:
    print("Student Failed")


# QUESTION 3: ATM MACHINE MONEY WITHDRAW
balance = 1000
lock = 1234
pin = int(input("enter your pin:"))

if pin == lock:
    withdrawal = int(input("enter withdrawal amount:"))
    if withdrawal <= balance:
        print("withdrawal is successfuly")
        balance = balance - withdrawal
        print(f"available balance after withdrawal:{balance}")
    else:
        print("amount is greater than available balance so,withdrawal failed")

else:
    print("pin is incorrect")






# QUESTION 4: A cinema hall has the following rules for allowing entry to an adult movie:
age = int(input("enter your age:"))

if age >= 18:
    proof = input("do you have valid id proof? yes or no:")

    if proof == 'yes':
        print("allowed to enter")

    else:
        print("Valid id proof is required")

else:
    print("you are underage")







# QUESTION 5: ONLINE SHOPPING WEBSITE DISCOUNT RULES
purchase = int(input("enter purchased amount:"))
discount =0

if purchase > 1000:
    premium = input("are you a premium customer? yes or no:")
    if premium=='yes':
        print("congatulations,you got 20percent discount")
        discount = purchase * (20/100)
        purchase -= discount
        print(f"final price after discount is:{purchase}")


    elif premium == 'no':
        print("Become a premium member for discount")
    else:
        print("premium customer or not? say only yes or no")

else:
    print("purchase more to get discount")






# QUESTION 6: MOBILE PHONE SECURITY RULES***********************
pas = 123
password = int(input("enter password:"))

if password== pas:
    fingerPrint = input("fingerprint match? yes or no:")
    if fingerPrint=='yes':
        print("Phone Unlocked")
    else:
        print("Fingerprint not matched")

else:
    print("Invalid password")






# QUESTION 7:CRICKET ACADEMY PLAYER SELECTION RULES
test = input("fitness test pass or not? yes or no:")

if test == 'yes':
    score = int(input("how much you have scored:"))
    if score > 50:
        print(f"you have scored {score} runs so you got Selected")

    else:
        print(f"you have scored only {score} runs so you are not selected")

else:
    print("Fitness test failed")