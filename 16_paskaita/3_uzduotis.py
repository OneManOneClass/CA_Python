'''Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus
 ir turi galimybę būti panaudotas kaip papildomas dekoratorius.'''


def only_strings(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != str:
                return (f'Funkcijai paduotas ne string tipo argumentas! ({arg})')
        return func(*args)

    return wrapper


@only_strings
def string_reverser(text):
    return text[::-1]


@only_strings
def string_concat(*args):
    return ' '.join(string for string in args)


print(string_reverser("Labas vakaras"))
print(string_reverser(16))
print(string_concat("Labas vakaras", "aciu kad susirinkote", "viso gero!"))
