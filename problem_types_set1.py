# print(int(2.5))
# # year = input('what is your year of birth?')
# # print('you are', end='')
# # print(2018 - int(year))
# a = 3
# b = 5
# c = 7
# # print true if a<b and b>c
# # also print true if a > b and b > c
# print(a > b and b > c)
# print(a < b and b < c)
# use % if year is divisible by 4
# unless it's divisible by 100
# it's okay to be divisible by 100
# if also divisible by 400
import random
year = random.randint(1000, 2018)
print(year, 'was a leap year?')
# print(year % 4 == 0 and year % 100 != 0)
# print((year % 400 == 0) or (year % 100 != 0))
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
print(random.choice(('dog', 'cat', 'bird')))
import time

