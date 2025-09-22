#Write a Python program which asks user to insert hex color.
#In this case hex color is expected to be the 7 character representation
# starting with # and followed by 6 0-F characters to represent RGB colors.
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors

#Slice the amount of red, green and blue
#from that inserted color and display each color as shown below.

print("Program starting. \n")
hex = input("Insert a hex color: ")
#kysytään käyttäjältä hex-koodi väri
print("\n Colors")
print(f"- Red {hex[1:3]}")
#ensimmäinen merkki pois, 2 ja 3 merkki printtaantuu
print(f"- Green {hex[3:5]}")
#ensimmäiset 3 merkkiä pois, 4 ja 5 merkki printtaantuu
print(f"- Blue {hex[5:7]}\n")
#ensimmäiset 5 merkkiä pois, 6 ja 7 merkki printtaantuu
print("Program ending.")


