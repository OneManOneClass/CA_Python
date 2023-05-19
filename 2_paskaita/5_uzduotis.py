'''Sukurti programą, kuri:
• Leistų vartotojui įvesti metus
• Atspausdintų „Keliamieji metai“, jei taip yra
• Atspausdintų „Nekeliamieji metai“, jei taip yra

Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų
'''

input_year = int(input("Iveskite metus: "))
if input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0):
    print("Metai yra keliamieji")
else:
    print("Metai yra nekeliamieji")