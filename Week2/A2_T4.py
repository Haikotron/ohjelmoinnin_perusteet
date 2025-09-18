#Prompt the user to insert the minutes spent on each previous topic task.
# Calculate the sum and the average.
# Display those in the example program run format. (Note! precision).
# Make sure to calculate the required average for two decimal digits
# and later integer as rounded integer (precision 0 + type conversion).

#Program starting.
#Estimate how many minutes you spent on programming...

#A1_T1: 3
#A1_T2: 7
#A1_T3: 9
#A1_T4: 8
#A1_T5: 13
#A1_T6: 14
#A1_T7: 21

#In total you spent 75 minutes on programming.
#Average per task was 10.71 min and same rounded to the nearest integer 11 min.

#Program ending.

print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

    #kysytään käyttäjäktä minuutit jokaiselle tehtävälle
task1 = int(input("A1:_T1, How many minutes you spent on this task?"))
task2 = int(input("A1:_T2, How many minutes you spent on this task?"))
task3 = int(input("A1:_T3, How many minutes you spent on this task?"))
task4 = int(input("A1:_T4, How many minutes you spent on this task?"))
task5 = int(input("A1:_T5, How many minutes you spent on this task?"))
task6 = int(input("A1:_T6, How many minutes you spent on this task?"))
task7 = int(input("A1:_T7, How many minutes you spent on this task?"))
#kokonais määrä
total_task = (task1+task2+task3+task4+task5+task6+task7)
#keskiarvo
average = float(total_task / 7)

print(f"\nIn total you spent {total_task} min on programming.")
print(f"Average per task was {round (average, 2)} min and same rounder to nearest integer {round(average)} min.")
print("\n Program ending.")