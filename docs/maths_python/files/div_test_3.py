import random


def is_div_by_3(num):
    sum_of_digits = repeated_sum_digits(num)
    if sum_of_digits in [3, 6, 9]:
        return True
    else:
        return False


def sum_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum


def repeated_sum_digits(num):
    sum_of_digits = sum_digits(num)
    while sum_of_digits > 10:
        sum_of_digits = sum_digits(sum_of_digits)
    return sum_of_digits


for _ in range(10):
    num = random.randint(12, 300)
    print(num, num/3, is_div_by_3(num))
