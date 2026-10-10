# print number from 1 to n
# def print_numbers(n):
#     if n==0:
#         return
#     print_numbers(n-1)
#     print(n)

# print_numbers(5)
# print()

# # print number from n to 1
# def print_numbers(n):
#     if n==0:
#         return
#     print(n)
#     print_numbers(n-1)
    
# print_numbers(5)



# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))


def sum_numbers(n):
    if n ==0:
        return 0
    return n%10 + sum_numbers(n//10)
print(sum_numbers(1521))