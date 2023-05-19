'''Sukurti programą, kuri:
• Leistų vartotojui įvesti norimą eilučių kiekį
• Įrašytų įvestą tekstą atskiromis eilutėmis į failą
• Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą

Patarimai:
• Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)
'''

file_name = input("Iveskite failo pavadinima: ")
text = ""
while True:
    input_string = input("Įveskite tekstą: ")
    text += input_string + "\n"
    if not input_string:
        break

with open(f"2_uzd_{file_name}.txt", 'w', encoding='utf-8') as f_out:
    f_out.write(text)