import math


def get_prime_factors(num):
    max_possible = int(math.sqrt(num)) + 1
    prime_factors = list()
    while num % 2 == 0:
        prime_factors.append(2)
        num = num // 2
    for factor in range(3, max_possible, 2):
        while num % factor == 0:
            prime_factors.append(factor)
            num = num // factor
    if num > 2:
        prime_factors.append(num)
    return prime_factors


for num in range(2, 101):
    fact  = get_prime_factors(num)
    if len(set(fact)) > 2:
        print(num, fact)

