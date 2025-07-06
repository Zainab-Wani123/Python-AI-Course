#input from user
celcius = float(input("Enter temperature in Celsius: "))
#convert Celsius to Fahrenheit
fahrenheit = (celcius * 9/5) + 32
#convert Celsius to Kelvin
kelvin = celcius + 273.15
#print the results
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)