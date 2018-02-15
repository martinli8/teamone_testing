# Assignment 4: TeamOne
import logging


def import_modules():
    logging.info('Importing numpy module')
    try:
        import numpy as np
    except:
        logging.warning('Please install numpy')
        raise ImportError('Module numpy not found!')


def max_diff(my_list):
    """
    Finds maximum difference between two adjacent numbers in a list

    :param my_list: Is a list of numbers
    :returns: Largest difference between two adjacent numbers
    :raises ValueError: If my_list has 0 or 1 elements
    :raises ImportError: If numpy is not installed in environment
    :raises TypeError: If element in my_list is not an int, float, or complex
    """

    logging.basicConfig(filename='log.txt', level=logging.DEBUG)

    logging.info('Finding max difference between adjacent values in list')
    logging.debug('Printing %s', str(my_list))
    n = 0
    if len(my_list) < 2:
        logging.warning('Not enough values to calculate difference')
        raise ValueError('List too small, no difference to compare!')
    for i in range(len(my_list)-1):
        if isinstance(my_list[i], (int, float, complex)) and \
           isinstance(my_list[i+1], (int, float, complex)):
            diff = abs(my_list[i+1] - my_list[i])
            if diff > n:
                n = diff
        else:
            raise TypeError('List elements must be int, float, or complex!')
    logging.debug('Returns %s', str(n))
    return n


def maxMin(inputList):
    myMin = min(inputList)
    myMax = max(inputList)
    maxMinTuple = (myMin, myMax)
    print(maxMinTuple)
    return maxMinTuple


def add_list_numbers(list_var):
    final_sum = 0
    for i in list_var:
        final_sum += i
    return final_sum
