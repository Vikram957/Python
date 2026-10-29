# import calendar
# year = int(input("enter year:"))
# month = int(input("enter month:"))

# cal = calendar.month(year,month)
# print(cal)


# Write a Python program to swap two variables without temp variable.
# a = int(input('enter value of a:'))
# b = int(input("enter value of b:"))
# a,b = b,a
# print("value of a is:",a)
# print("value of b is:",b)



# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
# for n in range(2,11):
#     for i in range(2,n):
#         if n % i ==0:
#             break
#     else:
#         print(n)


# factorial
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)


#write a python program to toggle the case of each character in a string without using the built in swapcase() method
# ex PyThOn output pYtHoN

# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if ch.isupper():
#         result += ch.lower()
#     else:
#         result += ch.upper()

# print(result)


# st = "PyThOn"
# s = ""
# for i in range(len(st)):
#     if i%2==0:
#         s +=i.upper()
#     else:
#         s += i.lower
# print(s)


# reverse
# string = "Vikram"
# ans = ""
# for i in range(len(string)-1,-1,-1):
#     ans += string[i]
# print(ans)


# reverse without using index
# s = "hello"
# reverse = ""

# for ch in s:
#     reverse = ch + reverse

# print(reverse)


numbers = [10, 20, 30, 40, 50]
reversed = []

n = len(numbers) - 1

while n >= 0:
    reversed.append(numbers[n])
    n -= 1
print(reversed)



l = [1,2,3,4,5,6,7,9,8]

lar = float("-inf")
sec = float("-inf")
trd = float("-inf")

for i in range(len(l)):
    if l[i] > lar:
        trd = sec
        sec = lar
        lar = l[i]

    elif l[i] > sec and l[i] != lar:
        trd = sec
        sec = l[i]

    elif l[i] > trd and l[i] != sec and l[i] != lar:
        trd = l[i]

print("largest element is:", lar)
print("sec largest element is:", sec)
print("third largest element is:", trd)




# greates in a number
# n = int(input("Enter a number: "))
# greatest = float("-inf")
# while n > 0:
#     digit = n % 10
#     if digit > greatest:
#         greatest = digit

#     n = n // 10

# print("grtst numbr is:", greatest)


# move zeroes*********
# better approach
l = [1,2,0,9,0,3,0,5,0,0,-1]
ans = []
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i],l[j] = l[j],l[i]
        j+=1

print(l)

# brute force approach
# for i in l:
#     if i !=0:
#         ans.append(i)

# for j in l:
#     if j ==0:
#         ans.append(j)

# print(ans)



#Armstrong number from 1 to 1000  
for num in range(1, 1001):
    temp = str(num)
    power = len(temp)
    totall = 0

    for i in temp:
        totall += int(i) ** power

    if totall == num:
        print(num)



# 5.	Write a Python program to reverse a list without using built-in methods. 
l = [1,2,3,4,5,6,7,8]
ans = []
for i in range(len(l)-1,-1,-1):
    ans.append(l[i])

print(ans)


# two pointer
l = [1, 2, 3, 4, 5, 6, 7, 8]

left = 0
right = len(l) - 1

while left < right:
    l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1

print(l)



# 6.Write a Python program to remove duplicate elements from a list. 
def remove_dup(l):
    ans = []
    for i in l:
        if i not in ans:     #time complexity n^2
            ans.append(i)
    return ans

print(remove_dup([1,2,1,2,3,4,5,5,5,5,6,7,8,9]))

# using set and for loop
def remove_dup(l):
    ans = []
    seen = set()
    for i in l:
        if i not in seen:    #tc -> n
            ans.append(i)
            seen.add(i)

    return ans

print(remove_dup([1, 2, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]))



# 7.Write a Python program to count the frequency of each element in a list. 
def freq_count(l):
    for i in set(l):   
        count = 0
        for j in l:
            if i == j:
                count +=1
        print(i,":",count)


freq_count([1,1,2,3,5,4,6,5,7,8,8,8,8,6,0,9])


# better approach using dictionary
def freq_count(l):
    freq = {}

    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for key, value in freq.items():
        print(key, ":", value)

freq_count([1,1,2,3,5,4,6,5,7,8,8,8,8,6,0,9])


# 8.	Write a Python program to find all duplicate elements in a list. 
def dupli_elem(l):
    un = []
    ans = []
    for i in l:
        if i in un: 
            if i not in ans:  #n^2
             ans.append(i)
        else:
            un.append(i)
    return ans

print("duplicate:",dupli_elem([1,1,2,2,3,4,5,3,6,7,3,3]))

# optimized tc -> n using set
def dupli_elem(l):
    un = set()
    ans = []

    for i in l:
        if i in un:
            if i not in ans:
                ans.append(i)
        else:
            un.add(i)

    return ans

print(dupli_elem([1, 1, 2, 2, 3, 4, 5, 3, 6, 7]))
print()


