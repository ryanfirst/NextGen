# things = ['hat', 'cat', 'book']
# for i in range(len(things)):
#     things[i] = things[i] + 's'
# print(things)
#
# nums = [1, 2, 3, 4, 5, 6]
# for i in range(len(nums)):
#     nums[i] = nums[i] * nums[i]
# print(nums)

# weights = [
#     ['dog', 30],
#     ['mug', 2],
#     ['book', 4]
# ]
# new_list = weights.append(['trucks', 5000])
# print(weights)
#
# for i in range(len(weights)):
#     print('a', weights[i][0], 'weighs', weights[i][1], 'pounds')


# targets = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
#
# for i in targets:
#     print(i, end= "   ")
#
# import random
# prize_spot = random.randint(0, 9)
#
# player_guess = -1
#
# tries = 0
#
# while player_guess != prize_spot and tries < 3:
#     player_guess = int(input('\n You have 3 tries to guess where the prize is.'))
#     tries = tries + 1
#
#     if player_guess != prize_spot:
#         targets[player_guess] = 'X'
#     else:
#         targets[player_guess] = '!!@!!'
#         print('You got it!')
#
#     for i in targets:
#         print(i, end="   ")
#
# if tries == 3:
#     print('\nYou are out of guesses')


# scores = [
#     [97, 89, 91],
#     [80, 85, 88],
#     [100, 59, 70]
# ]
# for row in range(len(scores)):
#     for x in range(len(scores[row])):
#         scores[row][x] = scores[row][x] + 3
#
# print(scores)
import random

lightbright = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
board = []
for x in range(10):
    board.append(lightbright.copy())

for row in board:
    for dot in row:
        print(dot, end=' ')
    print()
turns = 10
secret_x = random.randint(0, 9)
secret_y = random.randint(0, 9)

while turns > 0:
        y, x = map(int, input('You have 10 tries to guess the column and row of the secret number, (Example: 1, 2):').strip().split())
        turns = turns - 1

if x == secret_x and y == secret_y:
        print('You got it!')
        board[y][x] = 'X'
        turns = 0
else:
    board[y][x] = '0'
    for row in board:
        for dot in row:
            print(dot, end=' ')
        print()
