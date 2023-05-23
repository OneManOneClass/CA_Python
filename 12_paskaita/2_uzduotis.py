'''Perdaryti 1 užduoties programą, kad:
• Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
• Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu
Patarimas: panaudoti try/except/else, logging.exception()'''

import logging
from math import sqrt

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('12p2uzd.log', encoding='UTF-8')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
file_handler.setFormatter(log_formatter)


def square_root(x):
    try:
        result = sqrt(x)
        logger.info(f'SQRT({x}) = {result}')
        return result
    except TypeError:
        logger.exception(f'Funkcijai perduotas ne skaičius! ({x})')
    except ValueError:
        logger.exception(f'Funkcijai {square_root.__name__} perduotas neigiamas skaičius! ({x})')


def division(x, y):
    try:
        result = x / y
        logger.info(f'{x} / {y} = {result:.2f}')
        return result
    except ZeroDivisionError:
        logger.exception("Dalyba iš 0 negalima!")
    except TypeError:
        logger.exception("Funkcijai perduotas ne skaičius!")


print(square_root(-16))
print(square_root(16))
print(division(10, 2))
print(division(10, 0))
print(division(10, 'a'))