# Author: IBN (AMDG) 12/2/2021


def sum_to(n):
    total = 0
    i = 0
    while i <= n:
        total += i
        i += 1
    return total


def sum_too(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


print(sum_to(5))
print(sum_too(5))
