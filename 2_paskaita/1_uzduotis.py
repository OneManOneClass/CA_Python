'''Sukurti norimą sąrašą ir žodyną ir juose:
• Atspausdinti vieną norimą įrašą
• Pridėti įrašą
• Ištrinti įrašą
• pakeisti įrašą
Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(), remove...
https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/python_ref_dictionary.asp '''

list1 = [1,2,3,4,5,6]
dict1 = {"Vienas":1, "Du":2, "Trys":3}

print(list1[0])
print (dict1["Vienas"])

list1.append(7)
dict1["Keturi"] = 4
print(list1)
print(dict1)

list1.pop(0)
del dict1["Du"]
print(list1)
print(dict1)

list1[1] = 11
dict1["Vienas"]= 70
print(list1)
print(dict1)

print(list1.index(5))
print(dict1.get("Devintas", 9))
print(list1.clear())