#Make a program, which prompts user to insert words.
# Program must stop prompting words if user inserts empty word.
# After stopping the repetitive prompt,
# print the amount of words and characters that the user inserted.

print ("Program starting.")
print ("")
WordCount = 0
CharCount = 0

Word = input("Insert word (empty stops): ")
while Word != '':
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")

print("\n You inserted:")
print (f"- {WordCount} words")
print (f"- {CharCount} characters")

print ("Program ending.")