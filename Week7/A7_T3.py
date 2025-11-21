"""
##################################
# Task: T3 - Timestamp analysis #
# Developer Antti Haiko #
# Date 21.11.2025 #
##################################
"""
WEEKDAYS: tuple[str] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",        #HUOM SATURNDAY
    "Sunday",
    )

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PRows.clear()

    try:
        with open(PFilename, "r", encoding="utf-8") as file:
                next(file)
                for line in file:
                    if line.strip() == "":
                        continue
                    PRows.append(line.rstrip("\n"))
    except FileNotFoundError:
            print(f'File not found: {PFilename}')
    except Exception as e:
            print(f'Error reading file: {e}')
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    WeekdayTimestampAmount: list[int] = [0] * len(WEEKDAYS)

    for row in PRows:
        line = row.strip()
        if line == "":
             continue
        lowered = line.lower()
        for i, day in enumerate(WEEKDAYS):
             if lowered.startswith(day.lower()):
                WeekdayTimestampAmount[i] += 1
                break
             
    for day, count in zip(WEEKDAYS, WeekdayTimestampAmount):
         PResults.append(f"{day}: {count}")

    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    if not PResults:
         print("No results to display.")
         return None
    
    print("### Timestamp analysis ###")
    for line in PResults:
        print(line)
    print("### Timestamp analysis ###")
    
    return None

def main() -> None:
    Rows: list[str] = []
    Results: list[str] = []
    print("Program starting.")
    Filename = input("Insert filename: ")
    readFile(Filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)

    Rows.clear()
    Results.clear()
    del Rows, Results

    print("Program Ending.")

    return None

main()