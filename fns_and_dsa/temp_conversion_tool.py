CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

temperature = float(input("Enter a temperature: "))
unit = input("Is this temperature in Fahrenheit or Celsius? (F/C): ").strip().upper()

if unit == "F":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is equal to {celsius:.2f}°C")
elif unit == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")
else:
    print("invalid temperature. Please enter a numeric value.")