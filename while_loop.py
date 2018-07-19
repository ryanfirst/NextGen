import random
secret_num = random.randint(1, 10)
guess = int(input("Guess a number 1 - 10."))

while guess != secret_num:
    if guess > secret_num:
        print('No, too high', end=" ")
    else:
        print('Too low,', end= ' ')
    guess = int(input("Guess a number 1 - 10."))
if guess == secret_num:
    print('Correct! the number was', secret_num, end= '!')
