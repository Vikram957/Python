#1.Write a Python program to find the largest element in a tuple. 
# tp = (1,2,3,4,5,6,7,8,9)
# lar = float("-inf")
# for i in tp:
#     if i > lar:
#         lar = i
# print("largest element in tuple is:",lar)




#2.Write a Python program to find the smallest element in a tuple
# tp = (1,2,3,4,5,6,7,8,9)
# small = float("+inf")

# for i in tp:
#     if i < small:
#         small = i

# print("smallest element in tuple :",small)




#3.Write a Python program to find the sum of all elements in a tuple. 
# tp = (1,2,3,4,5,6,7,8,9)
# sum = 0
# for i in tp:
#     sum +=i

# print("sum of all elements in a tuple:",sum)


#4.Write a Python program to find the average of all elements in a tuple. 
# tp = (1,2,3,4,5,6,7,8,9)
# avg = 0
# sum = 0
# l = len(tp)
# for i in tp:
#     sum+=i
#     avg = sum//l

# print("sum of all elements in a tuple:",sum)
# print("avg of all elements in a tuple",avg)



#5 Write a Python program to count the occurrence of a specific element in a tuple.  
# tp = (1,2,3,4,5,6,7,8,9,4,4)
# tar = int(input("enter number:"))
# count = 0
# for i in tp:
#     if i == tar:
#         count+=1
# print("element",tar,"count is:",count)    


#6.Write a Python program to check whether an element exists in a tuple. 
# tp = (1,2,3,4,5,6,7,8,9)
# el = 90
# count = 0
# for i in tp:
#     if el in tp:
#         print("element exist in tuple")
#         break
# else:
#     print("not exist")



# 7.Write a Python program to reverse a tuple without using built-in methods. 
# tp = (1,2,3,4,5,6,7,8)
# rev = []
# for i in range(len(tp)-1,-1,-1):
#     rev.append(tp[i])

# print(tuple(rev))  

# without loop using slicing
# tp = (1,2,3,4,5,6)
# rev = tp[::-1]
# print(rev)



#8.Write a Python program to check whether a tuple is a palindrome. 
# tp = (1,2,1)
# rev = []
# for i in range(len(tp)-1,-1,-1):
#     rev.append(tp[i])

# print(tuple(rev))
# if tuple(rev) == tp:
#     print("your tuple is palindrome")
# else:
#     print("your tuple is not palindrome")


#9 Write a Python program to convert a tuple into a list. 
# tp = (1,2,3,4,5)
# print(list(tp))

# tp = (1, 2, 3, 4, 5)
# ls = []
# for i in tp:
#     ls.append(i)
# print(ls)


#10 Write a Python program to convert a list into a tuple. 
# ls = [1,2,3,4,5,6,7]
# print(tuple(ls))

# USING LOOP
# ls = [1, 2, 3, 4, 5, 6, 7]
# tp = ()
# for i in ls:
#     tp += (i,)
# print(tp)


# 43.	Write a Python program to find common elements between two tuples. 
# t = (1,2,3,4,5,6,7)
# u = (1,2,5,8,9,3,4,6,10)
# l = []
# for i in range(len(t)):
#     if t[i] in u:
#         l.append(t[i])
# print('common elements in two tuples are:',tuple(l))

# WITHOUT USING CONSTRUCTOR
# t = (1, 2, 3, 4, 5, 6, 7)
# u = (1, 2, 5, 8, 9)

# common = ()

# for i in t:
#     if i in u:
#         common = common + (i,)

# print("Common elements in two tuples are:", common)


# 44.Write a Python program to count the number of even and odd elements in a tuple. 
# t = (1,2,3,4,5,6,7,8,9)
# even = 0
# odd = 0
# for i in t:
#     if i % 2 == 0:
#         even +=1

#     else:
#         odd +=1
# print("even numbers",even)
# print("odd numbers ",odd)


# 45.Write a Python program to create a new tuple containing the squares of all elements in a tuple. 
# t = (1,2,3,4,5,6,7,8)
# sq = ()
# for i in t:
#     sq = sq+(i**2,)
# print(sq)


# 46.Write a Python program to find the length of a tuple without using the len() function. 
# t = (1,2,3,4,5,6,7,8,9)
# length = 0
# for i in t:
#     length =length+1
# print("length of tuple",length)



# 47.Write a Python program to merge two tuples into a single tuple
# t = (1,2,3,4,5,6)
# v = (1,2,6,7,8)
# res = ()
# for i in t:
#     res = res+(i,)

# for j in v:
#     res = res+(j,)

# print(res)




# 48.Write a Python program to find the frequency of each element in a tuple. 
# t = (1,2,3,2,4,5,6,7,4,8)
# for i in t:
#     count = 0
#     for j in t:
#         if i == j:
#             count+=1
#     print(i ,':', count)



# 49.Write a Python program to remove duplicate values from a tuple. 
# t = (1,2,3,4,5,6,3,5,7,2)
# res = ()
# for i in t:
#     if i not in res:
#         res = res+(i,)
# print(res)




# 50.Write a Python program to find the maximum and minimum values in a tuple
t = (1,2,3,4,5,6,7,8,9)
maxx = float("-inf")
minn = float("+inf")

for i in range(len(t)):
    if t[i] > maxx:
        maxx = t[i]
for j in range(len(t)):
    if t[j] < minn:
        minn = t[j]

print(f"maximum element is:{maxx}")
print(f"minimum element is:{minn}")


