#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# The variable last_digit should store the last digit of the number
# The variable last_digit should be positive if the last digit is greater than 5
# The variable last_digit should be 0 if the last digit is 0
# The variable last_digit should be negative if the last digit is less than 6 and not 0

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
