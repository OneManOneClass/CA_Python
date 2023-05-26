'''Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių, kuriuos reikia jame išcenzūruoti sąrašą.
 Pvz, žodis "kvaraba" yra baisus keiksmažodis, ir mums reikia duotame tekste pakeisti k*****a.'''

import re


def cenzura(tekstas, *keiksmai):
    print(f'Tekstas be cenzūros: {tekstas}')
    censored_list = []
    for keiksmas in keiksmai:
        if len(keiksmas) < 3:
            print(f'Žodis "{keiksmas}" yra per trumpas cenzūrai')
        else:
            censored_list.append(keiksmas)
            # cenzuruota = keiksmas[0] + '*' * len(keiksmas) + keiksmas[-1]  #censor using string operations (easy)
            cenzuruota = re.sub(r'(?<=\w)\w(?=\w)', '*', keiksmas)  # censor using regex (not so easy)
            tekstas = re.sub(r'\b' + re.escape(keiksmas) + r'\b', cenzuruota, tekstas, flags=re.I)

    print(f'Cenzūruojami žodžiai: {", ".join(censored_list)}')
    print(f'Cenzūruotas tekstas: {tekstas}')


cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')
cenzura('this is a test string to test how censoring given words that are longer than 3 characters work'
        , 'is', 'test', 'to')