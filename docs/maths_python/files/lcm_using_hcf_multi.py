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

def lcm_list(numbers):
    """Find LCM of a list of numbers."""
    result = numbers[0]
    for n in numbers[1:]:
        result = lcm(result, n)
    return result

def main():
    # Prompt the user for a list of numbers separated by spaces
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    result = lcm_list(nums)
    print(f"LCM({nums}) = {result}")

if __name__ == "__main__":
    main()
