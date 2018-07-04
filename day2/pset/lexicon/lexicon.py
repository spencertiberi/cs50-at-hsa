"""
Rap Lexicon
Spencer L Tiberi
CS50 at HSA, July 2018
"""
import os

def main():
    rappertexts = []

    # Directory where lyrics are stored
    directory = os.fsencode("lyrics/")

    # Fill list of rappers with txt filenames
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".txt"):
            rappertexts.append(filename)
            continue
        else:
            continue

    # Create a dict that has a rapper name and then set of words
    rappers = dict()

    # Fill dict with rapper names as keys and dicts of words as values then print name, wordcount, etc. to screen
    for rappertext in rappertexts:
        words = fill_words(rappertext)
        # Create rapper name from filefame (remove .txt and capitalize)
        rapper_name = rappertext[:-4].capitalize()

        # TODO: Add comment
        rappers[rapper_name] = words

        # Create a dotted line for formating based on length of the rapper's name
        line = "." * (40 - len(rapper_name))

        print("%s%s\n\tWord Count: %s\n\tLargest Word: %s\n\tMost Used Word: %s" % \
              (rapper_name, line, len(rappers[rapper_name]), \
              max(rappers[rapper_name], key=len), max(rappers[rapper_name], \
              key=rappers[rapper_name].get)))

    # TODO: Add comment
    while True:
        rapper = input("Choose a rapper to further examine (or type 'quit'): ")

        if rapper == 'quit':
            break
        elif rapper in rappers:
            examine_rapper(rappers[rapper])
        else:
            print("Invalid rapper!")

# Fills and returns a dict cotaining a set of words as keys and use count as valuesn for a given rapper file
def fill_words(rapper):
    # TODO

# Examines the number of times the rapper uses a user-inputted word and prints results to the screen
def examine_rapper(rapperWords):
    # TODO

if __name__ == '__main__':
    main()
