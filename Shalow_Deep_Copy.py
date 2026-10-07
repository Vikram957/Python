# Shallow Copy
from copy import copy
list1 = [[1,2],[3,4]]
list2 = list1.copy()

list2[0][0] = 100
print(list1)
print(list2)
print(list1)

import copy
# DEEP COPY
list1 = [[1,2],[3,4]]
list2 = copy.deepcopy(list1)
list2[0][0] = 100
print(list1)
print(list2)
print(list1)