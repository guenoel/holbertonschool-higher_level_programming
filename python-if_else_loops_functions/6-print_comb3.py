#!/usr/bin/python3
for i in range(0, 90):
    if ((i//10 + (i % 10)*10) > i) and (i//10 != i % 10):
        if (i != 89):
            print("{0:02d}, ".format(i), end='')
        else:
            print("{0:02d}\n".format(i), end='')
