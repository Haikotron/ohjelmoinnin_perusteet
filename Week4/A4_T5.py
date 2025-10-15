#Make a program, which prompts user to insert three integers:

    # 1.Starting point
    # 2.Stopping point
    # 3.Inspection point

#Test the points with following rules(Note! testing order matters):

    # 1. Starting point must be less than stopping point
        #"Starting point value must be less than the stopping point value."
    # 2. The inspection point must be within the range of the start and stop points.
        #"Inspection value must be within the range of start and stop."

#If any rule above is broken, print the violation message(s)
# to the user and then skip the next part till the "Program ending." print.

#Run two for-loops like shown in the example program runs
# if none of the rules above are broken.
# Inside the loops, compare the inspection point to the current iteration.
# Use break and continue commands if the current iteration is same as the inspection point.
# Otherwise print the current iteration on the same line.

#Note! There must be no trailing space character at the end of any row.

print ("Program starting.")
print ("")

Feed = input("Insert starting point: ")
PointStart = int(Feed)
Feed = input("Insert stopping point: ")
PointStop = int(Feed)
Feed = input("Insert inspection point: ")
PointInsp = int(Feed)
print("")

Run = True

if(PointStart >= PointStop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if(PointStart > PointInsp) or (PointInsp > PointStop):
    print("Inspection value must be within the range of start and stop.")
    Run = False

if(Run):
    print("First loop - inspection with break:")
    for i in range(PointStart, PointStop):
        if(i == PointInsp):
            break
        else:
            print(i, end=' ')

    print("")
    print("Second loop - inspection with continue:")
    for i in range(PointStart, PointStop):
        if (i == PointInsp):
            continue
        else:
            if(i == PointStop):
                print(i)
            else:
                print (i, end=' ')

print("")
print ("Program ending.")