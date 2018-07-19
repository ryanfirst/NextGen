# import random
# win = random.randint(1, 5)
# message = ('you win')
#
# guess = int(input('pick a number between 1 and 5'))
# if guess == win:
#     print('Congratulations, you won!!')
# elif guess < win:
#     print('Wow, you guessed too low')
# elif guess > win:
#     print('you guessed too high get outta here')
# print(win)
# job = input('would you like to apply for a job?')
# if job == "no":
#     print("okay, goodbye!")
# elif job == "yes":
#     experience =input("do you have experience in the work force?")
#     if experience == "no":
#         print("you may apply for an entry level job!")
#     elif experience == "yes":
#         work = (int(input('how many years have you been working?')))
#         if work >= 3:
#             print("you may apply for an advanced position.")
#         if work <= 3:
#             print("you may apply for a mid-level position.")
# hungry = input('are you hungry?')
# money = input('do you have money?')
# if hungry and money == 'yes':
#     print('here is a takeout menu.')
# elif hungry == 'yes' and money == 'no':
#     print('time to heat up some leftovers')
# elif hungry == 'no' and money == 'yes':
#     print('buy yourself something nice!')
# elif hungry == 'no' and money == 'no':
#     print('lets read a book!')
# import random
# number = random.randint(1, 6)
# number2 = random.randint(1, 6)
# if number == number2:
#     print('Congrats you won!!')
# elif number + number2 == 6:
#     print('Congrats you won!!')
# elif number + number2 == 3:
#     print('Congrats you won!!')
# elif number + number2 != 6:
#     print('Sorry, you lost.')
# elif number != number2:
#     print('Sorry, you lost.')
# elif number + number2 != 3:
#     print('Sorry, you lost.')
operand_one = int(int(input("enter operand")))
operator = input('Enter + or -')
operand_two = int(input('Enter operand: '))

if operator == '+':
    print(operand_one + operand_two)
elif operator == '-':
    print(operand_one - operand_two)
else:
    print("cant recognize operator")







