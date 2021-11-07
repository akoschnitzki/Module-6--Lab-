# Name- Alexander Koschnitzki
# Date- 11-4-21
# CSS - 225

# Problem 4
# In this problem, it can be able to calculate the
# the approximation of pi. You can be able to input any
# number and it can be able to find the answer.

# import math
# print(math.pi)

def main():
    z = int(input("Please enter a value:"))
    total=0
    for i in range(1, z):
        total += (-1)**(i+1)*((1.0/(i+i+1)))

    value = 4*(1-total)
    print(value)

main()