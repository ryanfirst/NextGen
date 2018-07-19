# ans = ('How are you today good sir? I hope you are well.')
# punctuation = ('?', '.', ',', '(', ')')
#
# for p in punctuation:
#     ans = ans.replace(p, ' ')
#
# ans.replace('?', ' ')
#
# ans_tuple = tuple(ans.split())
# print(ans_tuple)
# print('there are', len(ans_tuple), 'words')
#
# names = ('kathy', 'benji', 'ian', 'alejandro')
# for n in names:
#     print('there are', len(n), 'letters in the name', n[0:])

#
# import random
#
# firstnames = ('LeBron', 'Lavar', 'Shaquielle', 'Kobe', 'Giannis', 'Carmelo', 'Danilo', 'Steph', 'Draymond', 'JaVale')
#
# lastnames = ('Beckham Jr.', 'Ocho-Cinco', 'Mangold', 'Brown', 'Jones', 'Norman', 'Elliot', 'Lynch', 'Barkley', 'Bell')
#
# num_names = int(input('How many names?'))
#
#
# #for loop version
# # for n in range(num_names):
# #     print(random.choice(firstnames), random.choice(lastnames), sep= ' ')
#
# # while loop version
# total = 0
# while total < num_names:
#     print(random.choice(firstnames), random.choice(lastnames))
#     total += 1

import random
import time
print("Lets play hangman!")
words = ('Dog', 'Bird', 'Truck',)
secretword = random.choice(words)
tries = 6
for letters in secretword:
    print('_ ', end= '')
guess = input('You have 6 tries to guess the letters of the word, or just guesses the word! Go!')
win = 'Congrats you won!!!'
if guess == secretword:
    print(win)

if guess in secretword:
    print(guess)
    guess2 = input('keep going!')

    if guess2 in secretword:
        print(guess + guess2)
        guess3 = input('Keep going!!!!!')
        dog = (guess + guess2 + guess3)

        if guess3 in secretword and dog == secretword:
            print(dog)
            print(win)

        elif dog != secretword:
            print(dog)
            guess4 = input('a little further')

            if dog + guess4 == secretword:
                print(win)

            elif dog + guess4 != secretword:
                print(dog + guess4)
                guess5 = input('Just one more letter!!!!!!!!!!!!')

                if dog + guess4 + guess5 == secretword:
                    print(secretword)
                    print(win)


# person = 'Henry'
# for letter in person:
#     print(letter)