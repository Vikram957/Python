a = [1,2,3,4,5,6]
cube = map(lambda x : x**3,a)
print(list(cube))

list1 = [1,2,3,4,5,6,7,8,9]
even = filter(lambda x : x % 2==0,list1)
print(list(even))



from functools import reduce
even = lambda x,y : max(x,y)
print(reduce(even,[3,5,4,23,34,45]))


names = ["Mangesh" , "Sachin" , "Rahul"]
list(map(str.upper,names))


