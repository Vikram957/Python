# n = "i love india"
# print(n.capitalize())  #convert 1st word to upper
# print(n.title())    #convert first letter of word capital
# print(n.upper())    # convert all words to upper
# print(n.lower())    #convert all to lower case
# print(n.swapcase())    # convert upper to lower and lower to upper
# print(n.count("0"))    #count frequency
# print(n.find("p"))    #find index  it returns -1 if value is not present in the str
# print(n.index("l"))  #find index  it gives error if value is not present
# print(n.startswith('i'))  # check start letter of str
# print(n.endswith('z'))    # check end letter of str

# w = "programming"
# print(w.isalpha())   # if str contains number or space then gives false if str is fully letter and no space then it gioves true
# print(w.isdigit())   #check numbers
# print(w.isalnum())   # check numbers and alphabets
# print(w.isupper)     # check all is in upper case
# print(w.islower())   # check all is in lower case
# print(w.split())     #tokenization it splits 
# print(''.join(w))    # it joins split str

# sen = "  python is easy language----"
# print(sen.strip("---"))         #it removes extra space and symbol from left and right side
# print(sen.lstrip(" "))          #it is left strip
# print(sen.rstrip("-"))          #right strip
# print(sen.replace("python" , 'java'))



# text = "my name is {}, i am {}".format("vikram",22)     #format string
# print(text)

# w = "WORD HVIKRNJS"
# # x = w.center(50,'0')    #it center the str and add words in left and right side
# # print(x)

# x = w.casefold()
# print(x)



# find the first non repeated character in a string
# text = "abcabcabc" 
# max_count = 0
# max_char = ""
# for i in text:
#     count = 0
#     for j in text:
#         if i == j:
#             count += 1
#     if count > max_count:
#         max_count = count
#         max_char = i
# print("max character is : " + max_char)
# print(max_count)

# #find the first repeated character in a string
# text = "abcabcabc"
# max_count = 0
# max_char = ""
# for i in text:
#     count = 0
#     for j in text:
#         if i == j:
#             count += 1
#     if count == len(text):
#         max_count = count
#         max_char = i

# reverse a string
# text = "abcabcabc"
# print(text[::-1])

# find longest word in a string

# text = "abcabcabc"
# max_len = 0
# max_word = ""
# for i in text.split():
#     if len(i) > max_len:
#         max_len = len(i)
#         max_word = i



# find longest word in a string
# text = "abcabcabc  s v ikkdjdnjdnjd"
# max_len = 0
# max_word = ""
# for i in text.split():
#     if len(i) > max_len:
#         max_len = len(i)
#         max_word = i
# print("max word is : " + max_word)
# print(max_len)


# count vowels consonants and spaces in a string
text = "abcabcabc"
vowels = 0
consonants = 0
digit = 0
spaces = 0
for i in text:
    if i in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digit+=1
    elif i == "":
        spaces += 1

print("vowels :",vowels)
print("consonants :",consonants)
print("spaces : " ,spaces)
print("digit : " , digit)


# find duplicate characters in a string
# text = "abcabcabc"
# count = 0
# for i in text:
#     if i in text[1:]:
#         count += 1
# print("duplicate characters : ",count)



# s = input("Enter a string: ")

# for i in range(len(s)):
#     if s[i] in s[:i]:
#         print(s[i])


