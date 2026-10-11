# List Questions
# 1.Write a Python program to find the largest element in a list. 

def largest(list1):
    lar = float("-inf")
    for i in list1:
        if i>lar:
            lar = i
    return lar

print("Largest element in the list:",largest([1,2,3,4,5,6,7,8,9,10,111,11]))


# 2.	Write a Python program to find the smallest element in a list. 

def smallest(list1):
    small = float("+inf")
    for i in list1:
        if i<small:
            small = i
    return small

print("Smallest element in the list:",smallest([1,2,3,4,5,6,7,8,9,10,111,11]))



# 3.	Write a Python program to find the second largest element in a list. 
def sec_largest(list1):
    lar = float("-inf")
    sec = float("-inf")
    for i in list1:
        if i > lar:
            sec = lar
            lar = i
        elif i > sec and i !=lar:
            sec = i
    return sec

print(sec_largest([1,2,3,4,5,6,9,8]))



# 4.Write a Python program to find the second smallest element in a list. 
def sec_smallest(list1):
    small = float("+inf")
    sec = float("+inf")
    for i in list1:
        if i < small:
            sec = small
            small = i
        elif i < sec and i !=small:
             sec = i
    return sec

print(sec_smallest([1,2,3,4,5,6,9,8]))



# 5.Write a Python program to reverse a list without using built-in methods. 
def reverse_list(list1):
    rev = []
    for i in range(len(list1)-1,-1,-1):
        rev.append(list1[i])
    return rev

print("reversed list:",reverse_list([1,2,3,4,5,6]))




# 6.Write a Python program to remove duplicate elements from a list. 
def remove_duplicate(list1):
    ans = []
    for i in list1:
        if i not in ans:
            ans.append(i)
    return ans

print("duplicates removed:",remove_duplicate([1,2,3,2,3,4,5,1]))



# 7.Write a Python program to count the frequency of each element in a list. 
def frequency_count(list1):
    for i in range(len(list1)):
        count = 0
        for j in range(i+1):
            if list1[i] == list1[j]:
                count+=1
            print(list1[i],count)
                
frequency_count([1,2,1,3,4,3,5,4,6,7,8,9,9])


# 2nd way using dictionary

def frequency_count(list1):
    d = {}

    for i in list1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d

print(frequency_count([1, 2, 1, 3, 4, 3, 5, 4, 6, 9, 9]))



# 3rd way
def frequency_count(ls):
    for i in range(len(ls)):

        if ls[i] in ls[:i]:
         continue

        count = 0

        for j in range(len(ls)):
             if ls[i] == ls[j]:
              count += 1

        print(ls[i], ":", count)

frequency_count([1,2,1,3,2,4,5,6,7,6,66,6,6])



# 8.Write a Python program to find all duplicate elements in a list. 
def duplicate_elements(ls):
    dup = []
    non = []
    for i in ls:
        if i not in non:
            non.append(i)
        else:
            if i not in dup:
             dup.append(i) 
    return dup

print("duplicate elements:",duplicate_elements([1,2,3,4,2,4,4,4,4,4,4,45,6,1,7]))



# 9.	Write a Python program to check whether a list is a palindrome. 
def palindrome(ls):
    ans = []
    for i in range(len(ls)-1,-1,-1):
        ans.append(ls[i])
    if ans != ls:
        print("not palindrome")
        return False
    else:
        print("palindrome")
    
    return "palindrome"

palindrome([1,2,1])



# 10.	Write a Python program to find the sum of all elements in a list. 
def sum_of_elements(ls):
    summ = 0
    for i in ls:
        summ = summ+i
    return summ
print(sum_of_elements([1,2,3]))




# 11.	Write a Python program to find the product of all elements in a list. 

def pro_of_elements(ls):
    pro= 1
    for i in ls:
        pro = pro*i
    return pro
print(pro_of_elements([1,2,3,4]))




# 12.	Write a Python program to separate even and odd numbers from a list. 
def check(ls):
    even = []
    odd = []
    for i in ls:
        if i % 2 == 0:
            even.append(i)
            
        else:
            odd.append(i)

    return even,odd
print(check([1,2,3,4,5,6,7,8,9]))



# 13.	Write a Python program to move all zero values to the end of a list. 
def move_zeroes(ls):
    j = 0
    for i in range(len(ls)):
        if ls[i] != 0:
            ls[i],ls[j] = ls[j],ls[i]
            j+=1
    return ls

print(move_zeroes([0,9,3,0,2,0,3,0,23,3]))



# 14.	Write a Python program to find the common elements between two lists. 
def common_elements(ls1,ls2):
    common = []
    for i in ls1:
        if i in ls2:
            common.append(i)

    return common

print("common elements btw two list:",common_elements([1,2,3,4,5,6,7,8,9,],[1,2,3,4,99,88]))




# 15.	Write a Python program to find the union of two lists. 
def unionn(ls1,ls2):
    un = ls2.copy()
    for i in ls1:
        if i not in un:
            un.append(i)
    un.sort()

    return un
print("union:",unionn([1,2,3,4,5,6],[1,2,3,6,7,8,9]))




# 16.	Write a Python program to find the intersection of two lists. 
def inter(ls1,ls2):
    interr = []
    for i in ls1:
        if i in ls2:
            interr.append(i)

    return interr
print("intersection:",inter([1,2,3,4,5,6],[1,2,3,7,8,9]))


# 17.	Write a Python program to check whether two lists are identical. 
def identical(ls,ls1):
    if ls == ls1:
        return "Identical"
    else:
        return "not identical"

print(identical([1,2,3],[1,2,1]))




# 18.	Write a Python program to merge two lists without using the + operator. 
def merge_list(ls1,ls2):
    merge = []
    for i in ls1:
        merge.append(i)
    for j in ls2:
        merge.append(j)
    return merge

print("merge list:",merge_list([1,2,3,4,5],[1,2,3,4,5,6]))


# 19.	Write a Python program to rotate a list to the right by one position. 
def rotate_right(list1):
    return list1[-1:] + list1[:-1]

print(rotate_right([1, 2, 3, 4, 5]))



# 20.	Write a Python program to rotate a list to the left by one position. 

def rotate_left(list1):
    return list1[1:] + list1[:1]

print(rotate_left([1, 2, 3, 4, 5]))



# 21.	Write a Python program to rotate a list by k positions. 
def k_rotates(ls):
    rot = []
    k = 3
    k %= len(ls)
    rot = ls[k:] + ls[:k]
    return rot
print(k_rotates([1,2,3,4,5,6,7]))




