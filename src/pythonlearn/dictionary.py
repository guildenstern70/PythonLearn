"""
PythonLearn
Dictionaries in Pyhton
@author: Alessio Saltarin

"""

from learnobject import LearnObject

class Dictionaries(LearnObject):
    
    def __init__(self):
        # A dictionary
        self.my_dictionary = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        
        # Update existing entry
        self.my_dictionary['Age'] = 8; # update 
        
        # Add  new entry
        self.my_dictionary['School'] = "DPS School"
        
        # Select entry
        # ie: print self.my_dictionary['School']
        
        # Remove entry with key 'Name'
        del self.my_dictionary['Name']
            
    def output(self):
        self.printdictionary("DICTIONARIES", self.my_dictionary)
