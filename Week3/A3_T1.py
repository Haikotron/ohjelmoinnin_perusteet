#Make Python program and implement if-statements in proper places.

    #Ask user to insert two integers
    #Compare the integers and then announce the greater number
    #Create sum of the two integers
    #Check the parity of the sum (see modulo-operator ‘%’)

#Other possible output variants:

    #Integer comparison
        #Integers are the same.
        #First integer is greater.
    #Parity check
        #Sum is even.


print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

#Check which one is greater, or are they the same
if (int1 < int2):
    print("Second integer is greater.\n")
elif (int1 > int2):
    print("First integer is greater.\n")
else:
    print("Integers are the same.\n")

sum = int1 + int2
print("Adding integers together.")
print(f"{int1} + {int2} = {sum}\n")

remainder = sum % 2
#Check the parity of the sum
print("Checking the parity of the sum...")

if(remainder == 0):
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")