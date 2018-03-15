"""
    PythonLearn

    Object Composition in Pyhton
    @author: Alessio Saltarin

"""


class Chair:
    """ A chair class """

    def __init__(self, nr):
        self.serialNumber = nr

    def __repr__(self):
        return "I am the chair #" + str(self.serialNumber)


class Table:
    """ The table class with 4 chairs """

    def __init__(self):
        self.chairs = []
        for j in range(1,5):
            self.chairs.append(Chair(j))

    def __repr__(self):
        msg = "I am the table.\n"
        for chair in self.chairs:
            msg += '-- '+str(chair)+'\n'
        return msg

    def output(self):
        print('\n=== COMPOSITION TEST ===')
        print(self)







