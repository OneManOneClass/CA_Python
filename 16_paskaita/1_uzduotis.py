'''Parašykite dekoratorių kuris riboja parametrų kiekį (tarkime, ne daugiau negu 2 parametrai funkcijai)'''
from numpy import prod

def two_args(fn):
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return 'Perduoti daugiau nei 2 argumentai!'
        return fn(*args)

    return wrapper


@two_args
def sum_of_two(*args):
    return sum(args)

@two_args
def multiply(*args):
    return prod(args)

print(sum_of_two(12, 13))
print(sum_of_two(12, 13, 14))

print(multiply(2, 3))
print(multiply(2, 3, 4))