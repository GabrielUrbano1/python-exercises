print("Even of Odd checker")

def odd_or_even(number):
    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

def main():
    user_input = int(input("Enter an interger"))
    result = odd_or_even(user_input)
main()
