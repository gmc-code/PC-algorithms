def hcf_sub(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = 48
b = 18

print(f'HCF({a}, {b}) is {hcf_sub(a, b)}.')
# HCF(48, 18) is 6.
