'''Sukurti programą, kuri:
• Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".
• Atspausdintų tekstą iš sukurto failo
• Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
• Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
• Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
• Atspausdintų visą failo tekstą atbulai
• Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
• Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

Patarimai:
• Naudoti from datetime import datetime, datetime.today()
• Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
• Kai kur galima panaudoti funkcijas iš praeitų pamok'''

from datetime import datetime
import fileinput
import sys


def count_all(text):
    words = text.split()
    word_count = len(words)
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    num_count = sum(1 for c in text if c.isnumeric())
    return word_count, upper_count, lower_count, num_count


# Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".

zen = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

txt_file = "Tekstas"
txt_file_upper ="Tekstas_upper"
with open(f"1_uzd_{txt_file}.txt", 'w', encoding='utf-8') as f_out:
    f_out.write(zen)

# Atspausdintų tekstą iš sukurto failo

with open(f"1_uzd_{txt_file}.txt", 'r', encoding='utf-8') as f_in:
    print(f_in.read())

# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką

with open(f"1_uzd_{txt_file}.txt", 'a', encoding='utf-8') as f_out:
    f_out.write(f"\n{str(datetime.today())}")

# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# https://stackoverflow.com/questions/7633485/insert-string-at-the-beginning-of-each-line
line_no = 1
for line in fileinput.input([f"1_uzd_{txt_file}.txt"], inplace=True):
    sys.stdout.write(f"{line_no} {line}")
    line_no += 1

# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."

with open(f"1_uzd_{txt_file}.txt", 'r', encoding='utf-8') as f_in:
    new_zen = f_in.read()

new_zen = new_zen.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
with open(f"1_uzd_{txt_file}.txt", 'w', encoding='utf-8') as f_out:
    f_out.write(new_zen)

# Atspausdintų visą failo tekstą atbulai

with open(f"1_uzd_{txt_file}.txt", 'r', encoding='utf-8') as f_in:
    reverse_zen = f_in.read()
print(reverse_zen[::-1])

# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

with open(f"1_uzd_{txt_file}.txt", 'r', encoding='utf-8') as f_in:
    text = f_in.read()

print(f"Tekste rasta:\n"
      f"Žodžių: {count_all(text)[0]}\n"
      f"Didžiųjų raidžių: {count_all(text)[1]}\n"
      f"Mažųjų raidžių: {count_all(text)[2]}\n"
      f"Skaičių: {count_all(text)[3]}")

# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

with open(f"1_uzd_{txt_file}.txt", 'r', encoding='utf-8') as f_in:
    with open(f"1_uzd_{txt_file_upper}.txt", 'w', encoding='utf-8') as f_out:
        for read_line in f_in:
            f_out.write(read_line.upper())
