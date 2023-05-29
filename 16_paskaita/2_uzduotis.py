'''Parašykite dekoratorių, kuris atideda funkcijos vykdymą 3s'''

from time import sleep


# def uzvelavimas(laikas):
def uzvelavimas(fn):
    def wrapper(*args):
        # sleep(laikas)
        sleep(3)
        # print(f"Funkcija buvo atidėta {laikas} sekundę(-es)")
        print(f"Funkcija buvo atidėta 3s.")
        return fn(*args)
    return wrapper
    # return uzvelavimas


# @uzvelavimas(3)
@uzvelavimas
def sumavimas(*args):
    print("Skaičių suma:", sum(args))


sumavimas(50, 30)
sumavimas(50, 30, 20, 15)
