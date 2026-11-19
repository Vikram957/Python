# LIST QUESTIONS
# 1.	Write a Python program to find the largest element in a list. 
def check_largest(l):
    largest = float("-inf")
    for i in range(len(l)):
        if l[i] >largest:
            largest = l[i]
    return largest

print("largest element in a list:",check_largest([1,2,3,2,9,6,7,5,3,6,5,6,3]))

# 2.	Write a Python program to find the smallest element in a list. 
def check_smallest(l):
    smallest = float("+inf")
    for i in range(len(l)):
        if l[i] <smallest:
            smallest = l[i]
    return smallest

print("smallest element in a list:",check_smallest([1,2,3,2,9,6,7,5,3,0,6,5,6,3]))


# 3.	Write a Python program to find the second largest element in a list. 
def sec_small(l):
    lar = float("-inf")
    sec = float("-inf")

    for i in l:
        if i > lar:
            sec = lar
            lar = i

        elif sec < i and sec!=i:
            sec = i
    return sec

print("second largest element:",sec_small([0,3,2,9,5,8,5,4,3]))


# 4.	Write a Python program to find the second smallest element in a list. 
def sec_smallest(l):
    smallest = float('+inf')
    sec = float('+inf')

    for i in l:
        if i < smallest:
            sec = smallest
            smallest = i

        elif sec > i and sec!=i:
            sec = i
    return sec

print("second smallest element:",sec_smallest([9,7,5,3,0,3,1,7]))


# 5.	Write a Python program to reverse a list without using built-in methods. 
def reverse_list(l):
    reversed = l[::-1]   #with slicing
    # for i in range(len(l)-1,-1,-1):   #with indexing
    #     reversed.append(l[i])
    return reversed

print("reversed list:",reverse_list([1,2,3,4,5,6,7,8,9]))


# 6.	Write a Python program to remove duplicate elements from a list. 
def remove_duplicate(l):
    unique = []
    for i in l:
     if i not in unique:
         unique.append(i)

    return unique

print("removed duplicates:",remove_duplicate([1,2,3,4,1,2,3,4,5,5,4,6,7,8,9,7,8,9]))


# 7.	Write a Python program to count the frequency of each element in a list.
def freq_count(l):
    for i in set(l):   
        count = 0
        for j in l:
            if i == j:
                count +=1
        print(i,":",count)

freq_count([1,2,3,4,5,6,2,3,4,5,9])


def freq2(l):
    freq = {}
    for i in l:
        if i in freq:
            freq[i] +=1

        else:
            freq[i] =1

    for key,value in freq.items():
        print(key, ":",value)

freq2([1,1,1,1,2,3,4,2,3,3,3,4,5,6,5])


# 8.	Write a Python program to find all duplicate elements in a list. 
def check_duplicate(l):
    duplicate = []
    unique = []
    for i in l:
        if i in unique:
            if i not in duplicate:
                duplicate.append(i)
        else:
            unique.append(i)
        
    return duplicate

print("duplicate elements:",check_duplicate([1,2,3,1,4,5,6,3,4,8,9,9]))


