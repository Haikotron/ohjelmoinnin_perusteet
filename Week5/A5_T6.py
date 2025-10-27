"""
##################################
# Task A5_T6 Tally counter #
# Developer Antti Haiko #
# Date 27.10.2025 #
##################################
"""

def optionMenu():
    print ("Options:")
    print ("1 - Show count")
    print ("2 - Increase count")
    print ("3 - Reset count")
    print ("0 - Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!\n")
        return -1 # Palauttaa invalid valinnan mainiin

def main():
    print ("Program starting.")
    count = 0
    while True:
        optionMenu()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!\n")
        elif choice == 3:
            count = 0
            print("Cleared count!\n")
        elif choice == 0:
            print("Exiting program.\n")
            print("Program ending.")
            break
        elif choice == -1:
            continue
        else:
            print("Unknown option!")


if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()