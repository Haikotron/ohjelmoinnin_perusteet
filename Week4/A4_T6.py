print("Program starting.")
Num = int(input("Insert a positive integer: "))
Count = 0 #kierroslaskuri

while Num != 1:
    print(f"{Num} -> ", end="")
    if Num % 2 == 0:
        Num = Num // 2
    else:
        Num = Num * 3 + 1
    Count += 1
print("1")
print(f"Sequence had {Count} total steps.")
print("\nProgram ending.")