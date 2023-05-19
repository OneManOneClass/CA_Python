'''Patobulinti 5 pamokos biudžeto programą:
• Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų
visas savybes.
• Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų
įrašyti.
• Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas
galėtų įrašyti.
• Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo,
atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
• Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.
'''

class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return (balansas)

    def parodyti_ataskaita(self):
        if not self.zurnalas:
            print("Įrašų nerasta")
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Išlaidos: {irasas.suma} {irasas.atsiskaitymo_budas} {irasas.isigyta_preke_paslauga}")


def menu():
    while True:
        pasirinkimas = int(input(
            "1 - Įvesti pajamas, \n2 - Įvesti išlaidas, \n3 - Parodyti balansą, \n4 - Pajamų/išlaidų ataskaita, \n5 - Baigti\nPasirinkite: "))
        if pasirinkimas == 1:
            while True:
                try:
                    suma = float(input("Įveskite pajamų sumą: ").replace(',', '.'))
                    break
                except ValueError:
                    print("Įvestas ne skaičius!")
            siuntejas = input("Siuntėjas: ")
            papildoma_info = input("Papildoma informacija: ")
            biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)
        if pasirinkimas == 2:
            while True:
                try:
                    suma = float(input("Įveskite išlaidų sumą: ").replace(',', '.'))
                    break
                except ValueError:
                    print("Įvestas ne skaičius!")
            atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
            isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
            biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        if pasirinkimas == 3:
            print(f"Jūsų sąskaitoje: {biudzetas.gauti_balansą():.2f} eur")
        if pasirinkimas == 4:
            biudzetas.parodyti_ataskaita()
        if pasirinkimas == 5:
            print("Viso gero!")
            break
        if pasirinkimas not in range(6):
            print("Tokio pasirinkimo nėra!")


biudzetas = Biudzetas()
menu()