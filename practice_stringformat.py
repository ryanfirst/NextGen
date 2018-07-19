
things = ['camera', 'couch', 'potato salad', 'energy drink', 'comb', 'suitcase']
prices = [50, 100, 5, 5, 1, 25]

for i in range(len(things)):
    new_things = i
    print('{0:>20}:$ {1}.00'.format(things[i], prices[i],))

