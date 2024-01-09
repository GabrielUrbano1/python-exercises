print("Tip Calculator")

cost_of_meal = float(input("Enter meal cost: "))
tip_percent = float(input("Enter tip percent: "))

tip_amount = cost_of_meal * (tip_percent/100)
total_amount = tip_amount + cost_of_meal

rounded_tip_amount = round(tip_amount, 3)
rounded_total_amount = round(total_amount, 3)

print("Tip Amount: \t\t" + str(rounded_tip_amount))
print("Your total is: \t\t" + str(rounded_total_amount))
