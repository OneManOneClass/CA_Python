'''parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd.
Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu.'''

import re

pattern = re.compile(r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})')

while True:
    test_date = input("Įveskite norimą datą(dd.mm.yyyy): ")
    result = pattern.search(test_date)
    if test_date == "":
        break
    elif result:
        print(result.group())
        print(f'Metai: {result.group("year")} Mėnuo: {result.group("month")} Diena: {result.group("day")}')
    else:
        print("Pateikti neteisingi duomenys")

