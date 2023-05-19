'''Parašyti programą, kuri:
• Leistų vartotojui įvesti skaičių.
• Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
• Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
Patarimas: Naudoti ciklą while, sąlygą if, break'''

sum = 0
while True:
    num = int(input("Iveskite skaiciu: "))
    if num > 0:
        sum += num
    else:
        break
print(f"Ivestu skaiciu suma: {sum}")