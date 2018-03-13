"""
PythonLearn
Dictionaries in Pyhton
@author: Alessio Saltarin

"""

from .learnobject import LearnObject


class Dictionaries:
    
    def __init__(self):
        # A dictionary
        self.my_dictionary = {
            'Name': 'Zara',
            'Age': 8,
            'Class': 'First',
            'School': "DPS School"
        }
        
        # Update existing entry

        # Add  new entry

        # Select entry
        # ie: print self.my_dictionary['School']
        
        # Remove entry with key 'Name'
        del self.my_dictionary['Name']
            
    def output(self):
        LearnObject.print_dictionary("DICTIONARIES", self.my_dictionary)
