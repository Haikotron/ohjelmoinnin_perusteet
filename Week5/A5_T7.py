"""
##################################
# Task A5_T7 Words in a string #
# Developer Antti Haiko #
# Date 27.10.2025 #
##################################
"""

DELIMITER = ','

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(word_string):
    word_list = word_string.split(DELIMITER)
    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)
    avg_length = char_count / word_count if word_count > 0 else 0

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))


def main():
    print ("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()