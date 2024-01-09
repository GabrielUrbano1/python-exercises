print("Price Comparison")


large_cup = float(input("Enter the 64 oz cup cost: \t"))
small_cup = float(input("Enter the 32 oz cup cost: \t"))
print("Price of 64 oz cup is: " + str(large_cup))
print("Price of 32 oz cup is: " + str(small_cup))

price_per_oz_64 = large_cup / 64
price_per_oz_32 = small_cup / 32

rounded_64_oz = round(price_per_oz_64, 2)
rounded_32_oz = round(price_per_oz_32, 2)
print("Price per oz (64 OZ): " + str(rounded_64_oz))
print("Price per oz (32 OZ): " + str(rounded_32_oz))