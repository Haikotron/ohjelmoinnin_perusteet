# Make Python program, which prompts user to insert two words.
# Print the length of each word and then compound them together.
# Put single quotes around the compound word.

#Example program run:
#Program starting.
#Insert first word: fire
#Insert second word: fighter
#1st word is 4 characters long.
#2nd word is 7 characters long.
#Words together makes one closed compound 'firefighter'.
#Program ending.

print ("Program starting")
word1 = input("Insert first word: ")
word2 = input("Insert second word: ")

print(f"1st word is {len(word1)} characters long.")
print(f"2nd word is {len(word2)} characters long.")

compound_word = word1 + word2
print(f"Words together make one closed compound '{compound_word}'.")
print("Program ending.")
