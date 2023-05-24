'''Perdaryti 2 užduoties programą, kad:
• Būtų sukurtas savo logeris, kuris fikstuotus visus anksčiau aprašytus pranešimus
• Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje'''

import logging
from math import sqrt


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('12p3uzd.log', encoding='UTF-8')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

log_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
file_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

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


square_root(-16)
square_root(16)
division(10, 2)
division(10, 0)
division(10, 'a')