fid = open("abcd.txt","w")
fid.write("hello world")


fid = open("abcd.txt","r")
tmp = fid.read()
print(tmp)

fid = open("abcd.txt",'w')
fid.write("hello right now iam learning file handling in python\n")



a = ['hello world \n','iam learning file handling \n',"python is high level programming language"]
fid = open("abcd.txt","a")
fid.writelines(a)     #writelines is used to append or store multiple lines

fid = open("abcd.txt","r")
tmp = fid.read()
print(tmp)

print()
fid = open("abcd.txt","r")
tmp = fid.read()
print(tmp)


fid = open("abcd.txt","a")
fid = fid.write("data science")


# fid.seek(5)
fid = open("abcd.txt","r")
fid.read()

# for length of data in file
file = open("abcd.txt","r")
data = file.read()
count = len(data)
print("number of character:",count)


fid = open("abcd.txt","r")
print(fid.readline())      #readline is used to read only single line


fid = open("abcd.txt","r")
print(fid.readlines())      #readlines is used to read whole content in file


# for reading second line
fid = open("abcd.txt","r")
fid.readline()
second = fid.readline()
print("second line in file is:",second)



# for sace count
count = 0
with open("abcd.txt","r") as file:
    for line in file:
        for char in line:
            if char == " ":
                count+=1
print("number of word:",count)


# for character count without space
count = 0
with open("abcd.txt","r") as file:   
    for line in file:
        for char in line:
            if char != " ":
                count+=1
print("number of space:",count)


# w+ means first write and then read
#r+ means first read and then write

fid = open("abcd.txt","w+")
fid.write("debugShala")
# fid.seek(0)     # it moves cursor from last point to 0 because we seek 0
fid.seek(5)
print(fid.tell())
print(fid.read(5)) 



# x action in file handling it gives error if file is already exists 
with open("data.txt","x") as file:
    file.write("hello world")    #it creates new file because file is not exists



# with open("data.txt","x") as file:
#     file.write("hello world")     #this time it throws error bcoz file already exists