#Create a temperature unit conversion program.

#Start the program by listing options for the user:

#    Celsius to Fahrenheit
#    Fahrenheit to Celsius
#    Exit

#Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

#For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

#Data representation examples:

#    50.0 °F
#    10.0 °C

#If the user chooses option Exit, notify the user: Exiting...

#Use 1 decimal precision to round the converted value.

#Program starting.
print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
Choice = int(input("Your choice: "))
#Choice1
if Choice == 1:
    Cel = float(input("Insert the amount of Celsius: "))
    Fah = (Cel * 1.8) + 32
    Cel = round(Cel, 1)
    Fah = round(Fah, 1)
    print(f"{Cel} °C equals to {Fah} °F")

#Choice2
elif Choice == 2:
    Fah = float(input("Insert the amount of Fahrenheit: "))
    Cel = (Fah - 32) / 1.8
    Cel = round(Cel, 1)
    Fah = round(Fah, 1)
    print(f"{Fah} °F equals to {Cel} °C")

#Choice3
elif Choice == 0:
    print("Exiting...")

#Program ending.
print("Program ending.")