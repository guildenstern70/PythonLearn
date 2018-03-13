

from .learnobject import LearnObject


class BaseClass:
    
    def __init__(self, name):
        print('Base Class __init__ > ' + name)
        
    def sum(self, a, b):
        return a+b
    
    def multiply(self, c, d):
        return c*d
    
    def custom(self, e, f):
        return (e*2)+f
    
    def output(self):
        results = [self.sum(3, 3), self.multiply(3, 3), self.custom(3, 3)]
        LearnObject.print_collection('INHERITANCE TEST: ', results)
        

class ExtendedClass(BaseClass):
        
    def custom(self, e, f):
        return (e*e)+f
    
    

    