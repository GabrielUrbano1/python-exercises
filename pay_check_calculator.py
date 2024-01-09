print("Pay Check Calculator")
print()
hours_worked = float(input("Enter hours worked: \t"))
pay_rate = float(input("enter your pay rate: \t"))

gross_pay = hours_worked * pay_rate
print("Gross pay: \t\t" + str(gross_pay))
tax_rate = 0.18
print("Tax Rate: \t\t 18%")
tax_amount =  float(gross_pay * tax_rate)
print("Tax Amount: \t\t" + str(tax_amount))
take_home_pay = gross_pay - tax_amount
print("Take home amount: \t" + str(take_home_pay))