#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1

    if num_arg == 0:
        print("{} arguments.".format(num_arg))
    elif num_arg == 1:
        print("{} argument:".format(num_arg))
    else:
        print("{} arguments:".format(num_arg))

    if num_arg >= 1:
        num_arg = 0
        for arg in sys.argv:
            if num_arg != 0:
                print("{}: {}".format(num_arg, arg))
            num_arg += 1
