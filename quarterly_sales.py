# Initialize an empty list to store quarterly sales
quarterly_sales = []

# Get quarterly sales from the user
for quarter in range(1, 5):
    while True:
        sales = float(input(f"Enter sales for Q{quarter}: "))
        quarterly_sales.append(sales)
        break

# Calculate total, average, lowest, and highest quarterly sales
total_sales = round(sum(quarterly_sales), 2)
average_sales = round(total_sales / 4, 2)
lowest_sales = round(min(quarterly_sales), 2)
highest_sales = round(max(quarterly_sales), 2)

# Display the results
print("Total: ", total_sales)
print("Average Quarter: ", average_sales)
print("Lowest Quarter: ", lowest_sales)
print("Highest Quarter: ", highest_sales)
