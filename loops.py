# use continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# use pass
for i in range(1,11):
    if i == 5:
        pass

# use break
for i in range(1,11):
    if i == 6:
        break
            

            


# data = [437,79,46,394,33,42,9,10]
# for i in data:
#     if i == 100:
#         print("number found",i)
#         break

#     else:
#         print("number not found!")

# list = [1,2,3,4,5,6,7]
# max = 0
# for i in list:
#     if i > max:
#         max = i

# print("largest numbr in list is:",max)



# list = [1,2,3,4,5,6,7]
# min= float("+inf")
# for i in list:
#     if i < min:
#         min = i

# print("smallest numbr in list is:",min)


# list = [1,2,3,4,4,5,6,7,7,6,10]
# list = [1,2,6,5]
# largest = float("-inf")
# secLargest = float("-inf")
# for i in list:
#     if i > largest:
#         secLargest = largest
#         largest = i

#     elif i > secLargest and i != largest:
#         secLargest = i

# print("largest number in list is:", largest)
# print("second largest numbr is list is:", secLargest)


# list =[1,2,6,5]
# smallest = float("+inf")
# secSmallest = float("+inf")
# for i in list:
#     if i<smallest:
#         secSmallest = smallest
#         smallest = i

#     elif i< secSmallest and i!= smallest:
#         secSmallest = i

# print(smallest)
# print(secSmallest)



# list = [1,2,3,4,5,6]
# for i in range(len(list)):
#     print(list[i])

# list = [1,2,3,4,5,6]
# for i in range(len(list)-1,-1,-1):
#     print(list[i])

# text = "ABCDEFGHIJK"
# count = 0

# for ch in text:
#     if ch in "aeiouAEIOU":
#         count += 1

# print(count)




# s = input()

# for i in range(len(s)):
#     count = 0

#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count += 1

#     if count == 1:
#         print(s[i])
 

# total = 0
# i = 1
# while i<=5:
#     total += i
#     i += 1

# print(total)


# odd numbers
# i = 1
# count = 0
# while i<=20:
#     print(i)
#     count +=1
#     i += 2

# print(f"total odd numbers between 1 to 20 is:{count}")



# i = 0
# count = 0
# while i<=20:
#     print(i)
#     i += 2
#     count +=1

# print(f"total even number count between 1 to 20 is: {count}")

# i = 0
# ecount = 0
# odcount = 0
# while i <= 20:
#     if i%2==0:
#         ecount += 1

#     else:
#         odcount+=1

#     i+=1

# print(f"even count between 0 to 20 is:{ecount}")
# print(f"off count between 0 to 20 is:{odcount}")


# num = 12345
# total = 0

# while num>0:
#     digit = num%10
#     total = total + digit
#     num //=10

# print(total)



# num = 1234567
# largest = float("-inf")
# count = 0

# while num > 0:
#     num %= 10
#     if num>largest:
#         largest = num
#         count+=1

#     num //=10
# print(largest)
# print(count)



# num = int(input("enter number:"))
# fact = 1
# while num > 0:
#     fact *= num
#     num-=1
# print(fact)


# ARMSTRONG NUMBER
# num = int(input("enter number:"))
# length = len(str(num))
# total=0
# temp = num
# while num > 0:
#     digit = num % 10
#     total+= digit**length
#     num//=10

# if temp == total:
#     print(f"{total} is a armstrong number")

# else:
#     print("not a armstrong number")
# print(total)




# PALINDROME NUMBER 
# num = int(input("enter number:"))
# rev = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp//=10

# if num == rev:
#     print("your number is a palindrome number")

# else:
#     print("your number is not a palindrome number")



# 1.	Print all multiples of 7 from 1 to 100. 
# for i in range(7,101,7):
#     print(i)

# i = 7
# while i <=100:
#     print(i)
#     i+=7


# 2.Count the number of positive and negative numbers in a list.

# numbers = [10, -5, 20, -8, -2, 15]
# positive = 0
# negative = 0

# for num in numbers:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1

# print("Positive numbers:", positive)
# print("Negative numbers:", negative)



# 3.Print only numbers greater than 100 from a list. 
# ls = [100,20,300,36,150,260]
# for i in ls:
#     if i > 100:
#         print(i)

    
4.#Find the sum of numbers divisible by 3 between 1 and 100. 
# total = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         total += i

# print(total)


#5.	Print all numbers between 1 and 100 that are divisible by 2 but not by 5. 
# for i in range(1, 101):
#     if i % 2 == 0 and i % 5 != 0:
#         print(i)


#6.	Find the largest even number in a list. 
# numbers = [15, 22, 7, 40, 13, 18]
# largest = float("-inf")
# for num in numbers:
#     if num % 2 == 0 and num > largest:
#         largest = num

# print(largest)

#7 find the smallest odd number in a list
# numbers = [15, 22, 7, 40, 13, 18]
# smallest = float("+inf")
# for i in numbers:
#     if i!=0 and i<smallest:
#         smallest = i

# print(smallest)



# 8.Count how many elements are divisible by both 2 and 3 in a list. 
# count = 0
# numbers = [15, 22, 7, 40, 13, 18,30]
# for i in numbers:
#     if i%2==0 and i%3==0:
#         count+=1
#         print(f"total elements in a list which is divisible by 2 and 3 is:{i}")

# print(f"total number of count is:{count}")



# 9.Find the sum of all positive numbers in a list. 
# ls = [1,4,8,9,-2,40,-3,-44]
# ans = 0
# for i in ls:
#     if i > 0:
#         ans +=i

# print(ans)


# 10.	Print the index and value of each element in a list.
# ls = [2,3,54,6,7,8]
# for i in range(len(ls)):
#     print(f" At index:{i}: value is:{ls[i]}") 


# 11.Find the frequency of a particular number in a list. 
# ls = [1, 2, 3, 2, 4, 2, 5, 2]
# num = int(input("Enter the number:"))
# count = 0
# for i in ls:
#     if i == num:
#         count += 1

# print(count)


# 13.Create a new list containing only odd numbers from another list. 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd = []
# for i in numbers:
#     if i % 2 != 0:
#         odd.append(i)

# print(odd)


# 14.	Check whether a given number exists in a list. 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = int(input("enter your number:"))

# for i in numbers:
#     if i == num:
#         print("your number is exists in a list")
#         break

# else:
#     print("your number is not exists in a list")



#15 Find the common elements between two lists. 
list =[1,2,3,4,5,6,7,8]
list1 = [2,4,6,999,9]

for i in list:
    if i in list1:
        print(i)
    
    
    
