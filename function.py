# POSITIONAL ARGUMENTS
# def student(name,age):
#     print(name,age)
# student("vikram",22)

# # KEYWORD ARGUMENTS
# def student(name,age):
#     print(name,age)
# student(age = 22, name = 'vikram')


# # DEFAULT ARGUMENTS
# def student(name = 'VIKRAM',age = 22):
#     print(name,age)
# student()


#VARIABLE-LENGTH ARGUMENTS(*ARGS)
# def total(*args):
#     print(args)

# total(10,20,30) 

# keyword variable-length arguments (**kwargs) 
def details(**kwargs):  #keyword variable-length arguments (**kwargs)
    print(kwargs)
details(name=['vikram','singh'],age = 22)



# def addition(a,b):
#     res = a + b

#     return res

# print(addition(2,4))


# def largest(list):
#     lar = float("-inf")
#     for i in list:
#         if i > lar:
#             lar = i
#     return lar
# print(largest([1,2,3,4,5,6,7,8,9]))


# def star(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
#         print()

# star(5)



# def invertedstar(n):
#     for i in range(n):
#         for j in range(n-i):
#             print("*",end="")
#         print()

# invertedstar(5)


# def reve(st):
    # words = st.split()
    # rev = st[::-1]

    # for word in words:
    #     word = word.strip("!,.?")
    #     rev += word[::-1] + " "
#     return rev
        
# print(reve('python is a programing language yes'))


# def add(a,b):
#     return a+b

# def square(x):
#     return x*x

# a = int(input("enter the number1:"))
# b = int(input("enter the number2:"))

# sum = add(a,b)
# ans = square(sum)


# print(sum)
# print(ans)




# def totalMarks(sub1_marks,sub2_marks):
#     total = sub1_marks+sub2_marks
#     return total

# s1 = int(input("enter the marks:"))
# s2 = int(input("enter the marks:"))

# result = totalMarks(s1,s2)

# def avg(n):
#     average = result//n
#     return average

# no = int(input("enter no of subject:"))
# print("average:",avg(no))


# def perecent(n):
#     per = result/n
#     return per
# print("perecent:",perecent(no))





# def total(m1,m2,m3):
#     return m1+m2+m3

# totalM = total(30,56,100)
# print(totalM)

# def percen(totalM):
#     return (totalM / 300)*100

# per = percen(totalM)
# print(per)

# def grade(per):
#     if per >= 90:
#         return 'a+'
#     elif per >=75 and per < 90:
#         return "a grade"
#     elif per >= 40 and per < 75:
#         return "b grade"
#     else:
#         return 'fail'

# print(grade(per))





# 1.Write a Python program to find the largest element in a list. 
# def largest(list1):
#     lar = float("-inf")
#     for i in range(len(list1)):
#         if list1[i] > lar:
#             lar = list1[i]
#     return lar


# lar = largest([1,2,3,4,5,6,7,8,9,11])
# print("largest element in a list:",lar)




# 2.Write a Python program to find the smallest element in a list. 
# def smallest(list1):
#     smal = float("+inf")
#     for i in range(len(list1)):
#         if list1[i] < smal:
#             smal = list1[i]
#     return smal

# small = smallest([1,2,3,4,5,6,7,8,0,5,-1])
# print("smallest element in a list:",small)



# 3.Write a Python program to find the second largest element in a list. 
# def secLargest(l):
#     sec = float("-inf")
#     lar = float("-inf")
#     for i in range(len(l)):
#         if l[i] > lar:
#             sec = lar
#             lar = l[i]

#         elif sec < l[i] and l[i] != lar:
#             sec = l[i]
#     return sec

# sec = secLargestest([1,2,3,4,5,7,6])
# print("second largest in a list:",sec)




# 4.Write a Python program to find the second smallest element in a list. 
# def secSmallest(l):
#     smal = float("+inf")
#     secSml = float("+inf")
#     for i in range(len(l)):
#         if l[i] < smal:
#             secSml = smal
#             smal = l[i]

#         elif secSml > l[i] and l[i] != smal:
#             secSml = l[i]
#     return secSml

# secondSmallest = secSmallest([1,2,3,4,5,6,7,8,9])
# print("second smallest in a list is:",secondSmallest)



# 5.Write a Python program to reverse a list without using built-in methods. 
# def rev(l):
#     ans = []
#     for i in range(len(l)-1,-1,-1):
#         ans.append(l[i])

#     return ans

# reverse = rev([1,2,3,2,5,6,7,8,9])
# print("reversed list:",reverse)



# 6.Write a Python program to remove duplicate elements from a list. 
# def removeDuplicate(l):
#     dup = []
#     for i in range(len(l)):
#         if l[i] not in dup:
#             dup.append(l[i])

#     return dup

# remove = removeDuplicate([1,1,2,2,3,4,3,4,5,5,6,6,7,6,7,8,9,8])
# print("remove duplicate list:",remove)



# 7.Write a Python program to count the frequency of each element in a list. 
# def countFreq(l):
#     for i in range(len(l)):
#         if l[i] in l[:i]:
#             continue
#         count = 0
#         for j in range(len(l)):
#             if l[i] == l[j]:
#                 count += 1

#         print(l[i],":", count)


# countFreq([1,1,2,3,4,3,5,6,4,8,9])



