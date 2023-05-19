'''Sukurti programą, kuri:
• Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
• Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
• Kitu atveju atspausdinti „Laimėjai!“
Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break
'''

import random

print("Sugeneruoti skaiciai: ")
for x in range(3):
    rand_num = random.randint(1, 6)
    print(rand_num)
    if rand_num == 5:
        print("Pralaimejai")
        break
else:
    print("Laimejai")
