#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argz = sys.argv
    if len(argz) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argz)-1))
    for i in range (1, len(argz)):
        print("{}: {}".format(i, argz[i]))
