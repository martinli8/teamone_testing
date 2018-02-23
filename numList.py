import logging


class numList:
    """This is a numList class.

    Attributes:
        :maxMin (tuple): tuple of the Max and Min values in the list

        :max_diff (list): list of the highest diff between 2 adj values in list

        :list_add (int): sum of all the values in the list

    """

    def __init__(self, myList=[]):
        self.list = myList
        self.maxMin = None
        self.max_diff = None
        self.list_add = None
        self.max_Min()
        self.find_diff()
        self.find_sum()

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

    def find_diff(self):
        """
        Finds maximum difference between two adjacent numbers in a list

        :param my_list: Is a list of numbers
        :returns: Largest difference between two adjacent numbers
        :raises ValueError: If my_list has 0 or 1 elements
        :raises ImportError: If numpy is not installed in environment
        :raises TypeError: If element in my_list is not an int, float, complex
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
                raise TypeError('List elements must be int, float, complex!')
        logging.debug('Returns %s', str(n))
        self.max_diff = n

    def find_sum(self):
        """
        Adds a lenist of numbers

        :param list_var: Is a list of numbers (int, float, complex)
        :returns: Addition of values in list
        :raises ValueError: If list_var is empty
        :raises ImportError: If numpy or numbers not installed in environment
        :raises TypeError: If element in list_var is not an int, float,complex
        """
        list_var = self.list
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
        self.list_add = value
