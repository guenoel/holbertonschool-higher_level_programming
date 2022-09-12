#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        if len(my_string) == 0:
            return(" ")
        my_string2 = ""
        for i in range(len(my_string)):
            if my_string[i] != 'c' and my_string[i] != 'C':
                my_string2 = my_string2 + my_string[i]
        return(my_string2)
