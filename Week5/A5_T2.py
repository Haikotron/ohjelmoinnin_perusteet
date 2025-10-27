##################################
# Task A5_T2 #
# Developer Antti Haiko #
# Date 16-10-2025 #
##################################

def frameWord(Pword) -> None:
    print("*" * (len(Pword)+4))
    print(f"* {Pword} *")
    print("*" * (len(Pword)+4))
    return None


def main() -> None:
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("Program ending.")
    return None

main()