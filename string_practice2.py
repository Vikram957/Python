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




