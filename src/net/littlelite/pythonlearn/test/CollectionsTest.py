'''
PythonLearn
Test Collections in Pyhton
@author: Alessio Saltarin
'''

import unittest

from net.littlelite.pythonlearn.collections import items


class TestCollections(unittest.TestCase):


    def testItems(self):
        assert items == ['apple', 'banana', 'mango', 'cherry']


if __name__ == "__main__":
    unittest.main()