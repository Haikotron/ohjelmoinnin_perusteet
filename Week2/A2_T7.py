#A2_T7 Fahrenheit to Celcius

#Create a Python program to convert Fahrenheit to Celcius.
# Round the Celsius to 1 decimal precision.
#Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

#Example program run:

#Program starting.
#Insert fahrenheits: 50
#50.0°F is 10.0°C
#Program ending.

print("Program starting.")
fahr_temp = float(input("Insert fahrenheits: "))
celc_temp = (fahr_temp - 32) / 1.8
celc_temp = round(celc_temp, 1)
print(f"{fahr_temp}°F is {celc_temp}°C")
print("Program ending.")