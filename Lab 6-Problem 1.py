# Name- Alexander Koschnitzki
# Date- 11-4-21
# CSS - 225

# Problem 1
# In this program, it is able to print a list of
# 10 random number on the same line that are between
# 25 and 35. The numbers are always random.

import random
random_list = []
for i in range(1, 11):
    random_list.append(random.randrange(25, 35))
print(random_list)



