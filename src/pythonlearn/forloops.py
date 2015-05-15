"""
PythonLearn
For Loop in Pyhton
@author: Alessio Saltarin

"""

from learnobject import LearnObject

class ForLoops(LearnObject):
    
    def __init__(self):
        self.outputs = { 'Fruits': [], 'Range': [], 'Chars': [] }

    def forFruits(self):
        fruits = ['banana', 'apple',  'mango']
        for fruit in fruits:        
            self.outputs['Fruits'].append(fruit)
            
    def forRange(self):
        for i in range(10,20):
            self.outputs['Range'].append(i)
       
    def forCharacters(self):
        for letter in 'Python':     
            self.outputs['Chars'].append(letter)
            
    def output(self):
        self.forFruits()
        self.forRange()
        self.forCharacters()
        self.printdictionary("FOR_LOOPS", self.outputs)
        

