#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(str(number)[-1])
if lastdigit > 5:
    comp = "and is greater than 5"
if lastdigit == 0:
    comp = "and is 0"
elif lastdigit <= 5:
    comp = "and is less than 6 and not 0"
print(f"Last digit of {number} is {lastdigit} {comp}")
