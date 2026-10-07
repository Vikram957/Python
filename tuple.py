# t = (1,2,3,4,5,56,7)
# print(t.count(7))
# print(t.index(7))

# print(sum(t))
# print(min(t))
# print(max(t))
# print(sorted(t))
# print(sorted(t,reverse=True))


# t = (1,2,1,3,2,1)
# for i in t:
#     count = 0

#     for j in t:
#         if i == j:
#             count += 1
#     print(i, ':', count)


# t = (1,2,1,3,2,4)
# unique = []

# for num in t :
#     if num not in unique:
#         unique.append(num)

# tuple(unique)

# print(unique)


numbers = (1,2,3,4,5)
tar = 6

pair = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == tar:
            pair.append((numbers[i],numbers[j]))

print(pair)