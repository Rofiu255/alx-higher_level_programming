#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dickey = list(a_dictionary.keys())
    list_dickey.sort()
    for i in list_dickey:
        print("{}: {}".format(i, a_dictionary.get(i)))
