'''Sukurti minibiudžeto programą, kuri:
• Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
• Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
• Atvaizduotų jau įvestas pajamas ir išlaidas
• Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

Patarimas:
• import pickle
'''

import pickle

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
                balansas += irasas.suma
        return (balansas)

    def parodyti_ataskaita(self):
        if not self.zurnalas:
            print("Įrašų nerasta")
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} Siuntejas: {irasas.siuntejas} - {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(
                    f"Išlaidos: {irasas.suma} Atsiskaitymo budas: {irasas.atsiskaitymo_budas} - {irasas.isigyta_preke_paslauga}")


def main():
    while True:
        pasirinkimas = int(input(
            "1 - Įvesti pajamas/išlaidas, \n2 - Parodyti balansą, \n3 - Pajamų/išlaidų ataskaita, \n4 - Baigti\nPasirinkite: "))
        if pasirinkimas == 1:
            while True:
                try:
                    suma = float(input("Įveskite sumą: ").replace(',', '.'))
                    if suma == 0:
                        print("Pajamos/išlaidos negali būti = 0!")
                    else:
                        break
                except ValueError:
                    print("Įvestas ne skaičius!")
            if suma > 0:
                siuntejas = input("Siuntėjas: ")
                papildoma_info = input("Papildoma informacija: ")
                biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)

            else:
                atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
                isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
                biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)

        if pasirinkimas == 2:
            print(f"Jūsų sąskaitoje: {biudzetas.gauti_balansą():.2f} eur")
        if pasirinkimas == 3:
            biudzetas.parodyti_ataskaita()
        if pasirinkimas == 4:
            with open("biudzetas.pkl", 'wb') as budget_file:
                pickle.dump(biudzetas, budget_file)
            print("Viso gero!")
            break
        if pasirinkimas not in range(5):
            print("Tokio pasirinkimo nėra!")


if __name__ == '__main__':
    biudzetas = Biudzetas()
    try:
        with open("biudzetas.pkl", 'rb') as budget_file:
            biudzetas = pickle.load(budget_file)
    except FileNotFoundError:
        with open("biudzetas.pkl", 'wb') as budget_file:
            pickle.dump(biudzetas, budget_file)
    except EOFError:
        pass
    main()