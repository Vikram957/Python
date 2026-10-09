# s = {1,2,3,4,5,6,6,4}
# print(s)
# print(type(s))

# s.add(79)
# s.update([23,44])
# s.remove(300)   #it removes the element but if element is not present in set then it gives error
# s.discard(400)  #it removes the element but it doesnt give the error if element not found
# print(len(s))
# print(s.pop())

# print(s)
# se = set()     #empty set

# UNION OF 3 SET
# set1 = {1,2,3,4}
# set2 = {1,2,4,5,6}
# set3 = {4,5,6,7,8}

# print(set1.union(set2,set3))    # union operator is |
# print(set1 | set2)        # union by using operator
# print(set)

# print(set1 & set2)   #intersection by operator
# print(set1.intersection(set2,set3))  #intersection by using method

# x = {'banana','grapes'}
# y = {'apple','mango'}
# z = x.isdisjoint(y)     #it basically checks if any common element present in both set then returns false other wise it return true
# print(z)

# t = x.symmetric_difference(y)
# print(x ^ y)    #by operator
# print(t)


# fru = {'apple', 'mango','grapes'}
# fru.clear()
# print(fru)


# x = {1,2,3,4,5,6}
# y = {1,2,3}
# z = y.issubset(x)

# print(z)


# x = {1,2,3,4,5,6}
# y = {1,2,3}
# # z = x.issuperset(y)
# # print(z)
# x.intersection_update(y)
# print(x)

# x = {1,2,3,4,5,6}
# y = {1,2,3}
# print(x - y)       #difference by using operator
# print(x.difference(y)) #by using function



# 6.Write a Python program to check whether an element exists in a set. 
# s = {1,2,3,4,5,6}
# el = 9
# for i in s:
#     if el in s:
#         print("exist")
#         break
# else:
#     print("not exist")



# 7.Write a Python program to find the length of a set. 
# s = {1,2,3,4,5,6,7,8}
# length = 0
# for i in s:
#     length +=1
# print(f"length of set is:{length}")


# 8.Write a Python program to iterate through all elements of a set. 
# s = {1,2,3,4,5,6,7,8}
# for i in s:
#     print(i , end =" ")




# 9.Write a Python program to find the maximum and minimum elements in a set. 
# s = {1,2,3,4,5,6,7,8,9}
# maxx = float("-inf")
# minn = float("+inf")
# for i in s:
#     if i >maxx:
#         maxx = i
# for j in s:
#     if j < minn:
#         minn = j

# print("max:",maxx)
# print("min:",minn)


# 10.Write a Python program to convert a list into a set. 
# l = [1,2,3,4,5,6,7,8,9]
# s = set(l)
# print(s)


# Duplicate-Related Questions
# 11.Write a Python program to remove duplicates from a list using a set. 
# l = [1,2,1,2,3,4,5,3,6,7,8]
# s = set(l)
# print(s)

# 12.Write a Python program to check whether all elements in a list are unique. 
# l = [1,2,3,4,5,6,7,8,3]
# s = set(l)
# if len(l) == len(s):
#     print("all elements are unique")
# else:
#     print("not unique")



# 13.Write a Python program to find duplicate elements in a list using sets. 
# ls = [1,2,3,4,5,2,3,7,8,7]
# s = set()
# dup = set()
# for i in ls:
#     if i in s:
#         dup.add(i)
#     else:
#         s.add(i)

# print(dup)


# 14.Write a Python program to count the number of unique elements in a list. 
# l = [1,2,3,4,5,6,3,4,7,8]
# s = set()
# dup = set()
# count = 0
# for i in l:
#     if i not in s:
#         s.add(i)
#         count+=1
#     else:
#         dup.add(i)
# print(dup)
# print(count)


# 15.Write a Python program to find the first repeated element in a list. 
# l = [1,2,3,4,4,5,6,7,5]
# s = set()
# rep = set()
# for i in l:
#     if i not in s:
#         s.add(i)
#     else:
#         rep.add(i)
#         break
# print(rep)


# Union, Intersection, Difference
# 16.Write a Python program to find the union of two sets. 
# s = {1,2,3,4}
# s1 = {2,3,6,7,8}

# ans = set()
# ans = s | s1
# print(ans)


# 17.Write a Python program to find the intersection of two sets. 
# s = {1,2,3,4,5}
# s1 = {2,3,4,7,8}
# print(s & s1)

# 18.Write a Python program to find the difference between two sets. 
# s = {1,2,3,4,5,6,7}
# s1 = {2,3,4,5,9,8}
# ans = s - s1
# print(ans)


# 19.Write a Python program to find the symmetric difference between two sets. 
# s = {1,2,3,4,5}
# s1 = {2,3,4,6,7,8}
# ans = s ^ s1
# print(ans)


# 20.Write a Python program to check whether two sets are equal.
# s = {1,2,3,4}
# s1 = {1,2,4,3}

# if s == s1:
#     print("sets are equal")
# else:
#     print("not equal")


# 21.Write a Python program to find common elements between two lists using sets. 
# l = [1,2,3,4,5,6,7,8]
# l1 = [2,3,5,9,10]
# common = set(l) & set(l1)
# print(common)


# 22.Write a Python program to find uncommon elements between two lists using sets. 
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# l1 = [2, 3, 5, 9, 10]

# s1 = set(l)
# s2 = set(l1)
# uncommon = s1 ^ s2
# print(uncommon)


# Subset and Superset Questions
# 23.Write a Python program to check whether one set is a subset of another. 
# s = {1,2,3,4,5,6,7}
# s1 = {2,3,4,5}
# print(s1 <= s)

# 24.Write a Python program to check whether one set is a superset of another. 
# s = {1,2,3,4,5,6,7}
# s1 = {2,3,4,5}
# print(s >= s1)

# 25.Write a Python program to check whether two sets are disjoint. 
# s = {1,2,3,4,5}
# s1 = {2,6,7,8,9}
# print(s.isdisjoint(s1))


# 27.	Write a Python program to verify proper subset and proper superset relationships. 
# s1 = {1, 2, 3}
# s2 = {1, 2, 3, 4, 5}

# if s1 < s2:
#     print("s1 is a proper subset of s2")
# else:
#     print("s1 is not a proper subset of s2")

# if s2 > s1:
#     print("s2 is a proper superset of s1")
# else:
#     print("s2 is not a proper superset of s1")


# # frozen set***********
# it is a final set we cant change values in it