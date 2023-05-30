'''Parašykite generatoriaus funkciją, kuri atidarytų nurodytą failą, ir grąžintų po vieną eilutę
(tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.). Reikės prisiminti darbą su failais :)'''


def line_reader(file):
    for ln in open(file, 'r', encoding='utf-8'):
        yield ln


# read_file = '4uzd.txt'
read_file = 'war_and_peace.txt'

line = line_reader(read_file)
line_count = 0

while True:
    try:
        line_count += 1
        print(line_count, next(line))
    except StopIteration:
        print("\n\n***** End of file *****")
        break

