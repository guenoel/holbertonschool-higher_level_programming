#!/usr/bin/python3
"""Module de traitement de phrases"""


def text_indentation(text):
    """fonction qui découpe les phrases d'un texte"""

    prev = " "
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        if letter not in [".", "?", ":"]:
            if letter in [" "] and prev in [".", "?", ":", " "]:
                pass
            else:
                print('{}'.format(letter), end='')
            prev = letter
        else:
            print('{}'.format(letter))
            print()
            prev = letter
