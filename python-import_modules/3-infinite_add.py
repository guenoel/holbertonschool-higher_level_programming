#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    somme = 0
    argz = sys.argv
    if len(argz) == 1:
        print("0")
    elif len(argz) == 2:
        print(argz[1])
    else:
        for i in range(1, len(argz)):
            somme += int(argz[i])
        print(somme)
