# Author: IBN (AMDG) 12/3/2021

total = 0
while True:
    number = int(input("Give me a number: "))
    if number == -1:
        break
    else:
        total += number

print(total)
