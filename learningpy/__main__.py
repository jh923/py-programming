# Imports
import random
import math

# Learning by simple programs

# Initialise a list with pre-set values then apply bubble sort
def bubblesort(list):
    list = list
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                temp1 = list[j]
                temp2 = list[j+1]
                list[j] = temp2
                list[j+1] = temp1

    for i in list:
        print(i)

# Calculate a^b mod c
def bigMod(a, b, c):
    a = a % c
    b = b
    c = c

    # eliminate invalid mod
    if c <= 1:
        return 0

    # quick cases for x mod 2
    if c == 2 and a % 2 == 0:
        return 0
    elif c == 2 and a % 2 == 1:
        return 1

    # reached bottom of recursion
    if b == 1:
        return a

    # Split in half, using recursion
    if b%2 == 0:
        result = (bigMod(a, b//2, c) * bigMod(a, b//2, c) % c)
    else:
        result = (((bigMod(a, b//2, c) * bigMod(a, b//2, c) % c) * a) % c)

    return result


def nBynArray(n):
    n = n
    # Define size of array
    grid = [[0] * n for i in range(n)]
    # Populate array
    for i in range(n):
        for j in range(n):
            grid[i][j] = random.randint(0, 3)
    # Print each array
    for i in range(n):
        print(grid[i])


# init code
bubblesort([10, 21, 17, 102, 291, 1, 20, 39, 12, 934, 38])

# mod = bigMod(12657865, 12691, 123)
# print("\n", mod, "\n")

# nBynArray(10)


age = 21
guess = 0
while True:
    if age == guess:
        break
    guess += 1

print(guess)