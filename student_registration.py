first_name = input("Input your First name: \t")
last_name = input("Input your Last name: \t")
birth_year = int(input("Input your birth year: \t"))

print("Welcome " + first_name + " " + last_name + "!")
print("Your registration is complete.")
print("Your temporary password is:  " + first_name + "*" + str(birth_year))