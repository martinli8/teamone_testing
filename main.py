# Assignment 4: TeamOne
import logging


def max_diff(my_list):
    n = 0
    for i in range(len(my_list)-1):
        diff = abs(my_list[i+1] - my_list[i])
        if diff > n:
            n = diff
    return n


def maxMin(inputList):
    """
    Finds the max and min in a list of positive values and returns a tuple

    :param inputList: Is a list of positive values
    :returns: Tuple of the max and min values
    :raises ImportError: If numpy is not installed in the env
    :raises ValueError: If there are values less than 0
    :raises TypeError: If the inputList is not an actual list
    """

    logging.basicConfig(filename='log.txt', level=logging.DEBUG)

    try:
        import numpy
    except ImportError:
        logging.error("missing a module!")
        raise ImportError("missing a module!")
    for i in inputList:
        if i < 0:
            logging.warning("Negative value detected")
            raise ValueError('Negative value detected')
    if not isinstance(inputList, list):
        logging.warning('Input is not a list')
        raise TypeError('Input is not a list')
    myMin = min(inputList)
    myMax = max(inputList)
    logging.debug(inputList)
    logging.debug('Min value: %s', myMin)
    logging.debug('Max value: %s', myMax)
    maxMinTuple = (myMin, myMax)
    logging.info(maxMinTuple)
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
