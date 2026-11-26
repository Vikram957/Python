# Basic String Questions
# 1.	Write a Python program to print each character of a string on a new line.
def new(s):
    for i in s:
        print(i)

    return None

new('Vikram')
print()

# 2.	Write a Python program to find the length of a string without using len().
def length_string(s):
    length = 0
    for i in s:
        length +=1

    return length

print('length of string',length_string('Vikram'))
print()


# 3.	Write a Python program to count the number of vowels in a string.
def vowel_count(s):
    count = 0
    for i in s:
        if i.lower() in 'aeiou':
            count +=1

    return count

print('vowel count:',vowel_count('Vikram'))



# 4.	Write a Python program to count the number of consonants in a string.
def consonant_count(s):
    count = 0
    for i in s:
        if i.isalpha() and i.lower() not in 'aeiou':
            count+=1

    return count

print('consonant count:',consonant_count('Vikram23o'))



# 5.	Write a Python program to count the number of uppercase and lowercase letters in a string.
def check_case(s):
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
            upper_case +=1
        elif i.islower():
            lower_case+=1

    return upper_case,lower_case

print('upper and lower case count:',check_case('ViKRAM'))




# 6.	Write a Python program to count the number of digits in a string.
def number_digit(s):
    count = 0
    for i in s:
        if i.isdigit():
            count +=1

    return count

print('digit count in a str:',number_digit('Vik2am4'))



# 7.	Write a Python program to count the number of spaces in a string.
def space_count(s):
    count = 0
    for i in s:
        if i==' ':
            count+=1
    return count

print('space count:',space_count('Python is a easy language'))




# String Reversal and Comparison
# 8.	Write a Python program to reverse a string without using slicing or any string method.

def reverse_str(s):
    rev = ''
    for i in s:
        rev = i + rev
    return rev

print('reversed string:',reverse_str('vikram'))


def reverse_str2(s):
    rev = ''
    for i in range(len(s)-1,-1,-1):
        rev +=s[i]

    return rev

print('reversed str2:',reverse_str2('Singh'))




# 9.	Write a Python program to check whether a string is a palindrome. Example: "madam" → Palindrome.
def is_palindrome(s):
    rev = ''
    for i in s:
        rev = i + rev

    if rev == s:
        return 'Palindrome string'
    else:
        return 'not a palindrome'
    


print('palindrome check:',is_palindrome('viv'))



def palindrome2(s):
    return s == s[::-1]

print('is palindrome:',palindrome2('Vikram'))


# 10.	Write a Python program to check whether two strings are equal without using == directly on the strings.
def check_equal(s1,s2):
    if len(s1) != len(s2):
        return 'Not equals'
    
    for i in s1.lower():
        if i not in s2.lower():
            return 'Both strings are Not equal'

    return 'Both strings are equal'


print(check_equal('Vikram','VikraM'))




# 11.	Write a Python program to print the first and last character of a string.
def first_last(s):
    first = s[0]
    last = s[-1]

    return first,last

print('first and last character:',first_last('Vikram'))


# 12.	Write a Python program to print the characters at even indexes of a string

def even_indx_char(s):
    evenIndexCharacter = ''
    for i in range(len(s)):
        if i%2==0:
           evenIndexCharacter+=s[i] + ' '
    return evenIndexCharacter

print('even index character:',even_indx_char('Vikram'))



# 13.	Write a Python program to count how many times a particular character appears in a string. Example: "banana", character = "a" → 3.
def particular_char_count(s,char):
    count = 0
    for i in s:
        if i == char:
            count +=1

    return count


print('character count is:',particular_char_count('Python is easy language','a'))



# 14.	Write a Python program to find the first occurrence of a character in a string without using find().
def first_occurrence(s):
    word = ''
    for i in s:
        if i not in word:
            word += i
        else:
            return i
            


print('first occurence is:',first_occurrence('supercalifragilisticexplodicious'))



# 15.	Write a Python program to print all characters that appear more than once in a string.
def all_duplicate_elements(s):
    dic ={}
    for i in s:
        if i in dic:
            dic[i] +=1
        else:
            dic[i]=1
    # now for duplicate elements
    ans = ''
    for i,v in dic.items():
      
        if v >1:
            ans += i +' '

    return ans

print('duplicate characters are:',all_duplicate_elements('vikramsinghnv'))



# 16.	Write a Python program to remove all spaces from a string without using replace().
def remove_space(s):
    ans = ''
    for i in s:
        if i!=' ':
            ans+=i

    return ans

print('space removed:',remove_space('python is easy'))




# 17.	Write a Python program to remove duplicate characters from a string. Example: "programming" → "progamin".
def remove_duplicate(s):
    ans =''
    for i in s:
        if i not in ans:
            ans +=i

    return ans

print(remove_duplicate('programming'))