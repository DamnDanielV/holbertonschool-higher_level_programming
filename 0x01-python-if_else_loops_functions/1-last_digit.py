#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_pr = ['Last digit of', 'is', 'and is 0', 'and is greater than 5', 'and is less than 6 and not 0']
new_nu = number % 10 if number >= 0 else (abs(number) % 10) * -1
print(string_pr[0], number, string_pr[1], new_nu, string_pr[2] if new_nu == 0 else string_pr[3] if new_nu > 5 else string_pr[4])
