#!/usr/bin/python3
"""Documenter le module"""


class MyList(list):

    def print_sorted(self):
        newlist = self.copy()
        print(sorted(newlist))
