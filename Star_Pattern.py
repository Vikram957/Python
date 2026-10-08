# E PATTERN
# n = 7
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n//2 or i == n-1 or j == 0:
#             print("*",end="")
#         # elif j == 0:
#         #     print("*",end ="")
#         else:
#             print(" ",end = "")
#     print()


# PATTERN F
# n = 7
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n//2 or j == 0:
#             print("*",end="")
#         # elif j == 0:
#         #     print("*",end ="")
#         else:
#             print(" ",end = "")
#     print()


# PATTERN H
# n = 7
# for i in range(n):
#     for j in range(n):
#         if j==0 or i == n//2  or j == n-1:
#             print("*",end="")
#         # elif j == 0:
#         #     print("*",end ="")
#         else:
#             print(" ",end = "")
#     print()


# PATTERN I
# n = 7
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j ==n//2 or i == n-1:
#             print("*",end="")
#         else:
#             print(" ",end = "")
#     print()


# PATTERN L
# n = 7
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i == n-1:
#             print("*",end="")
        
#         else:
#             print(" ",end = "")
#     print()


# PATTERN M
# n = 7
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n-1:
#             print("*", end=" ")
#         elif i == j and i <= n//2:
#             print("*", end=" ")
#         elif i + j == n-1 and i <= n//2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # PATTERN X
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == i or j == n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # PATTERN N
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == 0 or j == n - 1 or i == j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# # n = 6
# # for i in range(1,n+1):
# #     for j in range(n-i):
# #         print(end =" ")

# #     for k in range(i):
# #         print("*",end="")
# #     print()

# # for i in range(5,0,-1):
# #     for j in range(i):
# #         print("*",end =" ")

# #     print()

# # DIAMOND PATTERN
# # n = 6
# # for i in range(1,n):
# #     print(" "*(n-i), end = " ")
# #     print("*"*(2*i-1),end="")
# #     print()


# # for j in range(n-1,0,-1):
# #     print(" "*(n-j), end = " ")
# #     print("*"*(2*j-1),end = "")
# #     print()

# # 2ND WAY
# # n = 5
# # for i in range(1,n+1):
# #     print(" "*(n-i) + "*"*(2*i-1))
# # for i in range(n-1,0,-1):
# #     print(" "*(n-i)+ "*" *(2*i-1))


    
# n = 7

# for i in range(n):
#     for j in range(n):
#         if ((j == 0 or j == n-1) and i != 0) or \
#            (i == 0 and j > 0 and j < n-1) or \
#            (i == n//2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# DIAMOND PATTERN 
n = 6
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)    #(2*i-1) for odd_Stars like 1-3-5-7

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


# BUTTERFLY PATTERN
n = 5
for i in range(1,n+1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


