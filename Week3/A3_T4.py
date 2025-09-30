#Extend the previous menu program by adding three more options to the menu.

#Options:

#    Print the name backwards
#        Your name backwards is "{NameBackwards}"
#    Print the first character
#        The first character in name "{Name}" is "{FirstChar}"
#    Show the amount of characters in the name
#        There are {NameLength} characters in the name "{Name}"

#Program starting.
print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")

print("\n Options: ")
#1 - Print welcome message
print("1 - Print welcome message")
#2 - Print the name backwards
print("2 - Print the name backwards")
#3 - Print the first character
print("3 - Print the first character")
#4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
#0 - Exit
print("0 - Exit")

Choice = int(input("Your choice: "))
#Your choice: 

#Choices
if Choice == 1:
    print(f"Welcome {Name}!")
elif Choice == 2:
    print(f"Your name backwards is {Name[::-1]}")
elif Choice == 3:
    print(f"The first character in your name \"{Name}\" is \"{Name[0]}\"")
elif Choice == 4:
    print(f"There are {len((Name))} characters in the name \"{Name}\"")
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

#Program ending.
print("Program ending.")