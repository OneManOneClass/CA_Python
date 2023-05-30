'''Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą.
Parašykite generatorių, kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas.
Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. Pabaigus funkciją, praiteruokite sukurtą generatorių
su for ciklu, kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, parašytų 'PIN is XXXX(jųsų pin'as)'.
Atkreipkite dėmesį, kad kodas gali prasidėti nuliu. Sugalvokite, kaip apeiti šią problemą :).'''


def bruteforce():
    a = b = c = d = 0
    while a < 10:
        yield a, b, c, d
        d += 1
        if d > 9:
            d = 0
            c += 1
            if c > 9:
                c = 0
                b += 1
                if b > 9:
                    b = 0
                    a += 1


br = bruteforce()
pin = input('Įveskite PIN kodą (XXXX):')
while True:
    try:
        p = ''.join(map(str, next(br)))
        if p == pin:
            print(f'PIN is {p}')
            break
        else:
            print(p)
    except StopIteration:
        break
