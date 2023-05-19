'''Parašyti programą, kuri:
• Leistų vartotojui įvesti pradžios ir pabaigos datą
• Suskaičiuotų kiek praėjo sekundžių tarp datų
'''

import datetime

while True:
    try:
        start_date = datetime.datetime.strptime(input("Iveskite pradzios data (yyyy-dd-mm hh:mm:ss) :"),
                                                "%Y-%m-%d %H:%M:%S")
        break
    except ValueError:
        print("Neteisingai įvesta data!")
while True:
    try:
        end_date = datetime.datetime.strptime(input("Iveskite pabaigos data (yyyy-dd-mm hh:mm:ss) :"),
                                              "%Y-%m-%d %H:%M:%S")
        break
    except ValueError:
        print("Neteisingai įvesta data!")

date_diff = 0
if end_date > start_date:
    date_diff = end_date - start_date
else:
    date_diff = start_date - end_date
print(f"Skirtumas tarp datu yra: {int(date_diff.total_seconds())}s")