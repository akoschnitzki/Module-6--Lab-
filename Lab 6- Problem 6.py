# Name- Alexander Koschnitzki
# Date- 11-4-21
# CSS - 225

# Number 6
# What this program does is that it calculates the factorial of a number
# when you input it. You can input any number and it can be able to
# find the factorial of it.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))