# Assignment 4: TeamOne
def max_diff(my_list):
    n = 0
    for i in range(len(my_list)-1):
        diff = abs(my_list[i+1] - my_list[i])
        if diff > n:
            n = diff
    return n


def maxMin(inputList):
    myMin = min(inputList)
    myMax = max(inputList)
    maxMinTuple = (myMin, myMax)
    print(maxMinTuple)
    return maxMinTuple


def add_list_numbers(list_var):
    try:
        import numpy as np
    except ImportError:
        raise ImportError('Module Numpy not found.')
    try:
        import numbers
    except ImportError:
        raise ImportError('Module Numbers not found.')
    for x in list_var:
        if isinstance(x, (int, float, complex)):
            continue
        else:
            raise TypeError('List must be made out of numbers only')
    return np.sum(list_var)
