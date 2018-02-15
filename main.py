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
    """
    Adds a lenist of numbers

    :param list_var: Is a list of numbers (int, float, complex)
    :returns: Addition of values in list
    :raises ValueError: If list_var is empty
    :raises ImportError: If numpy or numbers not installed in environment
    :raises TypeError: If element in list_var is not an int, float, or complex
    """
    try:
        import logging
    except ImportError:
        logging.warning('ImportError Logging')
        raise ImportError('Module Logging not found.')
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    try:
        import numpy as np
    except ImportError:
        logging.warning('ImportError Numpy')
        raise ImportError('Module Numpy not found.')
    if len(list_var) == 0:
        raise ValueError('Input list is empty')
    try:
        import numbers
    except ImportError:
        logging.warning('ImportError Numbers')
        raise ImportError('Module Numbers not found.')
    if not isinstance(list_var, list):
        logging.warning('Input is not a list')
    for x in list_var:
        if isinstance(x, (int, float, complex)):
            continue
        else:
            logging.warning('List elements must be int, float or complex')
            raise TypeError('List elements must be int, float, or complex')
    logging.debug(list_var)
    value = np.sum(list_var)
    logging.info(value)
    return value
