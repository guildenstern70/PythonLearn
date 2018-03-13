"""
    PythonLearn

    Printer Util Class
    @author: Alessio Saltarin

"""


class Printer(object):
    """
    This class prints various outputs to demonstrate the code.
    """
    
    def print_output(self):
        self.objtest.output()

    def __init__(self, object_to_test):
        """
        Constructor.
        Parameters: object_to_test: must have a method 'output'
        """
        self.objtest = object_to_test
