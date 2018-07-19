# residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
# print(residents['Sloth'])
#
# menu = {}   # empty dictionary
#
# menu['Sunday'] = 16.78
# print(menu['Sunday'])
#
# menu['Tuesday'] = 9.28
# menu['Friday'] = 3.01

# for i in menu:
#     print(i, ':', menu[i])

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
                'Sloth' : 'Rainforest Exhibit',
                'Bengal Tiger' : 'Jungle House',
                'Atlantic Puffin' : 'Arctic Exhibit',
                'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
print(zoo_animals)

zoo_animals['Rockhopper Penguin'] = 'Anywhere but the Arctic Exhibit'
print(zoo_animals)


webster = {"Aardvark" : "A star of a popular children's cartoon show.",
           "Baa" : "The sound a goat makes.",
           "Carpet": "Goes on the floor.",
           "Dab": "A small amount."}
for key in webster:
    print(key, ':', webster[key])

my_dict = {'Sports': 'Baseball, Basketball, Football',
           'Music': 'Chance the Rapper, Drake, J.Cole',
           'Food': 'Burgers, Pizza, Chipotle'}
print(my_dict.items())
my_dict.keys()
my_dict.values()
for k,v in my_dict.items():
    print(k, ':', v)