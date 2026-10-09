# In Python, map(), filter(), and reduce() are functional programming tools that help you process collections like lists and tuples with less code.

# map() — Apply a function to every element
# Use map() when you want to perform the same operation on every element of a list.

#1. Use lambda and map() to double every number in: 
numbers = [1, 2, 3, 4, 5]
ans = map(lambda x : x*2,numbers)
print(list(ans))


# 12. Use lambda and map() to find the square of every number in a list.
number = [1,2,3,4,5]
square = map(lambda x : x**2,number)
print(list(square))


# 13. Convert this list of names to uppercase using lambda and map(): 
names = ["aman", "riya", "rohan"]
result = map(lambda x : x.upper(),names)
print(list(result))


# 14. Add 10 to every number using lambda and map().
numbers = [1,2,3,4,5]
result = map(lambda x : x + 10,numbers)
print(list(result))


# Lambda with filter()

# filter() — Select elements based on a condition
# Use filter() when you want to keep only the elements that satisfy a condition.

# 15. Use lambda and filter() to extract even numbers from a list.
numbers = [1,2,3,4,5,6,7,8,9]
even = filter(lambda x : x % 2 == 0 , numbers)
print(list(even))


# 16. Use lambda and filter() to extract numbers greater than 50.
number = [1,56,54,45,77,99,2,4,2,88,78]
result = filter(lambda x : x > 50,number)
print(list(result))


# 17. Extract names having more than 5 characters using lambda and filter().
names = ["vikram","Singh","Pulkit","Jaiswal","Sawan","Meena"]
result = filter(lambda x : len(x) > 5,names)
print(list(result))


# 18. From marks = [45, 78, 32, 90, 66, 25], extract students' passing marks (marks >= 40).
marks = [45,78,32,90,66,25]
passed_Students = filter(lambda x :x >= 40,marks)
print(list(passed_Students))



# from functools import reduce
from functools import reduce
even = lambda x,y : max(x,y)
print(reduce(even,[3,5,4,23,34,45]))
