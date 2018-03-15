"""
    PythonLearn

    For Loop in Pyhton
    @author: Alessio Saltarin

"""

from .learnobject import LearnObject


class ForLoops:
    
    def __init__(self):
        self.outputs = { 'Fruits': [], 'Range': [], 'Chars': [] }

    def for_fruits(self):
        fruits = ['banana', 'apple',  'mango']
        for fruit in fruits:        
            self.outputs['Fruits'].append(fruit)
            
    def for_range(self):
        for i in range(10, 20):
            self.outputs['Range'].append(i)
       
    def for_characters(self):
        for letter in 'Python':     
            self.outputs['Chars'].append(letter)
            
    def output(self):
        self.for_fruits()
        self.for_range()
        self.for_characters()
        LearnObject.print_dictionary("FOR_LOOPS", self.outputs)
        

