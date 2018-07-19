# main_courses = ['steak', 'salmon', 'rice']
# main_courses.insert(0, 'stew')
# print(main_courses)
#
#
# # user_courses = input("Pick 3 main courses to eat")
# # main_courses.extend(user_courses.split())
# # print(main_courses)
#
# import random
#
# sides = ['carrots', 'fries', 'salad']
# style = ['seared', 'boiled', 'baked']
#
# print('The special for tonight is', random.choice(style), random.choice(main_courses), 'with',random.choice(sides))



operation = input("enter equation to solve") # 1 + 2 -> should return 3
operation = operation.split()
print(operation)

if operation[1] == '+':
    print(int(operation[0]) + int(operation[2]))
elif operation[1] == '-':
    print(int(operation[0]) - int(operation[2]))
elif operation[1] == '*':
    print(int(operation[0]) * int(operation[2]))
elif operation[1] == '/':
    print(int(operation[0]) / int(operation[2]))
#
#
# list = [4, 3, 9, 2, 1, 1]
# total = 1
# for w in list:
#     total = total * w
#     print(total)
#
