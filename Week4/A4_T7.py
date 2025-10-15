print ("Program starting.\n")
print ("Check multiplicative persistence.")
Num = int(input("Insert an integer: "))
Steps = 0

while Num >= 10:
    Digits = [int(d) for d in str(Num)]
    print(" * ".join(str(d) for d in Digits), end=" = ")
    Result = 1
    for d in Digits:
        Result *= d
    print(Result)
    Num = Result
    Steps += 1

print("No more steps.\n")
print(f"This program took {Steps} step(s)\n")
print("Program ending.")