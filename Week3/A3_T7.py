#In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. Structure, order and operators matter, so do exactly as the task describes.

    #Prompt user to insert value as an integer.
    #Display menu
    #    option 1 - In one multi-branched decision
    #    option 2 - Independent if-statement decisions
    #    option 0 - Exit
    #Prompt user to choose option
    #Apply following math operations in the options 1 & 2
    #    One multi-branched decision structure:
    #        Value is 400 or more => add 44 to the existing value
    #        Value is 200 or more => add 22 to the existing value
    #        Value is 100 or more => add 11 to the existing value
    #    Independent if-statement decisions one after another:
    #        Value is 400 or more => add 44 to the existing value
    #        Value is 200 or more => add 22 to the existing value
    #        Value is 100 or more => add 11 to the existing value
    #    Exit: “Exiting…”
    #At the end of the options 1 & 2, show the results like in the example program runs.

#Other possible output variats:

#   “Unknown option.”

print("Program starting.")
print("Testing decision structures.")

Feed = int(input("Insert an integer: "))

print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

Choice = int(input("Your choice: "))

if(Choice == 1):
    print("Using one multi-branched decision structure")
    if(Feed >= 400):
        Feed += 44
    elif(Feed >= 200):
        Feed += 22
    elif(Feed >= 100):
        Feed += 11
    print(f"Result is {Feed}")
elif(Choice == 2):
    print("Using Independent if-statement decisions one after another")
    if(Feed >= 400):
        Feed += 44
    if(Feed >= 200):
        Feed += 22
    if(Feed >= 100):
        Feed += 11
    print(f"Result is {Feed}")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option")

print("\nProgram ending.")