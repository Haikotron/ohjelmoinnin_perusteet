"""
##################################
# Task: T1 - Positive Integer Collector #
# Developer Antti Haiko #
# Date 13.11.2025 #
##################################
"""
def IntCollector():                     #Kerää positiivisia kokonaislukuja käyttäjältä listaan
    numbers: list[int] = []             #Lista kerättäville positiivisille kokonaisluvuille
    while True:                         #Pääsilmukka: Jatkuu kunnes negatiivinen luku, tai virhe
        try:
            feed = int(input("Insert positive integer (Negative stops): "))     #Pyydetään käyttäjältä kokonaisluku

        except ValueError:              #Jos käyttäjä antaa ei kokonaisluvun, esim kirjaimen tai desimaalin
            print("Invalid input. Please enter an integer.")
            break                       # Lopetetaan kerääminen

        except (KeyboardInterrupt, EOFError):       # Jos käyttäjä keskeyttää (Ctrl+C, tai Ctrl+D)
            print("User interrupted. Cancelling.")
            break                       #Lopetetaan kerääminen

        if feed < 0:                    #Jos negatiivinen luku syötetty
            break                       #Lopetetaan kerääinen

        elif feed > 0:                  #Jos positiivinen luku syötetty
            numbers.append(feed)        #Lisätään luku listaan.

    print("Stopped collecting positive integers.")

    if numbers:                         #Jos listassa on lukuja
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers):     #Käydään läpi jokainen luku indeksin kanssa
            ordinal = index + 1                     #Ordinal on ihmisluettava numero (Alkaa 1:stä)
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")

    else:       #Jos lista on tyhjä
        print("No integers to display.")



def main() -> None:         #Pääohjelma, koordinoi ohjelman kulun
    print("Program starting.")
    print("Collect positive integers.")

    IntCollector()          #Kutsutaan lukujen keruu funktiota!

    print("Program ending.")


if __name__ == "__main__":
    main()      # Käynnistetään ohjelma