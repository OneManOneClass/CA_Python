# '''Sukurkite ir išsibandykite funkcijas, kurios:
# 1. Gražinti trijų paduotų skaičių sumą.
# 2. Gražintų paduoto sąrašo iš skaičių, sumą.
# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
# 4. Gražintų paduotą stringą atbulai.
# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
# 7. Gražintų, ar paduotas skaičius yra pirminis.
# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.
# 10. Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių. '''
#
# import datetime
# from dateutil.relativedelta import relativedelta
# from collections import Counter
#
#
# # 1.1-----------------------------------------------
# def count_sum(num1, num2, num3):
#     suma = num1 + num2 + num3
#     return suma
#
#
# print(count_sum(1, 2, 3))
#
#
# # 1.2-----------------------------------------------
# def count_sum_list(list):
#     list_sum = sum(list)
#     return list_sum
#
#
# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30]
# print(count_sum_list(test_list))
#
#
# # 1.3-----------------------------------------------
# def find_max(*args):
#     return max(*args)
#
#
# print(find_max(1, 2, 3, 4, 5, 11, 25, 52, 0, 2, 3, 4))
#
#
# # 1.4-----------------------------------------------
# def reverse_string(string):
#     return string[::-1]
#
#
# print(reverse_string("Random text I've just thought of"))
#
#
# # 1.5-----------------------------------------------
# def string_info(string):
#     words = string.split()
#     word_count = len(Counter(words))
#     upper_count = sum(1 for c in string if c.isupper())
#     lower_count = sum(1 for c in string if c.islower())
#     return word_count, upper_count, lower_count
#
#
# test_string = "Let's test this random string OUT"
# word_count, upper_count, lower_count = string_info(test_string)
# print(f"Tekstas: {test_string}")
# print(f"Tekste zodziu: {word_count}")
# print(f"Didziuju raidziu: {upper_count}")
# print(f"Mazuju raidziu: {lower_count}")
#
#
# # 1.6-----------------------------------------------
# def unique_list(*args):
#     return set(*args)
#
#
# test_list = [1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 16]
# print(unique_list(test_list))
# print(type(unique_list(test_list)))
#
# # 1.7-----------------------------------------------
# from math import sqrt
#
#
# def prime_num(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True, num
#
#
# print(prime_num(17))
#
#
# # 1.8-----------------------------------------------
# def backwards(string):
#     words = string.split()
#     return words[::-1]
#
#
# test_string = "Pirmas antras trecias ketvirtas"
# print(backwards(test_string))
#
#
# # 1.9-----------------------------------------------
# def leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     else:
#         return False
#
#
# test_year = 2049
# print(leap_year(test_year))
#
#
# # 1.10-----------------------------------------------
#
# def elapsed_time(date_string):
#     now = datetime.datetime.now()
#     date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
#     time_diff = date - now
#     print(f"Nuo pateiktos datos praejo:\n"
#           f"Metu: {relativedelta(now, date).years} \n"
#           f"Menesiu: {relativedelta(now, date).months} \n"
#           f"Dienu: {relativedelta(now, date).days} \n"
#           f"Valandu: {relativedelta(now, date).hours} \n"
#           f"Minuciu: {relativedelta(now, date).minutes} \n"
#           f"Sekundziu: {relativedelta(now, date).seconds}")
#
#
# test_date = "2020-04-10 11:12:13"
# elapsed_time(test_date)
