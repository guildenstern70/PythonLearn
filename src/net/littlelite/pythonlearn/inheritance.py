

from learnobject import LearnObject

class BaseClass(LearnObject):
    
    def __init__(self):
        print 'Base Class __init__'
        
    def sum(self, a, b):
        return a+b
    
    def multiply(self, c, d):
        return c*d
    
    def custom(self, e, f):
        return (e*2)+f
    
    def output(self):
        results = [self.sum(3, 3), self.multiply(3, 3), self.custom(3, 3)]
        self.printcollection('INHERITANCE TEST: ', results)
        

class ExtendedClass(BaseClass):
    
    def custom(self, e, f):
        return (e*e)+f
    
    

    