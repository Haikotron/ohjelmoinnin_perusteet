"""
##################################
# Task: T2 - Analyse separated values #
# Developer Antti Haiko #
# Date 13.11.2025 #
##################################
"""
def integers(valid_num: list[int], feed):   #Määritetään funktio, joka käsittelee pilkuilla erotettuja kokonaislukuja
    parts = feed.split(",")     #Pilkotaan syöte pilkkujen kohdalta listaksi

    for part in parts:      #Käydään läpi jokainen pilkulla erotettu osa
        part = part.strip()     #Poistetaan tyhjät välilyönnit alusta ja lopusta

        try:
            num = int(part)         #Yritetään muuntaa merkkijono kokonaisluvuksi
            valid_num.append(num)   #Jos onnistuu, lisätään listaan

        except ValueError:
            print(f"Error: '{part}' is not a valid integer.")

        except (KeyboardInterrupt, EOFError):
            print("User interrupted. Cancelling")
            break

    if not valid_num:       #Jos yhtään kelvollista lukua ei löytynyt
        print("No valid integers to analyze.")
        return      #Lopetetaan funktion suoritus
    

def display(valid_num: list[int]):
    Sum = sum(valid_num)        #Lasketaan kaikkien kelvollisten lukujen summa
    count = len(valid_num)      #Lasketaan kelvollisten lukujen määrä
    parity = "even" if Sum % 2 == 0 else "odd"      #Tarkistetaan, onko summa parillinen vai pariton?

    print(f"There are {count} integers in the list.")       #Tulostetaan lukujen määrä
    print(f"Sum of the integers is {Sum} and it's {parity}")        #Tulostetaan summa ja pariteetti


def main():
    print("Program starting.")
    
    valid_num: list[int] = []       #Tähän listaan säilötään kelvolliset kokonaisluvut.

    feed = input("Insert comma seperated integers: ")       #Pyydetään käyttäjältä syötettä

    integers(valid_num, feed)       #Kutsutaan kokonaislukujen käsittelyfunktiota ja tallennetaan palautettu lista

    if valid_num:               #Jos lista ei ole None, eli kokonaislukuja löytyy
        display(valid_num)      #Näytetään tulokset antamalla lista parametrina

    print("Program ending.")


if __name__ == "__main__":
    main()