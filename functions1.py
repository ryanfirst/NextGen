def make_double(a):
    dbl = a * 2
    return dbl


def make_half(a):
    half = a % 2
    return half


b = make_double(5)
print(b)



def make_plural(word):
    return word + 's'


def get_power(base,exp):
    return base ** exp

print(get_power(8, 2))