#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for rowmatrix in matrix:
        if len(rowmatrix) == 0:
            print()
        for i in range(len(rowmatrix)):
            print("{:d}".format(rowmatrix[i]),
                  end="\n" if i is len(rowmatrix) - 1 else " ")
