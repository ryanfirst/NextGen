import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

file = open('/Users/RyanFirst/Desktop/harrypotter.txt', 'r')
text = file.read()

text = text.lower()
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace(':', '')
text = text.replace(';', '')
text = text.replace('&', '')
text = text.replace(')', '')
text = text.replace('(', '')
# text = text.replace('-', '')
text = text.replace('/', '')

tlist = text.split()
ulist = list(set(tlist))
ulist.sort()

plt.plot(['total words', 'unique words'], [len(tlist), len(ulist)])
plt.show()

adverbs = [word for word in ulist if word.endswith('ly')]
hyphenated = [word for word in ulist if '-' in word]
s_words = [word for word in ulist if word.startswith('s')]

for w in ulist:
    print(w, 'appears', tlist.count(w), 'times')
print(len(tlist))

print(len(set(tlist)))


import random
print(random.choice(tlist))
s = text
text_list = text.split()
print(len(text_list))


for line in file:
    print(line)
file.close()


fo = open('/Users/RyanFirst/Desktop/hp_wordcounts.txt', 'w')
for w in ulist:
    print(w, 'appears', tlist.count(w), file = fo)
#
#

list1 = ('steak ' 'salmon ' 'rice ')
print(list1 + 'stew')

