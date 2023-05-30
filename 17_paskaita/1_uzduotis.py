'''Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next grąžintų sekantį porinį skaičių.
Pirmas sk. 2, toliau 4 ir taip be pabaigos.'''

def poriniai(iki):
    count = 2
    while count <= iki:
        yield count
        count +=2

counter = poriniai(20)

while True:
    try:
        print(next(counter))
    except StopIteration:
        break