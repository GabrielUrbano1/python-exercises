# sales_tax_calculator.py

SALES_TAX_RATE = 0.06  # 6% sales tax rate

def calculate_sales_tax(cost):
    # Calculate sales tax rounded to 2 decimal places
    return round(cost * SALES_TAX_RATE, 2)

def calculate_total_after_tax(cost):
    # Calculate total cost after tax rounded to 2 decimal places
    return round(cost + calculate_sales_tax(cost), 2)
