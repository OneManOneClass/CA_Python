'''Parašyti programą, kuri atspausdintų norimą žodį, kas X sekundžių. Programa turi:
• Gauti sekundes iš vartotojo
• Spausdinti vartotojo įvesta žodį
• Įvedus netinkamą sekundžių formatą, programa turi paprašyti įvesti sekundes iš naujo
'''

import datetime

word = input("Iveskite norima zodi")
while True:
    try:
        seconds = int(input("Iveskite kas kiek laiko zodis bus spausdinamas (s)"))
        break
    except ValueError:
        print("Neteisingai ivestas laikas!")
while True:
    try:
        repeat_count = int(input("Kiek kartu norite pakartoti?"))
        break
    except ValueError:
        print("Ivesti duomenys turi buti skaicius!")

current_repeat_count = 0
prev_time = datetime.datetime.now()
while current_repeat_count < repeat_count:
    current_time = datetime.datetime.now()
    if (current_time - prev_time).seconds >= seconds:
        prev_time = current_time
        print(f"{word} - {datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')}")
        current_repeat_count += 1