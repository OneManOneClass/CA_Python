'''Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:
• Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
• Gražina, ar nurodytos sukakties metai buvo keliamieji
• Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
• Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
'''

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Sukaktis:
    def __init__(self, date="1993-08-12 16:30:00"):
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def time_passed(self):
        now = datetime.now()
        years = relativedelta(now, self.date).years
        months = relativedelta(now, self.date).months
        days = relativedelta(now, self.date).days
        hours = relativedelta(now, self.date).hours
        minutes = relativedelta(now, self.date).minutes
        seconds = relativedelta(now, self.date).seconds

        return years, months, days, hours, minutes, seconds

    def is_leap(self):
        leap = False
        if self.date.year % 4 == 0 and (self.date.year % 100 != 0 or self.date.year % 400 == 0):
            leap = True
        return leap

    def substract_days(self, n):
        days = int(n)
        return self.date - timedelta(days=days)

    def add_days(self, n):
        days = int(n)
        return self.date + timedelta(days=days)

    def __repr__(self):
        return f"Dabartine data: {self.date}"

    def __str__(self):
        return f"Dabartine data: {self.date}"


def menu(sukaktis):
    while True:
        pasirinkimas = int(input(
            "Pasirinkite:\n"
            "1 - Įvesti sukakties datą\n"
            "2 - Kiek nuo sukakties praėjo laiko?\n"
            "3 - Ar sukakties metai buvo keliamieji?\n"
            "4 - Pridėti prie datos n dienų\n"
            "5 - Atimti iš datos n dienų\n"
            "6 - Uždaryti programą   "))

        if pasirinkimas == 1:
            input_date = input("Formatas: yyyy-dd-mm hh:mm:ss   ")
            sukaktis = Sukaktis(input_date)
        if pasirinkimas == 2:
            print(f"Nuo {sukaktis.date} praėjo: \n"
                  f"Metų: {sukaktis.time_passed()[0]}\n"
                  f"Mėnesių: {sukaktis.time_passed()[1]}\n"
                  f"Dienų: {sukaktis.time_passed()[2]}\n"
                  f"Valandų: {sukaktis.time_passed()[3]}\n"
                  f"Minučių: {sukaktis.time_passed()[4]}\n"
                  f"Sekundžių: {sukaktis.time_passed()[5]}")
        if pasirinkimas == 3:
            if sukaktis.is_leap() == True:
                print(f"{sukaktis.date.year} metai yra keliamieji")
            else:
                print(f"{sukaktis.date.year} metai nėra keliamieji")
            pass
        if pasirinkimas == 4:
            n = input("Įveskite skaičių n: ")
            print(f"{sukaktis.date} + {n}d = {sukaktis.add_days(n)}")
        if pasirinkimas == 5:
            n = input("Įveskite skaičių n: ")
            print(f"{sukaktis.date} - {n}d = {sukaktis.substract_days(n)}")
        if pasirinkimas == 6:
            print("Viso gero!")
            break


sukaktis = Sukaktis()
print(repr(sukaktis))
print(sukaktis)
menu(sukaktis)
