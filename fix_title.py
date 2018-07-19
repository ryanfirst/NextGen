def fixed_title(title):
    title = title.lower()
    title = title.split()
    for i in range(len(title)):
        if title[i] not in ('a', 'the', 'and', 'in', 'of', 'an'):
            title[i] = title[i].capitalize()
    title = ' '.join(title)
    return title



title = ['the Tale Of two Cities', 'wind In The willows', 'GONE WITH THE WIND', 'about A Boy']
print(fixed_title(title[1]))

