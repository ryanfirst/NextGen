import random
f = open('/Users/RyanFirst/Desktop/BTTF.txt', 'r')
text = f.read()
text = text.replace('.', '').replace('?', '').replace('!', '').replace(',', '')
tlist = text.split()
ulist = list(set(tlist))
ulist.sort()
print(len(tlist))
rword = (random.choice(ulist).lower())

for r in rword:
    print('_ ', end='')

turn = 0
all_guesses = []

while turn < 10:
    print('\n You have already guessed the letters', all_guesses)
    player_letter = input("Guess a word from the script of back to the future")

    turn = turn + 1

    if player_letter in rword:
        print('Correct!')


    all_guesses.append(player_letter)

    for r in rword:
        if r in all_guesses:
            print(r, end=' ')
        else:
            print('_ ', end='')
if turn + 11:
    print(rword, end=" ")