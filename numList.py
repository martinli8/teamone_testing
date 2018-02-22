import logging

class numList:
    """This is a numList class.

    __init sets the various attributes.

    Attributes:
        maxMin (list): string

    """

    def __init__(self, myList = None, maxMin = None,
                 max_diff = None, list_add = None):
        self.list = myList
        self.maxMin = maxMin
        self.max_diff = max_diff
        self.list_add = list_add

    def max_Min(self):
        """
        Finds the max and min in a list of positive values and returns a tuple

        :param inputList: Is a list of positive values
        :returns: Tuple of the max and min values
        :raises ImportError: If numpy is not installed in the env
        :raises ValueError: If there are values less than 0
        :raises TypeError: If the inputList is not an actual list
        """

        inputList = self.list
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
        self.maxMin = maxMinTuple

    def max_diff(self):
        """
        Finds maximum difference between two adjacent numbers in a list

        :param my_list: Is a list of numbers
        :returns: Largest difference between two adjacent numbers
        :raises ValueError: If my_list has 0 or 1 elements
        :raises ImportError: If numpy is not installed in environment
        :raises TypeError: If element in my_list is not an int, float, or complex
        """

        my_list = self.list
        logging.basicConfig(filename='log.txt', level=logging.DEBUG)

        logging.info('Finding max difference between adjacent values in list')
        logging.debug('Printing %s', str(my_list))
        n = 0
        if len(my_list) < 2:
            logging.warning('Not enough values to calculate difference')
            raise ValueError('List too small, no difference to compare!')
        for i in range(len(my_list)-1):
            if(isinstance(my_list[i], (int, float, complex)) and
               isinstance(my_list[i+1], (int, float, complex))):
                diff = abs(my_list[i+1] - my_list[i])
                if diff > n:
                    n = diff
            else:
                raise TypeError('List elements must be int, float, or complex!')
        logging.debug('Returns %s', str(n))
        self.max_diff = n
