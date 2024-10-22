#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10

if number < 0:
    last_num = -last_num  # Preserve negative sign for negative numbers

if last_num < 6 and last_num != 0:
    print(f'Last digit of {number} is {last_num} and is less than 6 and not 0')
elif last_num > 5:
    print(f'Last digit of {number} is {last_num} and is greater than 5')
else:
    print(f'Last digit of {number} is {last_num} and is 0')
