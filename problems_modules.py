import random
import time
import statistics

num = int(input('pick a number'))
print(num, 'is a good choice. But did you win?')
ans = random.randint(1,10)
if num == ans:
    print('yes you won!!')
elif num > ans:
    print('too high')
else:
    print('too low')
if ans != num:
    print('sorry', end=' ')
    time.sleep(2)
    print('try again')
time.sleep(2)
print('the correct number was...', end= ' ', flush=True)
time.sleep(3)
print(ans)
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('bitch')
# ages = (18, 20, 21, 17, 15, 16, 20, 18, 21, 17, 22, 14)
# print(statistics.median(ages))
# age = int(input('how old are you'))
# if age >= 18:
#     news= 'riots in the streets'
#     print(news)
# if age <= 18:
#     news2= 'webkinz disabled'
#     print(news2)