'''Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
• Gražina tekstą atbulai
• Gražina tekstą mažosiomis raidėmis
• Gražina tekstą didžiosiomis raidėmis
• Gražina žodį pagal nurodytą eilės numerį
• Gražina, kiek tekste yra nurodytų simbolių arba žodžių
• Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
• Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
Susikurti kelis klasės objektus ir išbandyti visus metodus
'''

class Sakinys:
    def __init__(self, tekstas="This text is default 1 12 123"):
        self.tekstas = tekstas
        self.word_count = 0
        self.upper_count = 0
        self.lower_count = 0
        self.num_count = 0

    def reverse(self):
        return self.tekstas[::-1]

    def to_lower(self):
        return self.tekstas.lower()

    def to_upper(self):
        return self.tekstas.upper()

    def return_word(self, indeksas):
        txt_list = self.tekstas.split()
        return txt_list[indeksas]

    def count_chars(self, ieskomas):
        return self.tekstas.count(ieskomas)

    def change(self, tekstas1, tekstas2):
        return self.tekstas.replace(tekstas1, tekstas2)

    def count_all(self):
        words = self.tekstas.split()
        word_count = len(words)
        upper_count = sum(1 for c in self.tekstas if c.isupper())
        lower_count = sum(1 for c in self.tekstas if c.islower())
        num_count = sum(1 for c in self.tekstas if c.isnumeric())
        return word_count, upper_count, lower_count, num_count

    def __repr__(self):
        return self.tekstas


def menu():
    sakinys = Sakinys()
    while True:
        pasirinkimas = int(input(
            "Pasirinkite:\n"
            "1 - Įvesti tekstą\n"
            "2 - Tekstas atbulai\n"
            "3 - Tekstas mažosiomis raidėmis\n"
            "4 - Tekstas didžiosiomis raidėmis\n"
            "5 - Grąžinti žodį pagal nurodytą eilės numerį\n"
            "6 - Grąžinti kiek tekste yra nurodytų žodžių/simbolių\n"
            "7 - Grąžinti tekstą su pakeistu nurodytu žodžiu/simboliu\n"
            "8 - Tekste esančių žodžių, didžiųjų/mažųjų raidžių, skaičių kiekis\n"
            "9 - Uždaryti programą   "))

        if pasirinkimas == 1:
            tekstas = input("Įveskite tekstą: ")
            sakinys = Sakinys(tekstas)

        if pasirinkimas == 2:
            print(f"Tekstas atbulai: {sakinys.reverse()}")

        if pasirinkimas == 3:
            print(f"Tekstas mažosiomis raidėmis: {sakinys.to_lower()}")

        if pasirinkimas == 4:
            print(sakinys.to_upper())

        if pasirinkimas == 5:
            indeksas = int(input("Įveskite indeksą: "))
            print(f"Žodis/simbolis nr.{indeksas - 1}: {sakinys.return_word(indeksas - 1)}")

        if pasirinkimas == 6:
            char = str(input("Įveskite ieškomą žodį/simbolį: "))
            print(f'Tekste "{sakinys.tekstas}" rasta "{char}" {sakinys.count_chars(char)} kartų')

        if pasirinkimas == 7:
            change_what = str(input("Įveskite žodį/simbolį, kurį norite pakeisti: "))
            change_to_what = str(input("Įveskite naują žodį/simbolį: "))
            print(f"Naujas tekstas: {sakinys.change(change_what, change_to_what)}")

        if pasirinkimas == 8:
            print(f"Jūsų tekstas: {sakinys}")
            print("Tekste rasta: ")
            print(f"Žodžių: {sakinys.count_all()[0]}")
            print(f"Didžiųjų raidžių: {sakinys.count_all()[1]}")
            print(f"Mažųjų raidžių {sakinys.count_all()[2]}")
            print(f"Skaičių: {sakinys.count_all()[3]}")

        if pasirinkimas == 9:
            print("Viso gero!")
            break


menu()
