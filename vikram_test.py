#1 wap to find the first non-repeating element in a list
def non_repeating(ls):
    for i in ls:
        if ls.count(i) <=1:
            return i
print(non_repeating([1,2,3,4,5,6,7,8,2,3,4]))

#2write a python program to check whether a given string is a palindrome
def ispalindrome(s):
    rev = ""
    for i in range(len(s)-1,-1,-1):
        rev +=s[i]
    
    if rev == s:
        print("palindrome")
    else:
        print("not palindrome")

ispalindrome("viv")

#3 star pattern
def star_pattern(n):
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end="")
        print()

star_pattern(5)


4# sort a dictionary by its values
d = {"a": 1, 'b': 2, 'c': 3, 'd': 4}
ans = sorted(d.items(), key=lambda x: x[1])
print(ans)

#5 write a python program read a sentence and print longest word in sentence
sentence = "My name is vikram"
words = sentence.split()
long = ""
for i in words:
    if len(i) > len(long):
        long = i
print("longest word in the sentence:",long)



#6reverse a dic swap keys and values
def swap(d):
    ans = {}
    for i in d:
        ans[d[i]] = i
    return ans
print(swap({1:"vikram",2:"singh",3:"thakur"}))




#7 move zeroes
def move_zeroes(ls):
    j = 0
    for i in range(len(ls)):
        if ls[i] != 0:
            ls[i],ls[j] = ls[j],ls[i]
            j+=1
    return ls

print("moved zeroes till the end:",move_zeroes([0,9,3,0,2,0,3,0,23,3,22,3,0]))



#8 find longest palindrome
sentence = "madam, level and malayalam"
longest = ""
words = sentence.split()
for i in words:
    i = i.strip("!?,.")
    if i == i[::-1]:
        if len(i) > len(longest):
            longest = i

print(longest)




#9 second largest in a list
def second_lar(ls):
    lar = float("-inf")
    sec = float("-inf")
    for i in ls:
        if i > lar:
            sec = lar
            lar = i
        if i > sec and i != lar:
            sec = i
    return sec
print("second largest elemnt in list:",second_lar([1,2,3,4,5,7,6]))



# 10 check anagram
def is_anagram(s1,s2):
    anagram = True
    if len(s1) != len(s2):
        anagram = False
    for i in s1:
        if s1.count(i) != s2.count(i):
            anagram= False

    if anagram :
        print("it is anagram")
    else:
        print("it is not anagram")

is_anagram("silent","listen")



def toggle(s):
    togle = ""
    for i in s:
        if i.islower():
            togle += i.upper()
        elif i.isupper():
            togle += i.lower()
        else:
            togle += i
    return togle
print(toggle("VikrAm"))



        
