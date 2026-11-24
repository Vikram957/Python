# WAP OF FIBONACCI SERIES
n = 6
a = 0
b = 1
for i in range(n):
    print(a,end=' ')

    c=a+b
    a = b
    b = c 


print()

def remove_duplicate(l):
    ans = []
    for i in l:
        if i not in ans:
            ans.append(i)

    return ans

numbers = [1,2,3,2,5,6,4,7,8,3]
print(remove_duplicate(numbers))


# find common from two list
def common_element(l1,l2):
    ans = []
    for i in l1:
        if i in l2:
            ans.append(i)

    return ans

print('common element:',common_element([1,2,3,4,5,6,7],[1,2,3,7,8,9]))



# reverse string
def reverse_str(s):
    word = ''
    result = ''

    for i in s:
        if i != ' ':
            word += i
        else:
            result = word +' ' + result
            word = ''
    result = word + ' ' + result

    return result.strip()

print(reverse_str('python is a easy language'))
        


list1=[1,2,3,4,5,6]  
rev = []
for i in list1:
    rev = [i] + rev

print("reversed:",rev)




    