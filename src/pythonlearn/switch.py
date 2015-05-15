"""
PythonLearn
Switches in Pyhton
@author: Alessio Saltarin

"""

from learnobject import LearnObject

class Switch(LearnObject):

    def _switch_as_a_dict(self, elem):
        """ Elem is a tag containing a word
            Return value is choosen on input.
            Default value is 50 if elem is not found """
        return {
            'name': 21,
            'age': 22,
            'ageord': 23,
            'ageplus': 34,
            'ageplusord': 43
            }.get(elem, 50)    # 9 is default if x not found
            
    def output(self):
        self.printdetail('Switch', str(self._switch_as_a_dict('age')))  # Should give 22
        
