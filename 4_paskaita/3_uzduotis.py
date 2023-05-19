'''
1. Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
2. Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą
lytį, gimimo datą ir eilės numerį).
'''


from datetime import datetime
# 3.1-----------------------------------------------
def id_check(num):
    number = [int(i) for i in str(num)]
    if len(number) != 11:
        return False
    elif number[0] < 1 or number[0] > 6:
        return False
    elif checksum_check(number) != number[10]:
        return False
    elif number[3] * 10 + number[4] > 12 or number[5] * 10 + number[6] > 31:
        return False
    else:
        return True


def checksum_check(num):
    checksum = num[0] + num[1] * 2 + num[2] * 3 + num[3] * 4 + num[4] * 5 + num[5] * 6 + num[6] * 7 + num[7] * 8 + num[
        8] * 9 + num[9]
    if checksum % 11 != 10:
        return checksum % 11
    else:
        checksum = num[0] * 3 + num[1] * 4 + num[2] * 5 + num[3] * 6 + num[4] * 7 + num[5] * 8 + num[6] * 9 + num[7] + \
                   num[8] * 2 + num[9] * 3
        if checksum % 11 != 10:
            return checksum % 11
        else:
            return 0


print(id_check(46411231034))

# # 3.2-----------------------------------------------
# # REQUIRES checksum_check() FROM 3.1

def id_generator(sex, birth_date, serial_num):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    id_num = ""

    if sex == "V":
        if birth_date.year >= 1801 and birth_date.year < 1901:
            id_num += "1"
        elif birth_date.year >= 1901 and birth_date.year < 2001:
            id_num += "3"
        else:
            id_num += "5"
    if sex == "M":
        if birth_date.year >= 1801 and birth_date.year < 1901:
            id_num += "2"
        elif birth_date.year >= 1901 and birth_date.year < 2001:
            id_num += "4"
        else:
            id_num += "6"
    id_num += (str(birth_date.year)[2::])
    if birth_date.month < 10:
        id_num += "0" + str(birth_date.month)
    else:
        id_num += str(birth_date.month)
    if birth_date.day < 10:
        id_num += "0" + str(birth_date.day)
    else:
        id_num += str(birth_date.day)
    id_num += str(serial_num)
    checksum_list = [int(i) for i in id_num]
    checksum = checksum_check(checksum_list)
    id_num += str(checksum)

    print(str(id_num))


id_generator("M", "1993-08-02", 546)