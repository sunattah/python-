# STEP 1: Define calculation functions
def to_celsius(k):
    return round(k - 273.15, 2)

def to_fahrenheit(k):
    return round((k - 273.15) * 1.8 + 32, 2)

# STEP 2: Gather inputs from the user
try:
    kelvin_input = float(input("Enter temperature in Kelvin: "))
    
    # STEP 3: Handle physics boundary check
    if kelvin_input < 0:
        print("Error: Temperature cannot be below Absolute Zero (0 K).")
    else:
        unit_choice = input("Convert to (C)elsius, (F)ahrenheit, or (B)oth? ").upper()
        
        # STEP 4: Conditional routing logic
        if unit_choice == "C":
            print(f"{kelvin_input} K = {to_celsius(kelvin_input)}°C")
        elif unit_choice == "F":
            print(f"{kelvin_input} K = {to_fahrenheit(kelvin_input)}°F")
        elif unit_choice == "B":
            print(f"{kelvin_input} K = {to_celsius(kelvin_input)}°C")
            print(f"{kelvin_input} K = {to_fahrenheit(kelvin_input)}°F")
        else:
            print("Invalid choice selection.")

except ValueError:
    print("Error: Please enter a valid number for the temperature.")
