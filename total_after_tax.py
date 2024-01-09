import sales_tax_calculator

def main():
    print("Sales Tax Calculator")
    
    total_cost = 0
    
    while True:
        cost = float(input("Cost of item (enter 0 to end): "))
        
        if cost == 0:
            break
        
        total_cost += cost
    
    sales_tax = sales_tax_calculator.calculate_sales_tax(total_cost)
    total_after_tax = sales_tax_calculator.calculate_total_after_tax(total_cost)
    
    print(f"Total:           {total_cost:.2f}")
    print(f"Sales tax:       {sales_tax:.2f}")
    print(f"Total after tax: {total_after_tax:.2f}")
    
    again = input("Again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks, bye!")


main()
