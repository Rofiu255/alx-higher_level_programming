#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        list_copy = my_list.copy()
        list_copy.sort()
        return list_copy[-1]
