def hcf_sub(a, b):
    """Find HCF using subtraction-based Euclidean algorithm."""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def lcm(a, b):
    """Find LCM using HCF."""
    hcf = hcf_sub(a, b)
    return (a * b) // hcf

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = lcm(num1, num2)
    print(f"LCM({num1}, {num2}) = {result}")

if __name__ == "__main__":
    main()


'''
Enter the first number: 12
Enter the second number: 18
LCM(12, 18) = 36
'''