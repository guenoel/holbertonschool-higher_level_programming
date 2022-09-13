#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [1 if my_list[p] % 2 == 0 else 0 for p in range(len(my_list))]
