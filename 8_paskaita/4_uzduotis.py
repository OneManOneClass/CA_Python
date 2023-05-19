'''Sukurti programą, kuri:
• Turėtų klasę Zmogus, su savybėmis vardas ir amzius
• Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
• Inicijuoti kelis Zmogus objektus su vardais ir amžiais
• Įdėti sukurtus Zmogus objektus į naują sąrašą
• Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)

Patarimai:
• Naudoti sorted, attrgetter, reverse, funkciją repr
• from operator import attrgetter
'''

from operator import attrgetter


class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"{self.vardas} {self.amzius}")


def sorter(list, attribute, is_reverse):
    return sorted(list, key=attrgetter(attribute), reverse=is_reverse)


zmones = []
zmones.append(Zmogus("Jonas", 20))
zmones.append(Zmogus("Petras", 45))
zmones.append(Zmogus("Martynas", 19))
zmones.append(Zmogus("Živilė", 22))
zmones.append(Zmogus("Laura", 25))
zmones.append(Zmogus("Rūta", 32))
zmones.append(Zmogus("Monika", 21))

print(f'{"Žmonių sąrašas:":<25}{zmones}')
print(f'{"Pagal vardą: ":<25}{sorter(zmones, "vardas", False)}')
print(f'{"Pagal amžių: ":<25}{sorter(zmones, "amzius", False)}')
print(f'{"Pagal vardą (atbulai): ":<25}{sorter(zmones, "vardas", True)}')
print(f'{"Pagal amžių (atbulai): ":<25}{sorter(zmones, "amzius", True)}')
