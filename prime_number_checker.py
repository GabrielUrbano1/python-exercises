def get_valid_integer():
    while True:
        num = int(input("Please enter an integer between 1 and 5000: "))
        if 1 <= num <= 5000:
            return num
        else:
            print("Invalid integer. Please try again.")

def calculate_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    print("Prime Number Checker")
    while True:
        num = get_valid_integer()
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            factors = calculate_factors(num)
            factor_count = len(factors)
            print(f"{num} is NOT a prime number.")
            print(f"It has {factor_count} factors: {factors}")
        choice = input("Try again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Bye!")
            break

main()
