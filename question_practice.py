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




# 22.	Write a Python program to find all pairs in a list whose sum is equal to a given target value. 
def pairs(ls,tar):
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i] + ls[j] == tar:
                print(ls[i],ls[j])

pairs([1,2,3,4,5,6,7,8,9],8)



# 23.	Write a Python program to find the first non-repeating element in a list. 
def first_non_repeating(ls):
    for i in range(len(ls)):
        if ls.count(ls[i]) == 1:
            return ls[i]

print(first_non_repeating([1,2,3,4,5,1,2,5,6,7,8]))



# 24.	Write a Python program to find the missing number in a list containing consecutive integers. 
def consecutive_int(ls):
    for i in range(min(ls),max(ls)+1):
        if i not in ls:
            return i

print(consecutive_int([1,2,4,5]))




# 25.	Write a Python program to swap the first and last elements of a list. 
def swap(ls):
    ls[0],ls[-1] = ls[-1],ls[0]
    return ls
print(swap([1,2,3,4,5]))



# 26.Write a Python program to check if all elements in a list are unique. 
def check(ls):
    un = []
    ans = []
    for i in ls:
        if i not in un:
            un.append(i)
        else:
            return False
    return True

print(check([1,2,3,4,5,2]))



# 27.	Write a Python program to split a list into two equal halves. 
def split(ls):
    one = []
    two = []
    r = len(ls)//2
    for i in range(len(ls)):
        if i < r:
            one.append(ls[i])
        else:
            two.append(ls[i])
    return one,two
print(split([1,2,55,66,22,77,88]))



    # 29.	Write a Python program to sort a list without using built-in sorting methods. 
def sort_list(ls):
    for i in range(len(ls)):
        for j in range(len(ls) - i - 1):
         if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

print(sort_list([1,2,5,4,99,5,6]))



# 30.	Write a Python program to find the maximum difference between any two elements in a list.
def maximum_diff(ls):
    minimum = float("+inf")
    maximum = float("-inf")
    for i in ls:
        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i
    diff = maximum - minimum

    return diff
print("maximum difference:",maximum_diff([1,2,3,4,5,6,7]))





# STRINGS
# Write a Python program to find the number of characters in a string 
def length_string(s):
    count = 0
    for i in s:
        count+=1
    return count
print("length of str is:",length_string("vikram"))



# Write a Python program to count the number of occurrences of all vowels in a string.
def vowel_count(s):
    count = 0
    for i in s:
        if i.lower() in "aeiou":
            count +=1
    return count
print("vowel count is:",vowel_count("VIkramao"))



# Write a Python program to find common characters present in two words.
def common_char(s,s1):
    common = ""
    for i in s:
        if i in s1 and i not in common:
            common += i
    return common
print(common_char("vikram","singh"))




# Write a Python program to check whether a given string is a palindrome.
def palindrome(s):
    if s == s[::-1]:
            print("palindrome")
    else:
        print("not palindrome")

palindrome("viv")


# Write a Python program to convert alternate characters in a string to capital letters.
def convert_char(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result +=s[i].upper()
        else:
            result += s[i]
    return result
print(convert_char("vikram singh"))



# Write a Python program to reverse a string without using built-in methods
def reverse_str(s):
    rev = s[::-1]
    return rev
print(reverse_str("vikram singh"))


# Write a Python program to count the number of words in a sentence (without using the split() function).
def count_words(s):
    count = 1
    for i in s:
        if i == " ":
            count+=1
    return count
print("total words in the str:",count_words("python is easy language"))



# Write a Python program to remove all spaces from a string.
def remove_space(s):
    ans = ""
    for i in s:
        if i != " ":
            ans += i
    return ans
print(remove_space("python is easy language"))



# Write a Python program to replace all occurrences of a given character in a string with another character.
def replace(s,old,new):
    ans = ""
    for i in s:
        if i == old:
            ans += new
        else:
            ans += i
    return ans
print(replace("banana","a","o"))


# Write a Python program to read a sentence and print the longest word in that sentence.
def longest_word(s):
    long = ""
    for i in s.split():
        if len(i) > len(long):
            long = i
    return long
print(longest_word("python is a programming language"))



# Write a Python program to check if two strings are anagrams (words formed by rearranging the letters of another, like “listen” and “silent”).
def anagram(s1,s2):
    if sorted(s1) == sorted(s2):
        print("anagram")
    else:
        print("not anagram")
anagram("silent","listen")


# second way
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in s1:
        if s1.count(i) != s2.count(i):
            return False

    return True

print(anagram("listen", "silent"))



# Write a Python program to find all the words in a string that start with a vowel.
def vowel_check(s):
    for i in s.split():
        if i[0].lower() in "aeiou":
            print(i,end = " ")
            
vowel_check("python is a language of cofing")


print()
# Write a Python program to remove all digits from a given string.
def remove_digit(s):
    ans = ""
    for i in s:
        if i.isalpha():
            ans +=i
    return ans
print("removed digits from str:",remove_digit("vi23k3ram422"))



# 1.	Create a dictionary of student details and print all keys and values. 
d = {1:"vikram",2:"aman",3 : "pulkit"}
for i in d.items():
    print(i)


# 2.	Check whether a given key exists in a dictionary. 

d = {1:"vikram",2:"aman",3 : "pulkit"}
key = 5
for i in d.items():
    if i[0] == key:
        print("key exists")
        break
else:
    print("not exists")



# 3.Count the number of key-value pairs in a dictionary. 
d = {1: "vikram", 2: "aman", 3: "pulkit"}

count = 0
for i in d.items():
    count += 1

print("count of key-value pairs are:",count)



# 4.	Add a new key-value pair to a dictionary. 
d = {1: "vikram", 2: "aman", 3: "pulkit"}
d[4] = "sawan"
print(d)


# 5.	Update the value of an existing key. 
d = {1: "vikram", 2: "aman", 3: "pulkit"}
d[3] = "singh"
print(d)


# 6.	Delete a specific key from a dictionary. 
d = {1: "vikram", 2: "aman", 3: "pulkit"}
del d[1]
print(d)


# 7.	Find the sum of all values in a dictionary. 
d = {"vikram": 33, "pulkit": 22, "sawan": 44}
sum = 0
for i in d.values():
    sum += i
print(sum)


# 8.	Merge two dictionaries into one.
d1 = {1: "vikram", 2: "aman"}
d2 = {3: "pulkit", 4: "sawan"}

d = {}

for i in d1:
    d[i] = d1[i]

for i in d2:
    d[i] = d2[i]

print(d)



# 9.Count the frequency of each character in a string
s = "hello"
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)


