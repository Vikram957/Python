# Level 1 – Basic
# 1.Create a list containing the squares of numbers from 1 to 10.
list1 = [i**2 for i in range(1,11)]
print(list1)

# 2.Create a list containing the cubes of numbers from 1 to 10.
list1 = [i**3 for i in range(1,11)]
print(list1)

# 3.Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a list containing only the even numbers.
numbers = [1,2,3,4,5,6,7,8,9,10]
list1 = [i for i in numbers if i % 2 == 0]
print(list1)


# 4.Create a list containing only the odd numbers from 1 to 20.
list1 = [i for i in range(1,21) if i % 2 != 0]
print(list1)


# 5.Convert all strings to uppercase: names = ['mangesh', 'rahul', 'priya', 'amit'].
names = ['mangesh', 'rahul', 'priya', 'amit']
ans = [i.upper() for i in names]
print(ans)


# 6.Given words = ['python', 'data', 'science', 'machine', 'learning'], create a list containing the length of each word.
words = ['python', 'data', 'science', 'machine', 'learning']
ans = [("length of:",i,len(i))for i in words]
print(ans)


# 7.Create a list of numbers from 1 to 20 that are divisible by 3.
list1 = [i for i in range(1,21) if i % 3 == 0]
print(list1)


# 8.Given numbers = [10, 15, 20, 25, 30], add 5 to every element using list comprehension.
numbers = [10,15,20,25,30]
list1 = [i+5 for i in numbers]
print(list1)




# Level 2 – Conditions
# 9.Given numbers = [12, 5, 8, 21, 30, 17, 4], create a list containing numbers greater than 10.
numbers = [12, 5, 8, 21, 30, 17, 4]
ans = [i for i in numbers if i > 10]
print(ans)


# 10.	Create a list containing numbers between 10 and 50 that are divisible by 5.
list1 = [i for i in range(10,51) if i % 5 == 0]
print(list1)


# 11.	Given numbers = [-5, 3, -2, 8, -1, 10], create a list containing only positive numbers
numbers = [-5, 3, -2, 8, -1, 10]
ans = [i for i in numbers if i > 0]
print(ans)



# 12.Replace every negative number with 0: numbers = [10, -5, 7, -2, 8, -9]. Expected: [10, 0, 7, 0, 8, 0].
numbers = [10, -5, 7, -2, 8, -9]
list1 = [i if i > 0 else 0 for i in numbers ]
print(list1)



# 13.Given marks = [35, 78, 92, 41, 29, 67, 88], create a list containing 'Pass' for marks >= 40 and 'Fail' otherwise.
marks = [35, 78, 92, 41, 29, 67, 88]
list1 = [(i,"PASS") if i >= 40 else (i,"FAIL")for i in marks]
print(list1)



# 14.Create a list of numbers from 1 to 100 that are divisible by both 3 and 5.
list1 = [i for i in range(1,101) if i % 3 == 0 and i % 5 == 0]
print(list1)





# Level 3 – Strings
# 15.	Given words = ['apple', 'banana', 'kiwi', 'orange', 'cat'], create a list containing words whose length is greater than 5.
words = ['apple', 'banana', 'kiwi', 'orange', 'cat']
list1 = [i for i in words if len(i) > 5]
print(list1)



# 16.Given words = ['Python', 'Java', 'C', 'JavaScript', 'Ruby'], create a list containing words that contain the letter 'a'.
words = ['Python', 'Java', 'C', 'JavaScript', 'Ruby']
list1 = [i for i in words if "a" in i]
print(list1)



# 17.Convert only lowercase words to uppercase: words = ['python', 'DATA', 'science', 'AI', 'machine'].
words = ['python', 'DATA', 'science', 'AI', 'machine']
list1 = [i.upper() if i.islower() else i for i in words]
print(list1)


# 18.Given names = ['Amit', 'Rahul', 'Ankit', 'Priya', 'Ravi'], create a list containing names that start with 'A'
names = ['Amit', 'Rahul', 'Ankit', 'Priya', 'Ravi']
list1 = [i for i in names if i[0] == "A"]
print(list1)


# 19.Given words = ['level', 'python', 'madam', 'data', 'radar'], create a list containing only palindrome words.
words = ['level', 'python', 'madam', 'data', 'radar']
list1 = [i for i in words if i == i[::-1]]
print(list1)






# Level 4 – Interview-Based
# 20.Find all numbers between 1 and 100 that are perfect squares.
import math
perfect_square = [i for i in range(1,101) if math.isqrt(i)**2 == i]
print(perfect_square)


