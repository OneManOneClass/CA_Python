'''Sukurti programą, kuri:
• Leistų vartotojui įvesti 5 žodžius
• Pridėtų įvestus žodžius į sąrašą
• Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index
'''

word_list = []
list_lenght = int(input("Kiek zodziu norite ivesti? "))
for x in range(list_lenght):
    word_list.append(input(f"Iveskite #{x + 1} zodi"))

for x in range(list_lenght):
    print(f"Zodis: {word_list[x]}; Ilgis: {len(word_list[x])}; Vieta sarase: {word_list.index(word_list[x])+1}")