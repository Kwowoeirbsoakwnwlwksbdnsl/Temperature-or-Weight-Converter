def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def kg_to_oz(kg):
    return kg * 35.274

def oz_to_kg(oz):
    return oz / 35.274

def kg_to_g(kg):
    return kg * 1000

def g_to_kg(g):
    return g / 1000

def lbs_to_oz(lbs):
    return lbs * 16

def oz_to_lbs(oz):
    return oz / 16

def lbs_to_g(lbs):
    return lbs * 453.592

def g_to_lbs(g):
    return g / 453.592

def oz_to_g(oz):
    return oz * 28.3495

def g_to_oz(g):
    return g / 28.3495

def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Choose an option (1-6): ").strip()
    if choice not in ['1','2','3','4','5','6']:
        print("Invalid choice.")
        return
    
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid number.")
        return
    
    if choice == '1':
        result = celsius_to_fahrenheit(value)
        print(f"{value} °C = {result:.2f} °F")
    elif choice == '2':
        result = fahrenheit_to_celsius(value)
        print(f"{value} °F = {result:.2f} °C")
    elif choice == '3':
        result = celsius_to_kelvin(value)
        print(f"{value} °C = {result:.2f} K")
    elif choice == '4':
        result = kelvin_to_celsius(value)
        print(f"{value} K = {result:.2f} °C")
    elif choice == '5':
        result = fahrenheit_to_kelvin(value)
        print(f"{value} °F = {result:.2f} K")
    elif choice == '6':
        result = kelvin_to_fahrenheit(value)
        print(f"{value} K = {result:.2f} °F")

def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Kilograms to Ounces")
    print("4. Ounces to Kilograms")
    print("5. Kilograms to Grams")
    print("6. Grams to Kilograms")
    print("7. Pounds to Ounces")
    print("8. Ounces to Pounds")
    print("9. Pounds to Grams")
    print("10. Grams to Pounds")
    print("11. Ounces to Grams")
    print("12. Grams to Ounces")
    
    choice = input("Choose an option (1-12): ").strip()
    if choice not in [str(i) for i in range(1,13)]:
        print("Invalid choice.")
        return
    
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid number.")
        return
    
    conversions = {
        '1': (kg_to_lbs, "kg", "lbs"),
        '2': (lbs_to_kg, "lbs", "kg"),
        '3': (kg_to_oz, "kg", "oz"),
        '4': (oz_to_kg, "oz", "kg"),
        '5': (kg_to_g, "kg", "g"),
        '6': (g_to_kg, "g", "kg"),
        '7': (lbs_to_oz, "lbs", "oz"),
        '8': (oz_to_lbs, "oz", "lbs"),
        '9': (lbs_to_g, "lbs", "g"),
        '10': (g_to_lbs, "g", "lbs"),
        '11': (oz_to_g, "oz", "g"),
        '12': (g_to_oz, "g", "oz")
    }
    
    func, from_unit, to_unit = conversions[choice]
    result = func(value)
    print(f"{value} {from_unit} = {result:.2f} {to_unit}")

def main():
    while True:
        print("\nMain Menu")
        print("1. Temperature Converter")
        print("2. Weight Converter")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            temperature_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()