# LIST_COMPREHENSIONS
l = [1,2,3,4]
sq = [i**2 for i in l ]
print(sq)

# FINDING CUBE******************
v = [i**3 for i in range(6)]
print(v)

# EVEN AND ODD**************************
list1 = [1,2,3,4,5,6,7,8,9]
even = [i for i in list1 if i %2 == 0]
odd = [i for i in list1 if i%2 != 0]
print("even numbers:",even)
print("odd numbers :",odd)

# even odd
result = ["EVEN" if i%2 == 0 else "ODD" for i in range(5)]
print(result)

result = [f"EVEN: {i}" if i%2==0 else f"ODD: {i}" for i in range(10)]
print(result)


# SWAP CASE
names = ['Vikram','Mangesh','Abhishek']
result = [names.swapcase() for i in names]
print(result)


# LENTGH OF EACH WORD
words = ['python','Vikram','Science']
ans = [len(i) for i in words]
print(ans)

# FIRST CHARACTER OF EACH WORD
words = ['apple','mango','grapes']
first = [i[0] for i in words]
print(first)


# reverse each string
words = ['apple','mango','grapes','vikram']
reversed = [i[::-1] for i in words]
print(reversed)

words = ['apple','mango','grapes','vikram']
result = [w for w in words[::-1]]
print(result)


text = "python is easy"
words = text.split()
rev_words = " ".join([words[i]for i in range(len(words)-1,-1,-1)])
print(rev_words)

texts = ['data science' , 'machine learning']
result = [ch.replace(" ","") for ch in texts]
print(result)

nums = [1,2,3,-1,-3]
ans = [i for i in nums if i > 0]
print(ans)


nums = [1,2,3,4,-4,-5]
ans = [i if i >= 0 else 0 for i in nums]
print(ans)

# numbers divisible by 3 and 5
ans = [i for i in range(1,101) if i % 3 == 0 and i % 5 ==0]
print(ans)

matrix = [[1,2]],[[3,4]],[[5,6]]
flat = [num for row in matrix for num in row]
print(flat)

# FIND VOWELS 
text = 'data science'
vowels = [i for i in text if i.lower() in 'aeiou']
print(vowels)



text = 'ab17c13hc'
digits = [i for i in text if i.isdigit()]
print(digits)


# FIND COMMON ELEMENTS IN 2 LIST
a = [1,2,3,4,5]
b = [1,2,3,6,7,4]
ans = [i for i in a if i in b]
print(ans)



# FIND UNIQUE ELEMENTS USING LIST COMPREHENSIONS
l = [1,2,3,4,3,6,2]
ans = [i for i in l if l.count(i) == 1]
print(ans)



# FILTER LONG WORDS
words = ['AI','PYTHON','DATASCIENCE','MATHS']
ans = [i for i in words if len(i) > 5]
print(ans)



# CARTESIAN PRODUCT OR PAIRS FROM 2 LIST
colors = ['red','blue','green']
size = ['S','M','L','XL']
ans = [(i,j)for i in colors for j in size]
print(ans)
