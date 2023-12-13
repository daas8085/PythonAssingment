#Program of Celsius to Fahrenheit Conversion Formula
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is equal to {fahrenheit_temperature} Fahrenheit.")