# 8.Write a Python program to find all duplicate elements in a list. 
# def duplicateElements(l):
#     dup = []
#     non = []
#     for i in range(len(l)):
#         if l[i] not in non:
#             non.append(l[i])
#         else : 
#             if l[i] not in dup:
#              dup.append(l[i])
#     return dup

# duplicate = duplicateElements([1,2,3,4,2,3,6,6,7,8,9,8,2,2])
# print(duplicate)



# 2nd way
# def duplicateElements(l):
#     dup = []

#     for i in l:
#         if l.count(i) > 1 and i not in dup:
#             dup.append(i)

#     return dup


# duplicate = duplicateElements([1,2,3,4,2,3,6,6,7,8,9,8])
# print(duplicate)




# 9.Write a Python program to check whether a list is a palindrome. 
# def isPalindrom(l):
#     rev = []
#     for i in range(len(l)-1,-1,-1):
#         rev.append(l[i])

#     if rev == l:
#         print("palindrome list")
        
#     else:
#         print("not a palindrome list")

# isPalindrom([1,2,3,2,1,2])



# using return 
# def isPalindrome(l):
#     rev = []

#     for i in range(len(l)-1, -1, -1):
#         rev.append(l[i])

#     return rev == l

# print(isPalindrome([1,2,3,2,1,3]))




# 10.Write a Python program to find the sum of all elements in a list. 
# def sumOfElement(l):
#     sum = 0
#     for i in l:
#         sum +=i
#     return sum

# sum = sumOfElement([1,2,3,4,5])
# print("sum of all elements in a list:",sum)



# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(i):
#             print(j,end=' ')
#         print()

# print(pattern(6))

# def pattern(n):
#     result = ""

#     for i in range(1, n + 1):
#         for j in range(i):
#             result += str(j)
#         result += "\n"

#     return result

# print(pattern(5))


# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(i):
#             print(chr(65 + j), end="")
#         print()

# pattern(5)

# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(i):
#             print(chr(97 + j), end ="")
#         print()

# pattern(6)




# Upper half
# def diamondPattern(n):
#     for i in range(1, n + 1):
#      for j in range(n - i):
#         print(" ", end="")
        
#      for j in range(2 * i - 1):
#         print("*", end="")
        
#      print()

# # Lower half
#     for i in range(n - 1, 0, -1):
#      for j in range(n - i):
#         print(" ", end="")
        
#      for j in range(2 * i - 1):
#         print("*", end="")
        
#      print()


# diamondPattern(5)


# 11.	Write a Python program to find the product of all elements in a list. 
# def productOfElement(l):
#     product = 1
#     for i in l:
#         product *= i
#     return product

# prod = productOfElement([1,2,3,4,5])
# print(prod)


# 12.	Write a Python program to separate even and odd numbers from a list. 
# def evenOdd(l):
#     even = []
#     odd = []
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even,odd

# ans = evenOdd([1,2,3,4,5,6,7,8])
# print(ans)



# 13.	Write a Python program to move all zero values to the end of a list. 
def moveZeroes(l):
    j = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[i],l[j] = l[j],l[i]
            j+=1
    return l 

li = moveZeroes([1,2,0,0,2,3,0,5,0,6,0,8])
print(li) 


# 14.	Write a Python program to find the common elements between two lists. 
def cmonElem(l):
    common = []
    for i in range(len(l)):
        if l.count(l[i]) > 1 and l[i] not in common:
            common.append(l[i])
    return common

common = cmonElem([1,2,3,2,4,5,3,5,6,7,8])
print("common elements in a list:",common)


# 15.	Write a Python program to find the union of two lists. 
def union(l1,l2):
    un = l1.copy()
    for i in l2:
        if i not in un:
            un.append(i)
    return un

un = union([1,2,3,4,5],[3,5,6,7,8])
print("union of two list l1 and l2:",un)

# 16 write a python program to find intersection of two list
def intersection(l1,l2):
    inter = []
    for i in l1:
        if i in l2:
            inter.append(i)
    return inter

inter = intersection([1,2,3,4,5],[1,2,3,4,6,7,8,9])
print("intersection or two list l1 and l2:",inter)


# 17.	Write a Python program to check whether two lists are identical. 
def identical(l1,l2):
    if l1 == l2:
        print("identical list")
    else:
        print("not identical")

identical([1,2,3],[1,2,3])

# 18.	Write a Python program to merge two lists without using the + operator. 
def merge(l1,l2):
    mer = l2.copy()
    for i in l1:
        if i not in mer:
            mer.append(i)
    return mer

mergeList = merge([1,2,3,4],[1,2,3,4,5,6,7,8])
print("merge list:",mergeList)


# 20.	Write a Python program to rotate a list to the left by one position. 
def rotate(l):
    k = int(input("enter value of k:"))
    k = k % len(l)
    ans = l[-k:] + l[:-k]
    return ans

ans = rotate([1,2,3,4,5,6])
print(ans)


# 22.	Write a Python program to find all pairs in a list whose sum is equal to target
def sumTar(l):
    tar = int(input("enter target:"))
    for i in l:
        for j in l:
            if i+j == tar:
                print(i,j)

sumTar([1,2,3,4,5,6,7,8])


# 23.Write a Python program to find the first non-repeating element in a list. 
def first_non_Repeating(l):
    for i in l:
        if l.count(i) == 1:
            print("first non-repeating element:",i)
            break

first_non_Repeating([1,2,3,4,5,1,2,3,5,6,7])

