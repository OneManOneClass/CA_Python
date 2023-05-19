'''Python faile padaryti šiuos veiksmus (atskirai, ne iškart):
• Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką
(.now().time()).
• Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
• Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.
'''

import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(f"{datetime.datetime.now().time()}\n")

from datetime import date

print(f"{date.today()}\n")

from datetime import date as data

print(f"{data.today()}\n")
