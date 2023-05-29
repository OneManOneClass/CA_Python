'''Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti.
Galite patobulinti, pvz funkcijos (vardas), su tokiais ir tokiais argumentais vykdymo laikas - XX s.
Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija, išrenkančia pirminius skaičius užduotame diapazone.'''

from time import time  # importuojame time modulį
from math import sqrt
import requests  # importuojame requests


def fn_timer(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        runtime = end_time - start_time
        print(f'Funkcijos {fn.__name__} vykdymo laikas su argumentais args = {args},kwargs = {kwargs}: {runtime:.4f}s')
        return result

    return wrapper


@fn_timer
def get_status_code(web_url):
    return requests.get(web_url)


@fn_timer
def primary_nums(r1, r2):
    primary_list = []
    for num in range(r1, r2 + 1):
        if num > 1:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                primary_list.append(num)
    return primary_list


test_url = 'https://github.com'

print(get_status_code(test_url))
print(primary_nums(-500, 500))
