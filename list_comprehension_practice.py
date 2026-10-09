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


# 22.	Given numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6], create a list containing only unique values using list comprehension.
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
result = [i for i in numbers if numbers.count(i) <=1]
print(result)


# 23.	Given numbers = [1, 2, 3, 4, 5], create [1, 4, 9, 16, 25] without using a normal for loop.
numbers = [1,2,3,4,5]
square = [i**2 for i in numbers]
print(square)


# 24.	Given words = ['python', 'java', 'cpp', 'javascript'], create a list containing the first character of every word.
words = ['python', 'java', 'cpp', 'javascript']
ans = [i[0] for i in words]
print(ans)


# 25.	Given numbers = [10, 15, 20, 25, 30], create ['Even', 'Odd', 'Even', 'Odd', 'Even'].
numbers = [10, 15, 20, 25, 30]
check = ["EVEN" if i % 2 == 0 else "ODD"for i in numbers]
print(check)


# 26.Given numbers = [1, 2, 3, 4, 5, 6], create a list where even numbers are multiplied by 2 and odd numbers are multiplied by 3. Expected: [3, 4, 9, 8, 15, 12].
numbers = [1, 2, 3, 4, 5, 6]
result = [i*2 if i % 2 == 0 else i*3 for i in numbers]
print(result)


# 27.Given words = ['apple', 'banana', 'cat', 'dog', 'elephant'], create a list containing the lengths of only those words whose length is greater than 3.
words = ['apple', 'banana', 'cat', 'dog', 'elephant']
result = [i for i in words if len(i) > 3]
print(result)



# 28.Find all numbers from 1 to 50 whose square is greater than 500.
result = [i for i in range(1,51) if i**2 > 500]
print(result)



# 29.Given numbers = [2, 5, 8, 11, 14, 17], create a list containing 'Even' or 'Odd' based on each number.
numbers = [2, 5, 8, 11, 14, 17]
result = ["EVEN" if i % 2 == 0 else "ODD" for i in numbers]
print(result)



# 30.Challenge: Given sentence = 'Python is easy to learn', create a list containing the length of each word. Expected: [6, 2, 4, 2, 5].
sentence = 'Python is easy to learn'
result = [len(i) for i in sentence.split()]
print(result)






# Interview Challenge – No Normal for Loop

# 31.Create a list of squares of even numbers from 1 to 20.
even_square = [i**2 for i in range(1,21) if i % 2 == 0]
print(even_square)


# 32.Create a list of words having more than 5 characters.
words = ['python', 'cat', 'science', 'AI', 'machine', 'data']
result = [i for i in words if len(i) > 5]
print(result)


# 33.Create a list of numbers divisible by 3 or 5 from 1 to 100.
ans = [i for i in range(1,101) if i % 3 == 0 or i % 5 == 0]
print(ans)


# 34.Replace negative numbers with their absolute values.
numbers = [1,2,-3,-5,6,-7,8]
ans = [abs(i) for i in numbers]
print(ans)


# 35.Find all vowels from a string using list comprehension.
text = "Hello Python Programming"
result = [i for i in text if i.lower() in "aeiou"]
print(result)


# 37.Extract numbers greater than 50 from a list.
numbers = [20,30,50,60,70,80]
result = [i for i in numbers if i > 50]
print(result)



# 38.	Convert a list of Celsius temperatures to Fahrenheit.
celcius = [20,30,40,50,60]
fah = [(i*9/5)+32 for i in celcius]
print(fah)



# 39.	Create a list of (number, square) tuples.
numbers = [1,2,3,4,5,6,7]
square = [(i,i**2)for i in numbers]
print(square)



# 40.	Find common elements between two lists.
l1 = [1,2,3,4,5,6]
l2 = [1,2,3,7,8,9]
common = [i for i in l1 if i in l2]
print(common)


