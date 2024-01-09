print("Table of Powers")


start_number = int(input("Pick a starting number"))
stop_number = int(input("Pick a stoping number"))
plus_one = stop_number + 1
user_range_number = range(start_number, plus_one)

if start_number > stop_number:
    print("invalid response, start number can not be greater then stop number!")
elif start_number < stop_number:
    print("Number \t Squared \t Cubed")
    for i in user_range_number:
        print(f"{i}\t {i*i}\t\t {i**3}")


