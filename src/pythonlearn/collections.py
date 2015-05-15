"""
PythonLearn
Collections in Pyhton
@author: Alessio Saltarin

"""

from learnobject import LearnObject


class Collections(LearnObject):
    
    def __init__(self):
        # Lists
        self.items = ['apple', 'banana', 'mango']
        self.items.append('cherry')
        
        # Unique elements collection: set
        self.set_items = set()
        self.set_items.add('apple')
        self.set_items.add('banana')
        self.set_items.add('apple')
        
        # Item in list
        self.item_nr = self.items[2] # is mango
        
        # Tuples (immutable container: cannot append or delete)
        self.tupleitems = ('apple', 'banana', 'mango')
        
        # If item is in list
        if 'apple' in self.items:
            pass


    def output(self):
        self.printcollection('LIST TEST', self.items)
        self.printdetail('ITEM #', self.item_nr)
        self.printcollection('SET TEST', self.set_items)
        self.printcollection('TUPLE TEST', self.tupleitems)
        