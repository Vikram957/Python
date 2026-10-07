# 1.Write a Python program to find the largest element in a list. 
# ls = [1,3,4,5,6,7,4,7,9]
# largest = float("-inf")

# for i in ls:
#     if i > largest:
#         largest = i

# print(largest)


# 2. Write a Python program to find the smallest element in a list. 
# ls = [2,3,4,5,6,8,9,5,43,56,2,9,0]
# smallest = float("+inf")

# for i in ls:
#     if i < smallest:
#         smallest = i

# print(smallest)


# 2.Write a Python program to find the smallest element in a list. 
# ls = [1,2,3,4,45,5,6,7,87,6,5,7,99,88]
# lar = float("-inf")
# sec = 0

# for i in ls:
#     if i > lar:
#         sec = lar
#         lar = i

#     elif sec < i and i != lar:
#         sec = i

# print(f"largest element:{lar}")
# print(f"second largest element:{sec}")



# 4.Write a Python program to find the second smallest element in a list. 
# ls = [2,3,4,5,6,7,8,9,0,1]
# small = float("+inf")
# sec = float("+inf")

# for i in ls:
#     if i < small:
#         sec = small
#         small = i

#     elif i < sec and i!= small:
#         sec = i

# print("smallest element:",small)
# print("second smallest element",sec)



# 5.Write a Python program to reverse a list without using built-in methods. 
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# ans = []

# for i in range(len(ls) - 1, -1, -1):
#       ans.append(ls[i])
# print(ans)
      

#     digit = ls[i]
#     rev = rev * 10 + digit

# # print(rev)
# ls.reverse()  #using list reverse function this change the elements in original list
# print(ls)
# reversed(ls)  #using python reverse function this wont change elements in original list
# print(ls)



# 6.Write a Python program to remove duplicate elements from a list
# ls = [1,2,3,4,5,5,3,2,4,9]
# ans = []

# for i in ls:
#     if i not in ans:
#        ans.append(i)

# print(ans)


# 7.Write a Python program to count the frequency of each element in a list. 
# ls = [1,2,3,4,4,2,3,6,7,6,5,2]
# for i in range(len(ls)):
#     count = 0
#     for j in range(i+1):
#         if ls[i] == ls[j]:
#             count+=1
#             print(f"element:{ls[j]} frequency:{count}")
            


# ls = [1, 2, 3, 4, 4, 2, 3, 6, 7, 6, 5, 2]

# for i in range(len(ls)):
#     if ls[i] in ls[:i]:
#         continue

#     count = 0

#     for j in range(len(ls)):
#         if ls[i] == ls[j]:
#             count += 1

#     print(ls[i], ":", count)



# 8.Write a Python program to find all duplicate elements in a list. 
ls = [1, 2, 3, 4, 4, 2, 3, 6, 7, 6, 5, 2,2,2,2,2,2]
dup = []

for i in range(len(ls)):
    
    if ls.count(i) > 1:
        dup.append(i)

print(dup)



# 9.Write a Python program to check whether a list is a palindrome. 
# ls = [1,2,1,3]
# rev = []
# tem = ls

# for i in range(len(ls)-1,-1,-1):
#     rev.append(ls[i])

# if rev == tem:
#     print("list is palindrome")
# else:
#     print("list is not palindrome")



# 10.Write a Python program to find the sum of all elements in a list. 
# ls = [1, 2, 3, 4, 5, 6, 6, 7]
# sum = 0

# for i in range(len(ls)):
#     sum = sum + ls[i]

# print(sum)


# 11.Write a Python program to find the product of all elements in a list.

# ls = [1,2,3,4]
# pro = 1
# for i in range(len(ls)):
#     pro = pro * ls[i]
# print(pro) 



# 12.Write a Python program to separate even and odd numbers from a list. 
# ls = [1,2,3,4,5,6,7,8,9]
# even = []
# odd = []

# for i in range(len(ls)):
#     if ls[i] % 2 == 0:
#         even.append(ls[i])
#     else:
#         odd.append(ls[i])

# print(even)
# print(odd)



# 13.Write a Python program to move all zero values to the end of a list. 
# ls = [0,2,1,3,0,0,3,0,5]
# ans = []

# for i in range(len(ls)):
#     if ls[i] != 0:
#         ans.append(ls[i])

# for i in range(len(ls)):
#     if ls[i] == 0:
#         ans.append(ls[i])

# print(ans)

# # OPTIMIZED WAY
# ls = [2, 1, 3, 0, 0, 3, 0, 5]
# j = 0
 
# for i in range(len(ls)):
#     if ls[i] != 0:
#         ls[i], ls[j] = ls[j], ls[i]
#         j += 1

# print(ls)


