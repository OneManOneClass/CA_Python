# '''Parašyti klasę "Namas", kuri turėtų savybę "plotas" ir "verte". Padaryti taip, kad savybė "verte" koreguojama tik
# įvedus skaičių. Programoje naudoti dekoratorių @property. '''
#
#
class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, val):
        print(f"Priskiriama reikšmė: {val}")
        if type(val) != int or type(val) != float:
            print("Įvestas ne skaičius!")
        elif int(val) < 0:
                print("Vertė negali būti neigiama!")
        else:
            self.__verte = val

namas = Namas(200, 15000)
print(namas.verte)
namas.verte = -10
print(namas.verte)
namas.verte = "aaa"
print(namas.verte)
namas.verte = 15.16
print(namas.verte)






