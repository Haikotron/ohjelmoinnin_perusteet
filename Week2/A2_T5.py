#A2_T5 String length and slicing (TEST TASK)

#Make a Python program, which prompts for a compound word.
#Get following aspects from the word
#        Length
#        First character
#        Reversed version e.g. “Suitcase” is reversed “esactiuS”
#    Display the aspects using print commands.
#    Prompt the user to take substring from the existing compound word.
#    Finally print the user specified substring.

print("Program starting.\n")
word = input("Insert a closed compound word: ")
print(f"The word you inserted is \'{word}\' and in reverse it is \'{word[::-1]}\'.")
print(f"The inserted word length is {len(word)})")
print(f"Last character is \'{word[-1]}\'")

print("\nTake substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

sub_word = word[start:end:step]
#sub stringin komento

print(f"\nThe word \'{word}\' sliced to the defined substring is \'{sub_word}\'.")
print("Program ending.")