# 14.Write a Python program to find the common elements between two lists. 
# ls = [1,2,3,4,5,6,7,8,9]
# ls1 = [1,4,6,10,9]
# ans = []
# for i in range(len(ls)):
#     for j in range(len(ls1)):
#         if ls[i]==ls1[j]:
#             ans.append(ls[i])
# print(ans)

# # OPTIMIZED WAY
# ls = [1,2,3,4,5,6,7,8,9]
# ls1 = [1,4,6,10,9]
# ans = []

# for i in range(len(ls)):
#     if ls[i] in ls1:
#         ans.append(ls[i])

# print(ans)


# 15.	Write a Python program to find the union of two lists. 
# ls = [1,2,3,4,5,6]
# ls1 = [1,2,3,7,8,9]
# un = ls1.copy()
# for i in range(len(ls)):
#     if ls[i] not in un:
#         un.append(ls[i])
# un.sort()
# print(un)


# 16.	Write a Python program to find the intersection of two lists
# ls = [1,2,3,4,5,6,7]
# ls1 = [1,3,5,7,9,0,10]
# inter = []

# for i in range(len(ls)):
#     if ls[i] in ls1:
#         inter.append(ls[i])
# print(inter)


# 17.Write a Python program to check whether two lists are identical
# ls = [1,2,3,4,5]
# ls1 = [1,2,3,4,5]

# if ls == ls1:
#     print("list is identical")

# else:
#     print("list is not identical")


#18. Write a Python program to merge two lists without using the + operator. 
# ls = [1,2,3,4,5]
# ls1 = [1,2,3,4,5,554,6]
# m = []
# for i in range(len(ls)):
#     m.append(ls[i])

# for j in range(len(ls1)):
#     m.append(ls1[j])

# print(m)

# simple way
# merge = ls + ls1
# print(merge)





# 22.	Write a Python program to find all pairs in a list whose sum is equal to a given target value. 

# ls =[1,2,3,4,5,6,7,8,9]
# tar = int(input("enter target number:"))

# for i in range(len(ls)):
#     for j in range(len(ls)):
#         if ls[i] + ls[j] == tar:
#             print(ls[i],ls[j])



# 23.	Write a Python program to find the first non-repeating element in a list. 
# ls = [1,2,1,2,3,3,4,4,5,5,6,6,7,7]
# for i in range(len(ls)):
#     if ls.count(ls[i]) == 1:
#          print("first non repeating element is:",ls[i])
#          break

# else:
#      print("there is no non repeating element in list")


# 24.Write a Python program to find the missing number in a list containing consecutive integers. 
# ls = [1, 2, 3, 5, 6,8]

# for i in range(1, len(ls) + 2):
#     if i not in ls:
#         print("Missing number:", i)
        


# 25.	Write a Python program to swap the first and last elements of a list. 
# ls = [1, 2, 3, 4, 5]

# ls[0], ls[-1] = ls[-1], ls[0]

# print(ls)

        


#26.Write a Python program to check if all elements in a list are unique. 
# ls = [1, 2, 3, 4, 5, 6, 7, 1]
# unique = True
# for i in range(len(ls)):
#     count = 0
#     for j in range(len(ls)):
#         if ls[i] == ls[j]:
#             count += 1

#     if count > 1:
#         unique = False
#         break

# if unique:
#     print("unique")
# else:
#     print("not unique")

#optimized way*********************** 
# ls = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(ls)):
#     if ls.count(ls[i]) > 1:
#         print("not unique")
#         break
# else:
#         print("unique")


# 27.Write a Python program to split a list into two equal halves
# ls = [1, 2, 3, 4, 5, 6]

# mid = len(ls) // 2

# ls1 = []
# ls2 = []

# for i in range(len(ls)):
#     if i < mid:
#         ls1.append(ls[i])
#     else:
#         ls2.append(ls[i])

# print(ls1)
# print(ls2)



# 28.	Write a Python program to sort a list using the Bubble Sort algorithm. 
# ls = [1, 2, 3, 4, 5, 2, 3, 9, 4]

# for i in range(len(ls)):
#     for j in range(len(ls) - i - 1):

#         if ls[j] > ls[j + 1]:
#             ls[j], ls[j + 1] = ls[j + 1], ls[j]

# print(ls)


# 29.	Write a Python program to sort a list without using built-in sorting methods. 
# ls = [1,4,2,34,3,4,5,3,9,66,6]
# for i in range(len(ls)):
#     for j in range(len(ls)-i-1):

#       if ls[i] > ls[j]:
#         ls[i],ls[j] = ls[j],ls[i]


# print(ls)


# 30.Write a Python program to find the maximum difference between any two elements in a list.

# ls = [1, 5, 3, 9, 2, 7]

# maximum = ls[0]
# minimum = ls[0]

# for i in range(len(ls)):
#     if ls[i] > maximum:
#         maximum = ls[i]

#     if ls[i] < minimum:
#         minimum = ls[i]

# difference = maximum - minimum
# print("Maximum difference:", difference)


