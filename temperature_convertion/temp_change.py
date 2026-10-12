print("Input an option")
print("1 : celcius")
print("2 : Fehrenhite")

choice = input("choose an option(1, 2)")
if choice == "1":
    cencius = float(input("enter temperature in cencius :"))
    fehrenhite = (cencius*9/5)+ 32
    print(f"your temperature in cencius has been converted to {fehrenhite}")


    