import random

print("Lets play a game! Pick a number between 1 and 10.")
tries = 3
number = input('is it ' + str(random.randint(1, 10)))

while number.lower() == 'no' and tries > 1:

    number = input('is it ' + str(random.randint(1, 10)))
    tries = tries - 1

if number == 'yes':

    print("I knew it!")

else:
    print('I suck')

