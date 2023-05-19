'''Sukurti programą, kuri:
• Turėtų klasę Darbuotojas
• Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
• Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki
šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
• Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą
atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
• Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant
darbuotojui 5 dienas per savaitę
• Sukurti norimą Darbuotojo objektą
• Sukurti norimą NormalusDarbuotojas objektą
• Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima'''

from datetime import datetime, timedelta


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.strptime(dirba_nuo, "%Y-%m-%d")
        self.now = datetime.now()

    def _kiek_dirba(self):
        days_worked = (self.now - self.dirba_nuo).days
        return days_worked

    def paskaiciuoti_atlyginima(self):
        total_earnings = int(self._kiek_dirba()) * 8 * self.valandos_ikainis
        return total_earnings

    def get_kiek_dirba(self):
        return self._kiek_dirba()


class NormalusDarbuotojas(Darbuotojas):
    def _kiek_dirba(self):
        total_days = (self.now - self.dirba_nuo).days
        days_worked = sum(1 for day in range(1, total_days + 1) if (self.now - timedelta(days=day)).weekday() < 5)
        return days_worked


darbuotojas = Darbuotojas("Jonas", 9, "2023-05-01")
normalus_darbuotojas = NormalusDarbuotojas("Petras", 5, "2023-04-30")

print(f"{darbuotojas.vardas} įmonėje dirba {darbuotojas.get_kiek_dirba()}d")
print(f"{darbuotojas.vardas} uždirbo: {darbuotojas.paskaiciuoti_atlyginima()}eur")

print(f"{normalus_darbuotojas.vardas} įmonėje dirba {normalus_darbuotojas.get_kiek_dirba()}d")
print(f"{normalus_darbuotojas.vardas} uždirbo: {normalus_darbuotojas.paskaiciuoti_atlyginima()}eur")
