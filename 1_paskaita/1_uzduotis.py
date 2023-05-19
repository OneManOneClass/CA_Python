'''Parašyti programą, kuri:
• Leistų įvesti skaičius a ir b (int arba float)
• Išvestų į ekraną „a mažesnis už b“, jei taip yra
• Išvestų į ekraną „a lygu b“, jei taip yra
• Išvestų į ekraną „a didesnis už b“, jei taip yra
Patarimas: naudoti if, elif, esle sąlygas
'''

a = float(input("Iveskite skaiciu a: "))
b = float(input("Iveskite skaiciu b: "))
if a < b:
    print("a mažesnis už b")
elif a == b:
    print("a lygu b")
else:
    print("a didesnis už b")