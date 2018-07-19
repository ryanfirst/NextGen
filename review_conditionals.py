word = input('Please pick a word')
if word[-1] in ('x' 's'):
    print(word + 'es')
elif word[-2:] in ('th', 'sh', 'ch'):
    print(word + "es")
else:
    print(word + 's')

#bin-max
highest_num = 0

places = 20

for p in range(places):
    highest_num += 2 ** p
    print(highest_num)