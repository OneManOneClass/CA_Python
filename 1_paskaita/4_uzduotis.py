'''Parašyti programą, kuri:
• Leistų įvesti pirmą skaičių
• Leistų įvesti antrą skaičių
• Paklaustų, kokį matematinį veiksmą reiktų atliktų
• Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.
Patarimas: naudoti input(), if, print'''

a = int(input("Iveskite skaiciu a: "))
b = int(input("Iveskite skaiciu b: "))
num_operator = input("Iveskite operatoriu (+, -, *, /: ")

if num_operator == "+":
    print(a+b)
elif num_operator == "-":
    print(a-b)
elif num_operator == "*":
    print(a*b)
elif num_operator == "/":
    print(a/b)
else:
    print("FAIL")