# 9.	Write a Python program to check whether a list is a palindrome. 
# using slicing
def is_palindrome(l):
    temp = l
    if temp == l[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

print(is_palindrome([1,2,1,4]))

# 2nd method
def is_palindrome1(l):
    temp = []
    for i in range(len(l)-1,-1,-1):
        temp.append(l[i])
    if temp == l:
        print("palindrome")
    else:
        print("not palindrome")

is_palindrome1([1,2,1,2])
print()



# 10.	Write a Python program to find the sum of all elements in a list. 
def sum_elem(l):
    total = 0
    for i in l:
        total += i
    return total

print("sum of element:",sum_elem([1,2,3,4,5,6,7,8,9]))


# 12.	Write a Python program to separate even and odd numbers from a list. 
def even_odd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

print(even_odd([1,2,3,4,5,6,7,7,8,9]))



# 14.	Write a Python program to find the common elements between two lists. 
def common_elem(l,l1):
    ans = []
    for i in l:
        for j in l1:
            if i==j:
                ans.append(i)
    return ans

print(common_elem([1,2,3,4,5,6],[1,1,2,4,7,8,9]))


def common(l,l1):
    ans =[]

    for i in l:
        if i in l1:
            ans.append(i)

    return ans

print(common([1,2,3,4],[1,2,5,6,1,1,1,1]))
print()


# 15.	Write a Python program to find the union of two lists. 
# def unionn(l,l1):
#     ans = l1.copy()
#     for i in l:
#         if i not in ans:
#             ans.append(i)
#     return ans

# print(unionn([1,2,3,4,5],[1,2,6,7,8,9]))


def unionn(l,l1):
    ans = []
    for i in l+l1:
        if i not in ans:
            ans.append(i)
    return ans

print(unionn([1,2,3,4,5],[1,2,6,7,8,9]))
print()


# better approach
# def unionn(l, l1):
#     ans = []
#     seen = set()

#     for i in l1 + l:
#         if i not in seen:
#             ans.append(i)
#             seen.add(i)

#     return ans

# print(unionn([1,2,3,4,5], [1,2,6,7,8,9]))


# 16.	Write a Python program to find the intersection of two lists. 
def inter(l,l1):
    ans = []
    for i in l1:
        if i in l:
            ans.append(i)
    return ans

print(inter([1,2,3,4,5,6],[1,2,3,7,8,9]))



# better
def inter(l, l1):
    seen = set(l)
    ans = []
    added = set()

    for i in l1:
        if i in seen and i not in added:
            ans.append(i)
            added.add(i)

    return ans

print(inter([1,2,3,4,5,6], [1,2,3,7,8,9]))


# 17.	Write a Python program to check whether two lists are identical. 
def check_identical(l,l1):
    if l == l1:
        print("identical")
    else:
        print("not identical")

check_identical([1,2,3,4],[3,4,5])



# 18.	Write a Python program to merge two lists without using the + operator. 
def merge(l,l1):
    ans = l.copy()
    for i in l1:
        ans.append(i)
    return ans

print(merge([1,2,3,4],[1,2,4,5,6]))


# 19.	Write a Python program to rotate a list to the right by one position. 
def rotate_right(l):
    return l[-1:] + l[:-1]

print(rotate_right([1, 2, 3, 4, 5]))


# rotate left by 1
def rotate_left(l):
    return l[1:]  + l[:1]

print(rotate_left([1, 2, 3, 4, 5]))


# k rotates
def k_rotate(l,k):
    k = k % len(l)
    ans = l[k:] + l[:k]
    return ans

print(k_rotate([1,2,3,4,5,6],4))



# 22.Write a Python program to find all pairs in a list whose sum is equal to a given target value. 
def two_sum(l, tar):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == tar:
                print(l[i], l[j])

two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 8)



# 23.	Write a Python program to find the first non-repeating element in a list. 
def first_non_repeating(l):
    for i in range(len(l)):
        count = 0

        for j in range(len(l)):
            if l[i] == l[j]:
                count += 1

        if count == 1:
            print(l[i])
            return

    print("No non-repeating element found")


first_non_repeating([4, 5, 1, 2, 1, 4, 5])

# count funcn
def f_non(l):
    for i in range(len(l)):
        if l.count(l[i])==1:
            return l[i]

print(f_non([1,2,3,4,2,3,5,6,7,8,1]))


# 24.Write a Python program to find the missing number in a list containing consecutive integers. 

def mis_num(l):
    for i in range(min(l),max(l)+1):
        if i not in l:
            return "missing number:", i
mis_num([1,2,3,5,6])


# 25.Write a Python program to swap the first and last elements of a list. 
def swap(l):
    l[0],l[-1] = l[-1],l[0]
    return l

print(swap([1,2,3,4,5]))


# 26.	Write a Python program to check if all elements in a list are unique. 
def check(l):
    a=[]
    unique = True
    for i in l:
        if i not in a:
            a.append(i)
            
        else:
            unique = False
    return unique
    
    
print(check([1,2,3,4,5,6,6]))

# other ways
ls = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(ls)):
    if ls.count(ls[i]) > 1:
        print("not unique")
        break
else:
        print("unique")


# using set
def check(l):
    return len(l) == len(set(l))

print(check([1, 2, 3, 4, 5, 6, 6]))


# 27.	Write a Python program to split a list into two equal halves. 
def split_list(l):
    first = []
    sec = []
    mid = len(l)//2
    for i in range(len(l)):
        if i <mid:
            first.append(l[i])
        else:
            sec.append(l[i])

    return first,sec

print(split_list([1,2,3,4,5,6,7,8,9]))


# 29.	Write a Python program to sort a list without using built-in sorting methods. 
def sort_list(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

print(sort_list([2,4,6,7,1,2,3]))



# 30.Write a Python program to find the maximum difference between any two elements in a list.
def find_max_diff(l):
    min1 = float("+inf")
    max1 = float("-inf")
    for i in l:
        if i > max1:
            max1 = i
        if i < min1:
            min1 = i

    Difference = max1 - min1
    return Difference

print(find_max_diff([1,2,3,4,5,6,7,8,9]))