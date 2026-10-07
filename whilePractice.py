# count positive and negative using while loop
# ls = [10,-2,-4,29,-2,10,22]
# pos = 0
# neg = 0
# i = 0
# count = 0
# while i < len(ls):
#     if ls[i] > 0:
#         pos +=1

#     else:
#         neg += i

#     i +=1

# print("positive numbers are: ",pos)
# print("negative numbers are: ",neg)

# sum of all numbers divisible by 3
# num = 1
# total = 0

# while num<=100:
#     if num % 3==0:
#          total += num

#     num +=1

# print(total)


# reverse number

# num = 12345
# reverse = 0

# while num>0:
#     digit = num%10
#     reverse = reverse*10 + digit
#     num =num//10

# print(reverse)


# num = 12345
# while num > 0:
#     d = num%10
#     print(d)
#     num//=10



# count digit in a number
# num = 123456
# count = 0
# while num > 0:
#     count+=1
#     num = num//10

# print(count)

# PALINDROME NUMBER
# num = 121
# reverse = 0
# temp = num

# while num>0:
#     digit = num%10
#     reverse = reverse*10 + digit
#     num =num//10

# if reverse == temp:
#     print("your number is a Palindrome number")

# else:
#     print("Your number is not a palindrome number")




num = 123456
largest = float("-inf")
while num > 0:
    d = num % 10
    if d > largest:
        largest = d

    num = num//10

print(largest)

