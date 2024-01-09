#!/usr/bin/python3
def no_c(my_string):
    new_String = ""
    for letter in my_string:
        if (letter != 'c' and letter != 'C'):
            new_String += letter
    return (new_String)
