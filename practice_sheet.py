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
# for n in range(2,11):
#     for i in range(2,n):
#         if n % i ==0:
#             break
#     else:
#         print(n)


# factorial
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)


#write a python program to toggle the case of each character in a string without using the built in swapcase() method
# ex PyThOn output pYtHoN

# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if ch.isupper():
#         result += ch.lower()
#     else:
#         result += ch.upper()

# print(result)


# st = "PyThOn"
# s = ""
# for i in range(len(st)):
#     if i%2==0:
#         s +=i.upper()
#     else:
#         s += i.lower
# print(s)


# reverse
# string = "Vikram"
# ans = ""
# for i in range(len(string)-1,-1,-1):
#     ans += string[i]
# print(ans)


# reverse without using index
# s = "hello"
# reverse = ""

# for ch in s:
#     reverse = ch + reverse

# print(reverse)


numbers = [10, 20, 30, 40, 50]
reversed = []

n = len(numbers) - 1

while n >= 0:
    reversed.append(numbers[n])
    n -= 1
print(reversed)



l = [1,2,3,4,5,6,7,9,8]
lar = float("-inf")
sec = float('-inf')
trd = float("-inf")
for i in range(len(l)):
    if l[i] > lar:
        sec = lar
        trd = sec
        lar = l[i]

    elif l[i]>sec and l[i] !=lar:
        sec = l[i] 

print("sec largest element is:",sec)
print("third largest element is:",trd)



# greates in a number
n = int(input("Enter a number: "))
greatest = float("-inf")
while n > 0:
    digit = n % 10
    if digit > greatest:
        greatest = digit

    n = n // 10

print("grtst numbr is:", greatest)


# move zeroes*********
# better approach
l = [1,2,0,9,0,3,0,5,0,0,-1]
ans = []
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i],l[j] = l[j],l[i]
        j+=1

print(l)

# brute force approach
# for i in l:
#     if i !=0:
#         ans.append(i)

# for j in l:
#     if j ==0:
#         ans.append(j)

# print(ans)



# armstrong number from 1 to 1000
for num in range(1, 1001):
    temp = str(num)
    power = len(temp)
    total = 0

    for i in temp:
        total += int(i) ** power

    if total == num:
        print(num)
        
