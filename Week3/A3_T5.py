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

#Choice unknown
else:
    print("Unknown option.")

#Program ending.
print("\nProgram ending.")