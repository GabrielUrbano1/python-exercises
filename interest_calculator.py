import tkinter as tk
from decimal import Decimal, ROUND_HALF_UP

def calculate_monthly_payment(loan_amount, interest_rate, years):
    loan_amount = Decimal(str(loan_amount))
    interest_rate = Decimal(str(interest_rate))
    years = int(years)
    
    monthly_rate = interest_rate / Decimal('12') / Decimal('100')
    num_payments = years * 12
    
    if monthly_rate == 0:
        monthly_payment = loan_amount / Decimal(num_payments)
    else:
        monthly_payment = (loan_amount * (monthly_rate * ((1 + monthly_rate) ** num_payments))) / ((1 + monthly_rate) ** num_payments - 1)
    
    return monthly_payment

def generate_amortization_schedule(loan_amount, interest_rate, years, additional_payment=0):
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, years)
    monthly_rate = interest_rate / Decimal('12') / Decimal('100')
    num_payments = years * 12
    
    remaining_balance = loan_amount
    amortization_schedule = []
    
    total_interest_paid = Decimal('0.00')
    potential_home_value = Decimal(str(loan_amount))
    
    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        
        # Apply additional payment
        remaining_balance -= (principal_payment + additional_payment)
        
        # Track total interest paid and potential home value
        total_interest_paid += interest_payment
        if month % 12 == 0:
            # Increase potential home value by 8% annually (non-compounded)
            potential_home_value += (potential_home_value * Decimal('0.08'))
        
        amortization_schedule.append((month, monthly_payment, principal_payment, interest_payment, remaining_balance, total_interest_paid, potential_home_value))
        
        if remaining_balance <= 0:
            break
    
    return amortization_schedule

def create_home_value_trend(initial_home_value, sp500_returns):
    home_values = [initial_home_value]
    
    for annual_return in sp500_returns:
        previous_home_value = home_values[-1]
        
        # Calculate the new home value based on S&P 500 return
        new_home_value = previous_home_value * (1 + annual_return)
        
        home_values.append(new_home_value)
    
    return home_values



def calculate_amortization():
    try:
        # Validate input values
        loan_amount_str = loan_amount_entry.get()
        interest_rate_str = interest_rate_entry.get()
        years_str = years_entry.get()
        additional_payment_str = additional_payment_entry.get()
        
        if not (loan_amount_str and interest_rate_str and years_str):
            raise ValueError("Please fill in all fields.")
        
        loan_amount = Decimal(loan_amount_str)
        interest_rate = Decimal(interest_rate_str)
        years = int(years_str)
        additional_payment = Decimal(additional_payment_str)
        
        # Check for valid numeric values
        if (loan_amount <= 0) or (interest_rate <= 0) or (years <= 0):
            raise ValueError("Please enter positive values for loan amount, interest rate, and years.")
        
        amortization_schedule = generate_amortization_schedule(loan_amount, interest_rate, years, additional_payment)
        
        result_text.delete(1.0, tk.END)  # Clear previous results
        for row in amortization_schedule:
            result_text.insert(tk.END, f"{row}\n")
    except ValueError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(e))
# Create the main window
window = tk.Tk()
window.title("Amortization Schedule Calculator")

# Create input fields and labels
loan_amount_label = tk.Label(window, text="Loan Amount:")
loan_amount_entry = tk.Entry(window)
interest_rate_label = tk.Label(window, text="Interest Rate (%):")
interest_rate_entry = tk.Entry(window)
years_label = tk.Label(window, text="Number of Years:")
years_entry = tk.Entry(window)
additional_payment_label = tk.Label(window, text="Additional Monthly Payment:")
additional_payment_entry = tk.Entry(window)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate Amortization", command=calculate_amortization)

# Create a text widget for displaying the amortization schedule
result_text = tk.Text(window, height=20, width=50)

# Place widgets in the window using grid layout
loan_amount_label.grid(row=0, column=0, padx=10, pady=5)
loan_amount_entry.grid(row=0, column=1, padx=10, pady=5)
interest_rate_label.grid(row=1, column=0, padx=10, pady=5)
interest_rate_entry.grid(row=1, column=1, padx=10, pady=5)
years_label.grid(row=2, column=0, padx=10, pady=5)
years_entry.grid(row=2, column=1, padx=10, pady=5)
additional_payment_label.grid(row=3, column=0, padx=10, pady=5)
additional_payment_entry.grid(row=3, column=1, padx=10, pady=5)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()