#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    valeurs = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
            }
    roman_string = str(roman_string)
    if set(valeurs) & set(roman_string):
        tmp = valeurs[roman_string[-1]]
        for letter in reversed(roman_string):
            for k in valeurs:
                if letter == k:
                    if valeurs[letter] < tmp:
                        result -= valeurs[letter]
                    else:
                        result += valeurs[letter]
            tmp = valeurs[letter]
    return result
