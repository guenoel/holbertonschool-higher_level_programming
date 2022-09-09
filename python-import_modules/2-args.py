#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argz = sys.argv
    for i in range (1, len(argz)):
        print("{}: {}".format(i, argz[i]))
