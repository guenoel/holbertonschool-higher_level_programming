#!/usr/bin/python3
"""Documenter le module"""


class MyList(list):
    """Classe qui affiche les tableau rangés"""

    def print_sorted(self):
        newlist = self.copy()
        print(sorted(newlist))
