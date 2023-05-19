'''
1. Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma skaitmenų pusė yra lygi antrąjai, priešingu
atveju grąžintų False.
2. Parašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
      Input: 5678
      Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79
'''


# 2.1-----------------------------------------------
def equal_halfs(num):
    digit_count = (len(str(num)))
    num_list = [int(i) for i in str(num)]
    sum1 = 0
    sum2 = 0
    if digit_count % 2 == 0:
        half = int(digit_count / 2)
        for i in range(half):
            sum1 += num_list[i]
        for i in range(half, len(num_list)):
            sum2 += num_list[i]
    else:
        half = int(digit_count / 2) + 1
        for i in range(half):
            sum1 += num_list[i]
        for i in range(half - 1, len(num_list)):
            sum2 += num_list[i]
    if sum1 == sum2:
        return True
    else:
        return False


print(equal_halfs(1221))
print(equal_halfs(51215))
print(equal_halfs(1234))
print(equal_halfs(565656))


# 2.2-----------------------------------------------
def num_neighbours(num):
    num_list = [int(i) for i in str(num)]
    for i in range((len(num_list))):
        print(f"{num_list[i]} - {num_list[i] - 1}{num_list[i] + 1}")


num_neighbours(5678)
