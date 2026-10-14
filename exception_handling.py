try:
    fid = open("acd.txt","r")
except FileNotFoundError:
    print("File is not present, skipping the reading process...")
else:
    print(fid.read())



try:
    fid = open("abcd.txt","r")
except FileNotFoundError:
    print("File is not present, skipping the reading process...")
else:
    print(fid.read())




try:
    fid = open("my_data.txt","x")
    fid.write("hello world, hello world")
except (FileNotFoundError,IOError):
    print("Error in opening file or writing")
else:
    fid.close()
    print("file created and closed")



# USING MULTIPLE EXCEPT CLAUSES:
try:
    fid = open("abcd.txt","x")
    fid.write("hello world")
except FileNotFoundError:
    print("File not found error:")
except IOError:
    print("Input output error")
else:
    fid.close()
    print("file closed")



# FINALLY KEYWORD 
# fid = open("abcd.txt","w")
try:
    fid = open("abcd.txt","w")
    fid.write("hello iam vikram")
except IOError:
    print("Write operation failed")
else:
    print("write operation successfully, no error found")
finally:
    print("i will execute no matter what, because iam inside finally block")





try:
    fid = open("abd.txt","r")
    fid.write("hello")
except Exception as err:
    print("error detected:",err)



try:
    a = 10
    b = 0
    c = a // b
except Exception as err:
    # print("error name:", type(err).__name__)    THIS WILL GIVES YOU EXACT NAME OF THE ERROR
    print("error found:",err)
else:
    print("no error found")
finally:
    print("iam finally block")




try:
    number = int(input("enter a divisor: "))
    result = 10 / number
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("please enter a valid integer")
else:
    print("no error found: The Result is",result)
finally:
    print("cleaning up resources and exiting")



