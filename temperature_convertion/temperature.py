import sys

def kelvin_to_celsius(k):
    """Converts Kelvin to Celsius."""
    return round(k - 273.15, 2)

def kelvin_to_fahrenheit(k):
    """Converts Kelvin to Fahrenheit."""
    return round((k - 273.15) * 1.8 + 32, 2)

def print_header():
    """Prints a clean CLI visual banner."""
    print("\n" + "="*45)
    print("      🌡️  KELVIN TEMPERATURE CONVERTER CLI 🌡️      ")
    print("="*45)

def main():
    while True:
        print_header()
        
        # 1. Get and validate the Kelvin temperature input
        raw_temp = input("Enter temperature in Kelvin (or type 'exit' to quit): ").strip()
        
        if raw_temp.lower() == 'exit':
            print("\nThank you for using the Temperature Converter! Goodbye. 👋")
            sys.exit()
            
        try:
            kelvin = float(raw_temp)
        except ValueError:
            print("\n❌ Error: Invalid input! Please enter a valid number.")
            input("\nPress Enter to try again...")
            continue

        # 2. Safety check for absolute zero boundary condition
        if kelvin < 0:
            print("\n❌ Error: Temperature cannot be below Absolute Zero (0 Kelvin).")
            input("\nPress Enter to try again...")
            continue

        # 3. Get and route the unit choice selection
        print("\nTarget conversion options:")
        print("  [C] Celsius")
        print("  [F] Fahrenheit")
        print("  [B] Both Scales")
        choice = input("Select a target unit (C/F/B): ").strip().upper()

        print("\n" + "-"*45)
        print("📊 RESULTS:")
        print("-"*45)
        
        # 4. Handle conditional logic routes
        if choice == "C":
            print(f"✨ {kelvin} K  ==>  {kelvin_to_celsius(kelvin)} °C")
        elif choice == "F":
            print(f"✨ {kelvin} K  ==>  {kelvin_to_fahrenheit(kelvin)} °F")
        elif choice == "B":
            print(f"✨ {kelvin} K  ==>  {kelvin_to_celsius(kelvin)} °C")
            print(f"✨ {kelvin} K  ==>  {kelvin_to_fahrenheit(kelvin)} °F")
        else:
            print("❌ Invalid menu choice selected. No conversion performed.")

        print("="*45)
        
        # 5. Let the user view results before restarting the main loop
        input("\nPress Enter to perform another calculation...")

if __name__ == "__main__":
    main()
