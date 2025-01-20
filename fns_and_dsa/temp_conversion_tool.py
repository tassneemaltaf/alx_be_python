FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

def convert_to_fahrenheit(celsius):
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) - 32
    return temperature

def main():
    temp = int(input("Enter the temperature to convert: "))
    conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if conversion == 'F':
        fahrenheit_temp = convert_to_celsius(temp)
        print(temp,".0ºF is ",fahrenheit_temp,"°C")
    elif conversion == 'C':
        celsius_temp = convert_to_fahrenheit(temp)
        print(temp, ".0ºF is ", celsius_temp, "ºC")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
