'''Sukurti funkcijas, kurios:
• Gražintų visų paduotų skaičių sumą (su *args argumentu)
• Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
• Gražintų paduoto sakinio simbolių kiekį (su len())
• Gražintų rezultatą, skaičių x padalinus iš y
Nustatyti standartinį logerį (logging) taip, kad jis:
• Saugotų pranešimus į norimą failą
• Saugotų INFO lygio žinutes
• Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė'''

import logging
from math import sqrt

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('12p1uzd.log', encoding='UTF-8')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
file_handler.setFormatter(log_formatter)


def sum_nums(*args):
    try:
        result = sum(float(i) for i in args)
        logger.info(f'Suma {result:.2f}')
        return result
    except ValueError:
        logger.info(f'Funkcijai {sum_nums.__name__} perduotas ne skaičius!')


def square_root(x):
    try:
        result = sqrt(x)
        logger.info(f'SQRT({x}) = {result}')
        return result
    except TypeError:
        logger.info(f'Funkcijai perduotas ne skaičius! ({x})')
    except ValueError:
        logger.info(f'Funkcijai {square_root.__name__} perduotas neigiamas skaičius! ({x})')


def s_count(s):
    try:
        result = len(s)
        logger.info(f'Duotame sakinyje {s} rasta(i) {result} simbolių(ai)')
        return result
    except TypeError:
        logger.info(f'Funkcijai {s_count.__name__} perduotas ne tekstas! ({s})')


def division(x, y):
    try:
        result = x / y
        logger.info(f'{x} / {y} = {result:.2f}')
        return result
    except ZeroDivisionError:
        logger.info("Dalyba iš 0 negalima!")
    except TypeError:
        logger.info("Funkcijai perduotas ne skaičius!")


sum_nums(1, 2, 3, 4, 5, 2.2157)
sum_nums("abc")
square_root(-16)
square_root(16)
s_count("Random test text")
s_count(123)
division(10, 2)
division(10, 0)
division(10, 'a')
