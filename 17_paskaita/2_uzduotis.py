'''Parašykite generatorių , kuris kas kartą generuotų po vieną Fibonačio sekos skaičių.
(Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233.
Kiekvienas šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai, daugiau google:)'''


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        tmp = b
        b = a + b
        a = tmp


f = fibonacci()
while True:
    action = input('Enter - Fibonacci skaičius, 0 - Išeiti')
    if action == "":
        print(next(f))
    elif action == '0':
        break
    else:
        print("Nežinoma komanda!")
