






choice = ("y")

while choice == "y":

    try:
        number = int(input("pick a number: "))
    except ValueError:
        print ("Invalid number!") 
    choice = input("continue? (y/n)")
