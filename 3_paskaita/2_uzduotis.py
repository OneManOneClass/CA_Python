'''Parašyti programą, kuri:
• Atspausdintų dabartinę datą ir laiką
• Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
• Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
• Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
Patarimas: naudoti datetime, timedelta (from datetime import timedelta)
'''

import datetime

now_datetime = datetime.datetime.now()
print(f"{'Dabartis:' :<25}{now_datetime}")
print(f"{'T - 5d =:':<25}{now_datetime - datetime.timedelta(days=5)}")
print(f"{'T + 08:00 =:':<25}{now_datetime + datetime.timedelta(hours=8)}")
print(f"{'YYYY MM DD, hh:mm:ss:':<25}{now_datetime.strftime('%Y %m %d, %H:%M:%S')}")
