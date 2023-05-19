'''Parašyti programą, kuri:
• Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
• Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
• Metų
• Mėnesių
• Dienų
• Valandų
• Minučių
• Sekundžių
• Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
Patarimas: naudoti datetime, .days, .total_seconds()
'''

from dateutil.relativedelta import relativedelta
import datetime

while True:
    try:
        input_date = datetime.datetime.strptime(input("Iveskite norima data ir laika (yyyy-dd-mm hh:mm:ss) :"),
                                        "%Y-%m-%d %H:%M:%S")
        break
    except ValueError:
        print("Neteisingai įvesta data!")

now = datetime.datetime.now()
time_diff = input_date - now
print(f"Nuo ivestos datos praejo:\n"
      f"Metu: {relativedelta(now, input_date).years} \n"
      f"Menesiu: {relativedelta(now, input_date).months} \n"
      f"Dienu: {relativedelta(now, input_date).days} \n"
      f"Valandu: {relativedelta(now, input_date).hours} \n"
      f"Minuciu: {relativedelta(now, input_date).minutes} \n"
      f"Sekundziu: {relativedelta(now, input_date).seconds}")
