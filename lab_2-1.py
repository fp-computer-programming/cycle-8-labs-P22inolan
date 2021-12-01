# Author: IBN (AMDG) 12/1/2021


def ranges(num):
    total = 0
    for value in range(int(num) + 1):
        total += value
    return total


numba = input("give me a number: ")
print(ranges(numba))
