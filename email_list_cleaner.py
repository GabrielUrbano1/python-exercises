# import csv

# def clean_prospects(input_fi lename, output_filename):
#     cleaned_prospects = []

#     with open(input_filename, 'r', newline='') as input_file:
#         reader = csv.reader(input_file)
#         next(reader)  # Skip the header row

#         for row in reader:
#             if len(row) >= 2:  # Ensure there are at least two columns
#                 name = row[0].strip().title()  # Clean and format the name
#                 email = row[1].strip().lower()  # Clean and format the email

#                 cleaned_prospects.append([name, email])

#     with open(output_filename, 'w', newline='') as output_file:
#         writer = csv.writer(output_file)
#         writer.writerow(['Name', 'Email'])  # Write header row

#         for prospect in cleaned_prospects:
#             writer.writerow(prospect)

# def main():
#     input_filename = 'prospects.csv'
#     output_filename = 'prospects_clean.csv'

#     try:
#         clean_prospects(input_filename, output_filename)
#         print(f"Cleaned prospects saved to {output_filename}")
#     except FileNotFoundError:
#         print(f"File {input_filename} not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     main()


n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)