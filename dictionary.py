d = {'name': ['vikram','singh'],'age':[20,30]}
d['age'][1] = 100
print(d)
print(d['age'])

d = dict()
type(d)


students = {'vikram': {'python' : 90, 'sql' :80, 'maths':30}}
total = sum(students['vikram'].values())
print(total)
students.items()
students.keys()


students = {'vikram': {'python' : 90, 'sql' :80, 'maths':30}}
print(students.items())
print(students.keys())
print(students['vikram'].keys())    # for keys 
print(students['vikram'].values())   #for values


d = {'name': ['vikram','singh'],'age':30}
d.update({'age':89})
print(d)
print(d.pop('name'))   
print(d)
print(d.get('name'))
print(d.popitem())
print(d)

del d['age']    # del is python method used to delete 
print(d)

st = {
    'name' : ['vikram','pulkit','sawan','abhishek'],
    'id' : ['dcddc','ddcd','vvvv','tttt'],
    'marks' : [[20,30,40,50],[20,30,40,70],[20,3,45,63],[2,3,4,5]]

}
for i in range(len(st['name'])):
    print("name :",st['name'][i])
    print("id :",st['id'][i])
    print('marks :',st['marks'][i])
    print()



# create a dictionary and print keys and values
student = {
    'name':'vikram','age':22,'city':'indore'
}
# student.items()
for key , value in student.items():
    print(key, ":" ,value)


str = input("enter string:")
freq = {}
for ch in str:
    freq[ch] = freq.get(ch,0)+1
print(freq)

sen = input("enter ur sentence:")
words = sen.split()
freq = {}

for i in words:
    freq[i] = freq.get(i,0)+1
print(freq)


data = {
    'a':50,'b':20,'c':40
}
lar = float("-inf")
for k, v in data.items():
    if v > lar:
        lar = v
        word=k
print(word, lar)

maxKey = max(data , key = data.get)      #by using max method
print(maxKey, ":", data[maxKey])


str = "vikram"
freq = {}
for ch in str:
    # freq[ch] = freq.get(ch,0)+1
    freq[ch] = str.count(ch)
print(freq)

sen = "vikram is a good boy"
words = sen.split()
freq = {}
for i in words:
    # freq[i] = freq.get(i,0)+1
    freq[i] = words.count(i)
print(freq)


# find the length of a dictionary without using len() function
data = {
    'a':50,'b':20,'c':40
}
count = 0
for i in data:
    count += 1
print(count)


#invert a dictionary (handle duplicate values)
data = {
    'a':50,'b':20,'c':40 ,'d' : 20
}
inv = {}
for k, v in data.items():
    if v not in inv:
        inv[v] = [k]
    else:
        inv[v].append(k)
print(inv)


# merge two dictionaries 
data1 = {
    'a':50,'b':20,'c':40
}
data2 = {
    'a':50,'b':20,'c':40 ,'d' : 20
}
res = data1.copy()
for k, v in data2.items():
    if k in res:
        res[k] += v
    else:
        res[k] = v
print(res)


# count the frequency of each character in a paragraph
str = """Python is easy to learn. 
python is powerful
python is popular""" 

words = str.lower().replace(".","").split()
freq = {}
# for i in words:
#     freq[i] = freq.get(i,0)+1
# print(freq
# )

for i in words:
    if i in freq:
        freq[i] += 1
        
    else:
        freq[i] = 1

print(freq)




# filter a dictionary based on a threshold
data = {
    'a':50,'b':20,'c':40 ,'d' : 20
}

threshold = 30
res = {}
for k, v in data.items():
    if v > threshold:
        res[k] = v    
print(res)


# make a value to key and key to value dictionary
data = {
    'a':50,'b':20,'c':40 ,'d' : 20
}
res = {}
for k, v in data.items():
    res[v] = k
print(res)




# common question
# fibonacci series
# palindrome
# factorial
# armstrog
# anagram
# prime number
# leap year

# count the freq of words in string
# move all the zeroes to the end of the list
# find second maximum from a list
# convert the keys to the values and values to the keys
# find all the pairs whose sum equals to target
# move all negative numbers to the begning
# count the vowels and consonants in a string
# write a code for atm machine for withdraw deposit and check balance
# list intersaction and union of two lists
# write a code for rotate a tuple and list by k position
# find firstnon character in a string
# find cmon and duplicate elements in a list
# count the alphabets and numbers in a string
# reverse a given numbers
# find the maximum and minimum value in a dictionary