# 9.	Write a Python program to check whether a list is a palindrome. 
def check_palindrome(l):
    if l == l[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

check_palindrome([1,2,1])


# 10.	Write a Python program to find the sum of all elements in a list. 
def sum_element(l):
    ans = 0
    for i in l:
        ans +=i
    return ans

print("sum of elements:",sum_element([1,2,3,4,5,6,7,8,9]))


# 11.	Write a Python program to find the product of all elements in a list. 
def pro_element(l):
    pro = 1
    for i in l:
        pro *=i
    return pro

print("product of elements:",pro_element([1,2,3,4,5,6,7,8,9]))


# 12.	Write a Python program to separate even and odd numbers from a list. 
def sep_even_odd(l):
    even = []
    odd = []
    for i in l:
        if i %2 ==0:
            even.append(i)
        else:
            odd.append(i)

    return even,odd

print("even odd separated:",sep_even_odd([1,2,3,4,5,6,7,8,9]))


# 13.	Write a Python program to move all zero values to the end of a list. 
def move_zeroes(l):
    j = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[i],l[j] = l[j],l[i]
            j +=1

    return l

print("move zeroes to the end:",move_zeroes([0,1,2,30,4,0,5,0,6,7]))


# 14.	Write a Python program to find the common elements between two lists. 
def common_two(l,l2):
    common = []
    for i in l:
        for j in l2:
            if i==j:
                common.append(i)

    return common

print("common elements:",common_two([1,2,3,4,5,6],[1,2,7,8,9]))


def common_2(l,l2):
    common = []
    for i in l:
        if i in l2:
            common.append(i)

    return common

print("common elements:",common_2([1,2,3,4,5,6],[1,2,7,8,9]))


# 15.	Write a Python program to find the union of two lists. 
def union_two(l,l1):
    un = l1
    for i in l:
        if i not in un:
            un.append(i)

    return un

print(union_two([1,2,3,4,2,3],[1,2,3,4,5,6,7,8,9]))


def unionn(l,l1):
    ans = []
    for i in l+l1:
        if i not in ans:
            ans.append(i)
    return ans

print(unionn([1,2,3,4,5],[1,2,6,7,8,9]))
print()


# 16.	Write a Python program to find the intersection of two lists. 
def find_intersection(l,l1):
    inter = []
    for i in l:
        if i in l1:
            inter.append(i)
    return inter


print("intersection:",find_intersection([1,2,3,4,5,6],[1,2,3,8,9]))



# 17.	Write a Python program to check whether two lists are identical. 
def check_identical(l,l1):
    if l == l1:
        print("identical list")
    else:
        print("not identical list")

check_identical([1,2,3,4],[1,2,3,43])


# 18.	Write a Python program to merge two lists without using the + operator. 
def merge_list(l,l1):
    ans = l.copy()
    for i in l1:
        ans.append(i)
    return ans

print(merge_list([1,2,3,4],[5,6,7,8]))


# 19.	Write a Python program to rotate a list to the right by one position. 
def right_rotate(l):
    return l[-1:] + l[:-1]

print("right rotate by 1:",right_rotate([1,2,3,4,5]))

# 20.	Write a Python program to rotate a list to the left by one position. 
def left_rotate(l):
    return l[1:]+l[:1]
print("left rotation:",left_rotate([1,2,3,4,5]))


# 21.	Write a Python program to rotate a list by k positions. 
def rotate_k(l,k):
    k = k % len(l)
    ans = l[k:]+l[:k]

    return ans
print(rotate_k([1,2,3,4,5,6],3))

# 22.	Write a Python program to find all pairs in a list whose sum is equal to a given target value. 
def find_pairs(l,tar):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==tar:
                print(l[i],l[j])

find_pairs([1,2,3,4,5,6,7,8,9],8)


# 23.	Write a Python program to find the first non-repeating element in a list. 
def first_non_repeating(l):
    for i in l:
        if l.count(i)==1:
            return i

print("first non repeating element:",first_non_repeating([1,1,2,3,4,2,3,4,6,7,8]))


# 24.	Write a Python program to find the missing number in a list containing consecutive integers. 
def mis_num(l):
    for i in range(min(l),max(l)+1):
        if i not in l:
            return "missing number:", i
mis_num([1,2,3,5,6])


# 25.	Write a Python program to swap the first and last elements of a list. 
def swap_last(l):
    l[-1],l[0] = l[0],l[-1]
    return l

print(swap_last([1,2,3,4]))

# 26.	Write a Python program to check if all elements in a list are unique. 
def check_unique_list(l):
    unique = []
    ans = True
    for i in l:
        if i not in unique:
            unique.append(i)
        else:
            ans = False
    return ans

print(check_unique_list([1,2,3,4,5,6]))


# 27.	Write a Python program to split a list into two equal halves. 
def split_two_halves(l):
    first = []
    second = []
    mid = len(l)//2

    for i in range(0,mid):
        first.append(l[i])
    for i in range(mid,len(l)):
        second.append(l[i])

    return first,second

print(split_two_halves([1,2,3,4,5,6,7,8,9]))


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


# 29.	Write a Python program to sort a list without using built-in sorting methods. 
def sort_list(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

print(sort_list([2,4,6,7,1,2,3]))





# 30.	Write a Python program to find the maximum difference between any two elements in a list.

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