# Count the frequency of each word in a sentence
s = "python is a language"
d = {}
for i in s.split():
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
print(d)



# 11.	Find the first non-repeating character in a string.
s = "aabbcde"
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in s:
    if d[i] == 1:
        print(i)
        break

# 12.	Find the first repeating character in a string.
s = "abbccd"
d = {}
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
for i in s:
    if d[i]> 1:
        print(i)
        break





# 13.	Find the most frequent character in a string. 
s = "banana"
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

max_char = ""
max_count = 0

for i in d:
    if d[i] > max_count:
        max_count = d[i]
        max_char = i

print(max_char)


# 13.	Find the most frequent character in a string. 

s = "banana"
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

min_char = ""
min_count = float("+inf")

for i in d:
    if d[i] < min_count:
        min_count = d[i]
        min_char = i

print(min_char)

# 15.	Find duplicate characters in a string.
s = "banana"
ans = ""

for i in s:
    if s.count(i) > 1 and i not in ans:
        ans += i

print(ans)



# Find duplicate words in a sentence.
s = "banana is a fruit is tree nest"
ans = ""
for i in s.split():
    if s.split().count(i) > 1 and i not in ans.split():
        ans += i + " "
print(ans)


# 17.Find the key having the maximum value. 
d = {1: 20, 2: 30, 3: 40, 4: 50}

max_value = 0
ans = 0

for i in d:
    if d[i] > max_value:
        max_value = d[i]
        ans = i

print(ans)


# 18.	Find the key having the minimum value. 
d = {1: 20, 2: 30, 3: 40, 4: 50}

min_value = float("+inf")
ans = 0

for i in d:
    if d[i] < min_value:
        min_value = d[i]
        ans = i

print(ans)



# 19.	Sort a dictionary by keys.
d = {3: "pulkit", 1: "vikram", 2: "aman"}

ans = {}

for i in sorted(d):
    ans[i] = d[i]

print(ans)


# 20.	Sort a dictionary by values.
d = {1: 40, 2: 10, 3: 30, 4: 20}
ans = {}

items = list(d.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

for i in items:
    ans[i[0]] = i[1]

print(ans)


# 21.	Reverse a dictionary (swap keys and values). 
d = {1: "vikram", 2: "aman", 3: "pulkit"}
ans = {}

for i in d:
    ans[d[i]] = i

print(ans)

# 22.Create a dictionary from two lists. 
keys = [1, 2, 3]
values = ["vikram", "aman", "pulkit"]
d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)


# 23.Convert a list into a dictionary where elements are keys and their squares are values
ls = [1, 2, 3, 4, 5]
d = {}

for i in ls:
    d[i] = i ** 2

print(d)



# 24.	Find all keys associated with a particular value. 
d = {1: "aman", 2: "vikram", 3: "aman", 4: "pulkit"}
value = "aman"
ans = []

for i in d:
    if d[i] == value:
        ans.append(i)

print(ans)





# 25.	Remove all duplicate values from a dictionary. 
d = {1: "aman", 2: "vikram", 3: "aman", 4: "pulkit"}
ans = {}

for i in d:
    if d[i] not in ans.values():
        ans[i] = d[i]

print(ans)




# 26.	Count how many times each element appears in a list using a dictionary.
ls = [1, 2, 3, 2, 1, 4, 2]
d = {}

for i in ls:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)


