from my_package.math_utils import add
print("1st way ",add(2,5))

# 2nd way
from my_package import math_utils
ans = math_utils.add(2,4)
print("2nd way ",ans)