#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    result = 0
    length = len(sys.argv)
    for i in range(1, length):
        result += int(sys.argv[i])
    print("{}".format(result))
