def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = kelvin * 9/5 - 459.67
    return fahrenheit

def main():
    print("Temperature Converter between Celsius, Fahrenheit, and Kelvin")
    print("-------------------------------------------------------------")
    
    # Input temperature value and unit
    temp = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original temperature unit (C, F, or K): ").upper()
    
    converted_temperatures = []
    
    # Convert the temperature based on the original unit
    if original_unit == 'C':
        celsius = temp
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        
    elif original_unit == 'F':
        fahrenheit = temp
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        
    elif original_unit == 'K':
        kelvin = temp
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    
    # Store the converted temperatures
    converted_temperatures.append(("Celsius", celsius))
    converted_temperatures.append(("Fahrenheit", fahrenheit))
    converted_temperatures.append(("Kelvin", kelvin))
    
    # Display the converted temperatures
    print(f"\nOriginal Temperature: {temp} {original_unit}")
    for unit, value in converted_temperatures:
        print(f"{unit}: {value:.2f}")

if __name__ == "__main__":
    main()
