'''Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
Sukurti programą, kuri:
• Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
• Sudėtų ir atspausdintų visus sąrašo žodžius
• Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme

Patarimai:
• Naudoti filter arba comprehension, sum, " ".join()
'''


list1 = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
sum_digits = sum([x for x in list1 if ((type(x) is float) or (type(x) is int))])
words = filter(lambda x: type(x) is str, list1)
sum_true = sum([1 for x in list1 if x is True])

print(f"Sąraše:\nSkaičių suma: {sum_digits:.2f}\nEsantys žodžiai: {' '.join(words)}\nTrue reikšmių: {sum_true}")
