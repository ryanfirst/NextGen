import re
import sys
try:
    f = open('/Users/RyanFirst/Desktop/harrypotter.t', 'r')
    text = f.read()

    f.close()

# print(text[:1000])

    harry_quotes = re.findall('.*Harry.*', text)

# for quote in harry_quotes:
#     print(quote)

    print(len(harry_quotes))

    list = ['dog', 'cat', 'bunny']

    for x in list:
        x = x + 's'
    print(x)
except:
    print('oh naw baby what is you doin')
    e = sys.exc_info()[0]
    print(e)
# text = f.read()
#
# f.close()
#
# # print(text[:1000])
#
# harry_quotes = re.findall('.*Harry.*', text)
#
# # for quote in harry_quotes:
# #     print(quote)
#
# print(len(harry_quotes))
#
# list = ['dog', 'cat', 'bunny']
#
# for x in list:
#     x = x + 's'
#     print(x)