# 3.Find the longest palindrome word in a sentence.
# sentence = "madam, level and malayalam are palindrome words in this sentence"
# words = sentence.split()
# longest = ""
# for word in words:
#     word = word.strip("!,.?")
#     if word == word[::-1]:
#         if len(word) > len(longest):
#             longest = word
# print("longest palindrome word is:",longest)





# 5.Write a Python program to determine whether the second string is an anagram of the first string. Two strings are anagrams if they contain the same characters with the same frequencies, but possibly in a different order.
# s1 = "listen" 
# s2 = "silene"
# anagram = True

# if len(s1) != len(s2):
#     print("your str is not a anagram")
    
# else:
#     anagram = True

# for i in s1:
#     if s1.count(i) != s2.count(i):
#         anagram = False

# if anagram:
#     print("str is anagram")
# else:
#     print("str is not a anagram")




# Write a Python program to toggle the case of each character in a string without using the built-in swapcase() method.
# s = input("Enter your string: ")
# result = ""
# for i in s:
#     if i.isupper():
#         result += i.lower()
#     elif i.islower():
#         result += i.upper()
#     else:
#         result += i

# print(result)



# Write a Python program to find the first non-repeating element in a list.
# l = [1,2,3,4,5,1,2,3,7,8,9,0]

# for i in range(len(l)):
#     if l.count(l[i]) == 1:
#      print("first non repeating element:",l[i])
#      break


# 3.Write a Python program to check whether a given string is a palindrome
# s = input("Enter your string: ")
# rev = ""

# for i in range(len(s) - 1, -1, -1):
#     rev += s[i]

# if rev == s:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# with slicing
# s = input("Enter your string: ")

# rev = s[::-1]

# if rev == s:
#     print("Palindrome")
# else:
#     print("Not palindrome")




# 4	Write a Python program to read a sentence and print the longest word in that sentence.
# s = "my name is vikram."
# ans = s.split()
# longest = ""

# for i in ans:
#     i = i.strip("!,.?")
#     if len(i) > len(longest):
#         longest = i
# print(longest)




# 1.	Write a Python program to print the following star pattern: 
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

# n = int(input("Enter number: "))

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()




# n = int(input("Enter number: "))

# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()


# n = int(input("enter no:"))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end='')
#     print()


# sort dict using values
# d = {
#     "a": 5,
#     "b": 2,
#     "c": 8,
#     "d": 1
# }

# items = list(d.items())

# for i in range(len(items)):
#     for j in range(i + 1, len(items)):
#         if items[i][1] > items[j][1]:
#             items[i], items[j] = items[j], items[i]

# print(dict(items))


# 6 sort dictionary in ascending order by values. 
# d = {
#     "a": 5,
#     "b": 2,
#     "c": 8,
#     "d": 1
#  }

# ans = list(d.items())
# for i in range(len(ans)):
#     for j in range(i+1,len(ans)):
#         if ans[i][1] > ans[j][1]:
#             ans[i],ans[j] = ans[j],ans[i]
# print(ans)



# Reverse a dictionary (swap keys and values). 
# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# new = {}

# for key, value in d.items():
#     new[value] = key

# print(new)
    