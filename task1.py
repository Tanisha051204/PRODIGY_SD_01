def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
print("Temperature Conversion Program")
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == 'C':
    fahrenheit = celsius_to_fahrenheit(temp)
    kelvin = celsius_to_kelvin(temp)
    print(f"{temp} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
elif unit == 'F':
    celsius = fahrenheit_to_celsius(temp)
    kelvin = fahrenheit_to_kelvin(temp)
    print(f"{temp} degrees Fahrenheit is {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
elif unit == 'K':
    celsius = kelvin_to_celsius(temp)
    fahrenheit = kelvin_to_fahrenheit(temp)
    print(f"{temp} Kelvin is {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")
else:
    print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")