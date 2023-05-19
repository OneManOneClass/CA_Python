'''Sukurti programą, kuri:
• Sukurtų sąrašą iš skaičių nuo 0 iki 50
• Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
• Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
• Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
• Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
• Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai

Patarimai:
• Naudoti map, filter arba comprehension, sum, min, max, mean, median, %
• from statistics import mean, median
'''

from statistics import mean, median


list1 = list(range(51))
print(f"Sąrašas * 10 :{[x*10 for x in list1]}")
print(f"Sąrašas skaičiai, kurie dalinasi iš 7: {[x for x in list1 if x % 7 == 0]}")
sqr_list = [x ** 2 for x in list1]
print(f"Sąrašas kvadratu: {list(sqr_list)}")
print(f"Kvadratų suma: {sum(sqr_list)}")
print(f"Mažiausias kvadratas: {min(sqr_list)}")
print(f"Didžiausias kvadratas: {max(sqr_list)}")
print(f"Kvadratų vidurkis: {mean(sqr_list):.2f}")
print(f"Kvadratų mediana: {median((sqr_list))}")
print(f"Kvadratų sąrašas atbulai: {sorted(sqr_list, reverse=True)}")


