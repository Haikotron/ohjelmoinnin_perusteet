#Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf
#Menu options:
#    Length
#        Meters to kilometers
#        Kilometers to meters
#    Weight
#        Grams to pounds
#        Pounds to grams
#    Exit
#        “Exiting...”
#Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.
#Other possible prints:
#    “Unknown option.”

#Program starting.
print("Program starting.")
#Welcome to the unit converter program!
print("Welcome to the unit converter program!")
#Follow the menu instructions below.
print("Follow the menu instructions below.")

#Options:
print("Options:")
#1 - Length
print("1 - Length")
#2 - Weight
print("2 - Weight")
#0 - Exit
print("0 - Exit")

#Your choice: 
Choice = int(input("Your choice: "))
#Length options:
if Choice == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))
    if Choice2 == 1:
        Meter = float(input("Insert meters: "))
        Km = Meter / 1000
        print(f"{round(Meter, 1)} m is {round(Km, 1)} km")
    elif Choice2 == 2:
        Km = float(input("Insert kilometers: "))
        Meter = Km * 1000
        print(f"{round(Km, 1)} km is {round(Meter, 1)} m")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))
    if Choice2 == 1:
        Gram = float(input("Insert grams: "))
        Pound = float(Gram * 0.002205)
        print(f"{round(Gram, 1)} g is {round(Pound, 1)} lb")
    elif Choice2 == 2:
        Pound = float(input("Insert pounds: "))
        Gram = float(Pound / 0.002205)
        print(f"{round(Pound, 1)} lb is {round(Gram, 1)} g")
    elif Choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif Choice == 0:
    print("Exiting...")

else:
    print("Unknown option.")

#Program ending.
print("\nProgram ending.")