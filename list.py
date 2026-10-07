# ls = [4,23,43,"hlw",True,5.6,34,23]
# print(ls[2])
# print(ls[::-1])
# print(ls[6:3:-1])
# print(ls[-1:3:-1])

# ls = [1,2,3,4,5]
# target = 7
# for i in range(len(ls)):
#     for j in range(i+1,len(ls)):
#         if ls[i]+ls[j] == target:
#             print(ls[i] , ls[j])
# sum = 0
# for i in range(1,101):
#   if i%2==0:
#     sum += i

# print(sum)
# table = int(input("enter table"))
# for i in range(1, 11):
#     print(table*i)

    
# s = input()

# for i in range(len(s)):
#     count = 0

#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count += 1

#     if count == 1:
#         print(s[i])



# LIST METHODS************************************

# ls = [1,2,3,4,5,6,2,2]
# ls1 = [1,2,3,4,7,5,3,2]
# ll = [1,2,3,4,5,6,7,8,9]
# ls.append(10000)   #append method used to add value at the last
# ls.append(['vikram','singh'])  #we append list in the list
# ls.extend([34,56])   #extend method used to add element at the last but it stores elements individually 

# ls.insert(3,"debuShala")    # insert method is used to insert element it takes indexing first and then value (idx,value)
# ls[0] = 5

# ls.pop(2)   #this method remove element and it takes index in 
# ls.remove(2) # remove but tekes elements

# ls.reverse() #this method is used to reverse list
# ls1.sort() #this method is used to sort the elements but we can only perform sort method when all the data type is same in list and this sort the elements in original list
# # sorted(ls) this method is used to sort elements and it makes a duplicate list and sort their
# # print(ls.count(2)) #this method is used to count element frequency and we pass value inside this method
# lis = ls1.copy()
# ls.clear()  #it clears all the list

# del ll[0:4]

# print("ll after del fuction is used ",ll)
# print(ls)
# print(ls1)
# print(f"copy list {lis}")
# print(f"additon of list and ls:{lis+ls}")



# MULTIPLE LIST***********************
# nestLS = [[1,2,3,4],[2,3,4,2,4],[10,20,30,20,10]]
# print(nestLS[2][1:3]) 

# ls = [1,2,3,4,5,6]
# ls1 = []
# for i in ls:
#     ls1.append(i**2)

# print(ls1)


# REVERSE LIST USING APPEND METHOD
# ls = [1,2,3,4,5,6,7]
# reverse = []
# for i in range(len(ls)-1,-1,-1):
#     reverse.append(ls[i])

# print(reverse)

# duplicate and unique Elements******************
# ls = [1,2,3,4,5,6,7,1,3]
# unique = []
# duplicate = []

# for i in ls:
#     if i not in unique:
#         unique.append(i)

#     else:
#         duplicate.append(i)

# print("unique elements are:",unique)
# print("duplicate elements are:",duplicate)


#duplicate elements
# 
# ls = [1,2,3,44,5,6,7,3,3,4,5]
# duplicate = []

# for i in ls:
#     if ls.count(i) > 1:
#         duplicate.append(i)

# print(duplicate)

# ls = [1,2,3,4,5,6,7,8]
# ls1 = [2,4,6,8,56]
# common = []

# for i in ls:
#     for j in ls1:
#         if i == j:
#             common.append(i)

# print("common elements in list1 and list2 are:",common)



# move zeroes to the end***************************
# ls = [1,0,2,3,4,0,5,6,0,6,8]

# result = []

# for i in ls:
#     if i !=0:
#         result.append(i)

# for i in ls:
#     if i==0:
#         result.append(i)

# print(result)


# FIND ALL sum PAIRS  **********************
# ls = [1,2,3,4,5,6,7,8]
# target = int(input("enter your number:"))

# for i in range(len(ls)):
#     for j in range(i+1,len(ls)):
#         if ls[i] + ls[j] == target:
#             print(ls[i],ls[j])




# find all sum pairs of target
# ls = [2,3,4,5,6,7,8,9,10]
# ls1 = [2,1,3,5,6,7,8]
# target = int(input("enter your number:"))

# for i in range(len(ls)):
#     for j in range(len(ls1)):
#         if ls[i]+ls[j] == target:
#             print(ls[i],ls[j])



# merge two list without duplicate elements
# ls = [1,2,3,4,5,6,7,8,9,10]
# ls1 = [2,1,3,5,6,7,8]  
# result = []


# for i in ls:
#     if i not in ls1:
#         result.append(i)

# for i in ls1:
#     if i not in ls1:
#         result


# find maximum value and find minimum value and difference between them 
# ls = [1,2,3,4,5,6,7,8,9,10]

# max = max(ls)
# min = min(ls)
# diff = max-min
# print(max,min,diff)


# find maximum value and find minimum value and difference between them without using max and min function
# ls = [1,2,3,4,5,6,7,8,9,10]

# max = ls[0]
# min = ls[0]
# for i in range(1,len(ls)):
#     if ls[i] > max:
#         max = ls[i]
#     if ls[i] < min:
#         min = ls[i]
            
# diff = max-min
# print(max,min,diff)


# count positive negative and zero
# ls = [1,2,-2-3,0]
# pos = 0
# neg = 0
# zero = 0

# for i in ls:
#     if i > 0:
#         pos += 1
#     elif i < 0:
#         neg += 1 
#     else:
#         zero += 1
        
# print("positive number are:",pos)
# print("negative number are:",neg)
# print("zero number are:",zero)



# check if list is sorted
# ls = [1,2,3,4,5,6,7,8,9,10,]
# sorted = True
# for i in range(len(ls)-1):
#     if ls[i] > ls[i+1]:
#         sorted = False
#         break

# if sorted == True:
#     print("list is sorted")
# else:
#     print("list is not sorted")


# find missing number in list
# ls = [1,2,3,4,5,7,8,9,10]
# n = 6
# for i in range(1,n+1):
#     if i not in ls:
#         print("missing number in list is:",i)

# count occurence of element in list
# ls = [1,2,3,4,5,7,8,9,10,2,2,2]
# target = 2
# count = 0
# for i in ls:
#     if i == target:
#         count += 1        
# print("count of element in list is:",count)


# find the index of element in list
# ls = [1,2,3,4,5,7,8,9,10,2,2,2]
# target = 2
# for i in range(len(ls)):
#     if ls[i] == target:       
#         print("index of element in list is:",i)


# print prime numbers in list

numbers = [1,2,3,4,5,6,7,8]
for num in numbers:
    if num > 1:
        prime = True
        for i in range(2,num):
            if num%i == 0:
                prime = False
                break
    
        if prime == True:
             print(num)




# find fibonacci series



# find palindrome number  




    



