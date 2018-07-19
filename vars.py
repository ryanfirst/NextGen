t = 9
name = 'Mr. T'
animal = 'Hippo'

d = vars().copy()

for k in d:
    if '_' not in k:
        print(k, ':', d[k])

print('__name__ =', d['__name__'])