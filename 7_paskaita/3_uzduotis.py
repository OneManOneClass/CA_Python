'''Sukurti programą, kuri:
• Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
• Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
• Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais

Patarimai:
• Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime
'''

import os

directory = "C:\\Users\\Corsair\\Desktop"
folder_name = "Naujas Katalogas"
file_name = "Failas.txt"
try:
    os.chdir(directory)
    os.mkdir(folder_name)
except FileExistsError:
    print(f'Katalogas pavadinimu "{folder_name}" jau egzistuoja!')

os.chdir(directory + "\\" + folder_name)
with open(file_name, 'w') as f_out:
    f_out.write(str(datetime.today()))

print(f'Failas: "{file_name}"\n'
      f'Sukurtas: {datetime.fromtimestamp(os.stat(file_name).st_ctime)}\n'
      f'Dydis: {os.stat(file_name).st_size} B')
