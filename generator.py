def numbers(data):
    for num in data:
        yield(num)  #yield keyword basically generate values one by one 
data = [1,2,3,4,5,6,7,8]

ans = numbers(data)
print(next(ans))
print(next(ans))
print(next(ans))


# SQUARE 
def squares(n):
    for i in range(1,n+1):
        yield i**2

ans = squares(5)
print(next(ans))
print(next(ans))
print(next(ans))



