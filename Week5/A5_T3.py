##################################
# Task A5_T3 #
# Developer Antti Haiko #
# Date 16-10-2025 #
##################################

def askName():
    name = input("Insert name: ")
    return name

def greetUser(PName):
    print (f"Hello {PName}")
    return None



def main() -> None:
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

main()