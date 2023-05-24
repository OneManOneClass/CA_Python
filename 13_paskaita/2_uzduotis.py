'''Sukurti paleidžiamąjį failą iš programos, kuri:
• Leistų vartotojui įvesti metus nuo ir metus iki
• Atspausdintų visus keliamuosius metus pagal duotą rėžį
• Paleidžiamasis failas turi turėti norimą ikoną'''

year1 = int(input("Iveskite pradžios metus: "))
year2 = int(input("Iveskite pabaigos metus: "))

print(f"Visi keliamieji metai ({year1} - {year2}):")
for y in range(year1, year2 + 1):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        print(y)

input()
