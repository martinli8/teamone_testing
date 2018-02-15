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
    final_sum = 0
    for i in list_var:
        final_sum += i
    return final_sum
