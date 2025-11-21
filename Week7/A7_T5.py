from dataclasses import dataclass
from typing import List

WEEKDAYS: List[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",  # SATURNDAAYYYY
    "Sunday",
]

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float  # kWh
    price: float        # €/kWh

@dataclass
class DAY_USAGE:
    weekday: str
    usage: float
    cost: float

def readTimestamps(filename: str) -> List[TIMESTAMP]:
    timestamps: List[TIMESTAMP] = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                    continue
            parts = [p.strip() for p in line.split(";")]

            if parts and parts[0].lower() == "weekday":
                continue
            if len(parts) != 4:
                continue

            weekday, hour, cons_s, price_s = parts
            try:
                cons = float(cons_s)
                price = float(price_s)
            except ValueError:
                continue
            timestamps.append(TIMESTAMP(weekday, hour, cons, price))
    return timestamps

def analyse_daily(timestamps: List[TIMESTAMP]) -> List[DAY_USAGE]:
    day_usages = [DAY_USAGE(day, 0.0, 0.0) for day in WEEKDAYS]
    for t in timestamps:
        try:
            idx = WEEKDAYS.index(t.weekday)
        except ValueError:
            continue
        day_usages[idx].usage += t.consumption
        day_usages[idx].cost += t.consumption * t.price
    return day_usages

def display_summary(day_usages: List[DAY_USAGE]) -> None:
    print("Analysing timestamps.")
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for d in day_usages:
        print(f" - {d.weekday} usage {d.usage:.2f} kWh, cost {d.cost:.2f} €")
    print("### Electricity consumption summary ###")

def main() -> None:
    print("Program starting.")
    Filename = input("Insert filename: ")
    print(f'Reading file "{Filename}".')
    timestamps = readTimestamps(Filename)
    day_usages = analyse_daily(timestamps)
    display_summary(day_usages)
    print(f"Reading file: \"{Filename}\"")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()