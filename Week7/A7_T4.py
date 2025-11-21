"""
##################################
# Task: T4 - T4 - Timestamp dataclass #
# Developer Antti Haiko #
# Date 21.11.2025 #
##################################
"""

from dataclasses import dataclass
from typing import List

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float  # kWh
    price: float        # €/kWh

def readTimestamps(filename: str,) -> List[TIMESTAMP]:
    timestamps: List[TIMESTAMP] = []

    try:
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

                hour = hour.strip()
                if ":" not in hour:
                    try:
                        hh = int(hour) % 24
                        hour = f"{hh:02d}:00"
                    except ValueError:
                        pass

                timestamps.append(TIMESTAMP(weekday, hour, cons, price))
    except FileNotFoundError:
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
    return timestamps

def displayTimestamps(timestamps: List[TIMESTAMP]) -> None:
    print("Electricity usages:")
    total_consumption = 0.0
    total_cost = 0.0
    for t in timestamps:
        total = t.consumption * t.price
        print(f" - {t.weekday} {t.hour}, price {t.price:.2f} €, consumption {t.consumption:.2f} kWh, total {total:.2f} €")
        total_consumption += t.consumption
        total_cost += total

def main() -> None:
    print("Program starting.")
    Filename = input("Insert filename: ")
    usages = readTimestamps(Filename)
    print(f"Reading file: \"{Filename}\"")
    if not usages:
        print("No usage records found.")
    else:
        displayTimestamps(usages)

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()