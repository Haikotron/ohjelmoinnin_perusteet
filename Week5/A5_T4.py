##################################
# Task A5_T4 #
# Developer Antti Haiko #
# Date 16-10-2025 #
##################################

def askDimension(PPrompt) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth, PHeight) -> float:
   Area = PWidth * PHeight
   return Area

def main():
   print("Program starting.")
   Width = askDimension("width")
   Height = askDimension("height")
   Area = calcRectangleArea(Width, Height)
   print("")
   print(f"Area is {Area}")
   print("Program ending.")

main()