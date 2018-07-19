# import random
#
# def find_max(num1, num2, num3):
#     return max((num1, num2, num3))
#
#
# def sum_num(num1, num2, num3, num4, num5, num6):
#     return sum((num1, num2, num3, num4, num5, num6))
#
#
#
# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
#
# def reverse_str(string):
#     rev = string[::-1]
#     return rev
#
#
# def factorial(num):
#     ans = 1
#     while num != 0:
#         ans = (ans * num)
#         num = num - 1
#     return ans
#
# # pick = (int(input("Pick a number to find the factorial")))
#
# def test_range(n):
#     if n in range(1, 20):
#         return 'That number is in my range'
#     else:
#         return 'That number is not in my range'
#
#
# # number = int(input('Pick a number and we will see if it is in my range'))
#
# def count_upper_lower(word):
#     count_uppers = 0
#     count_lowers = 0
#     for w in word:
#         if w == w.lower():
#             count_lowers += 1
#         else:
#             count_uppers += 1
#     return (count_uppers, count_lowers)
#
#
# t = count_upper_lower("Ryan First")
# print(t)
# print('The upper count is', t[0], ', the lower count is', t[1])
#
#
# if __name__ == '__main__':
#     print(factorial(6))
#     print('I am in the module!!')
#
# print(test_range(3))
# print(factorial(3))
# print(reverse_str('Ryan'))
# print(multiply((4, 2, 3, 2)))
# print(sum_num(4, 8, 12, 16, 20, 10))
# print(find_max(96, 69, 11))
# print(find_max(43, 1, 69))


# def mercury(weight):
#     return print('you would weigh', weight ** 0.38, 'pounds on Mercury.')
#
#
# def venus(weight):
#     return print('You would weigh', weight ** 0.91, 'pounds on Venus.')
#
#
# def earth(weight):
#     return print('You weigh', weight, 'pounds.')
#
#
# def mars(weight):
#     return print('You would weigh', weight ** 0.38, 'pounds on Mars.')
#
#
# def jupiter(weight):
#     return print( 'You would weigh', weight ** 2.34, 'pounds on Jupiter.')
#
#
# def saturn(weight):
#     return print('You would weigh', weight ** 1.06, 'pounds on Saturn.')
#
#
# def uranus(weight):
#     return print('You would weigh', weight ** 0.92, 'pounds on Uranus.')
#
#
# def neptune(weight):
#     return print('You would weigh', weight ** 1.19, 'pounds on Neptune.')
#
#
# def pluto(weight):
#     return print('You would weigh', weight ** 0.06, 'pounds on Pluto.')


def get_weight(weight, planet="earth"):
    if planet == "earth":
        return weight
    elif planet == 'mercury':
        return weight ** 0.38
    elif planet == 'venus':
        return weight ** 0.91
    elif planet == 'mars':
        return weight ** 0.38
    elif planet == "neptune":
        return weight ** 1.19
    elif planet == 'pluto':
        return weight ** 0.06
    elif planet == 'uranus':
        return weight ** 0.92
    elif planet == 'saturn':
        return weight ** 1.06


w = int(input("Want to know how much you'd weigh on another planet? Enter your weight!"))
print(get_weight(w))
planet = input('Now choose a planet to live on.')
print('You would weigh', get_weight(w, planet), 'pounds on', planet)