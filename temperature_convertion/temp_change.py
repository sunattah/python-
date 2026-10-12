print("Input an option")
print("1 : celcius")
print("2 : Fehrenhite")

choice = input("choose an option(1, 2)  : ")
if choice == "1":
    cencius = float(input("enter temperature in cencius :"))
    fehrenhite = (cencius*9/5)+ 32
    print(f"your temperature in cencius has been converted to {fehrenhite}")
elif choice == "2":
    fehrenhite = float(input("enter a temperature in fehrenhite :"))
    cencius = (fehrenhite - 32) * 5/9
    print(f"your temperature in fehrenhite has been converted to {cencius}")
else:
        print("invalid option")


    