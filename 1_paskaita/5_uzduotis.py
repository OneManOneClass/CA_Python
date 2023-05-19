'''Parašyti programą, kuri:
• Leistų įvesti skaičių
• Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
• Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
• Išvesti į ekraną „Skaičius dalinasi iš 3“, jei skaičius dalinasi iš trijų
Patarimas: naudoti input(), if, print, %, <, > '''

a = int(input("Iveskite skaiciu a: "))
if a % 2 == 0:
    print("Skaicius yra lyginis")
else:
    print("Skaicius yra nelyginis")
if a % 3 == 0:
    print("Skaicius dalinasi is 3")
