print("Tip Calculator")

cost_of_meal = float(input("Enter meal cost: "))
tip_15 = 0.15
tip_20 = 0.20
tip_25 = 0.25

tip_amount = cost_of_meal * tip_15
total_amount = tip_amount + cost_of_meal
rounded_tip_amount = round(tip_amount, 2)
rounded_total_amount = round(total_amount, 2)
print(f"15%\nTip amount:\t {rounded_tip_amount}\nTotal Amount:\t {rounded_total_amount} ")

tip_amount = cost_of_meal * tip_20
total_amount = tip_amount + cost_of_meal
rounded_tip_amount = round(tip_amount, 2)
rounded_total_amount = round(total_amount, 2)
print(f"20%\nTip amount:\t {rounded_tip_amount}\nTotal Amount:\t {rounded_total_amount} ")

tip_amount = cost_of_meal * tip_25
total_amount = tip_amount + cost_of_meal
rounded_tip_amount = round(tip_amount, 2)
rounded_total_amount = round(total_amount, 2)
print(f"25%\nTip amount:\t {rounded_tip_amount}\nTotal Amount:\t {rounded_total_amount} ")

