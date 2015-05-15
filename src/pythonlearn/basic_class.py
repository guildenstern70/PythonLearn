"""
PythonLearn
Classes in Pyhton
@author: Alessio Saltarin

"""

from learnobject import LearnObject

class BasicClass(LearnObject):
    """
    Sample class with basic accessors and properties.
    Note the style: "Almost without exception, class names use the CapWords convention", from Guido's Style Guide
    """
    
    def ___get_x(self):
        return self._x
    
    def ___get_y(self):
        return self._y
    
    def ___set_x(self, xval):
        self._x = xval
        
    def ___set_y(self, yval):
        self._y = yval

    @property
    def sum(self):
        return (self._x + self._y)
    
    x = property(___get_x, ___set_x,
                         doc="""Gets or sets the X variable.""")

    y = property(___get_y, ___set_y,
                         doc="""Gets or sets the Y variable.""")
    
    def output(self):
        print '\n=== BASIC CLASS TEST ==='
        print 'Basic Class [' + str(self.x) + ',' + str(self.y) + ']'
        print 'Sum = ' + str(self.sum)
        print 'str(self) => ' + str(self)
        
    @staticmethod
    def static(x):
        print 'And this is a STATIC METHOD (without self)'
    
    @classmethod   
    def fromXY(self, x, y):
        "Initialize Basic Class with x and y values. This is a static method"
        return BasicClass(x, y)
    
    def __repr__(self):
        return "Object of BasicClass with x=" + str(self._x) + " and y=" + str(self._y)

    def __init__(self, xval=10, yval=10):
        " Constructor "
        self._x = xval
        self._y = yval
        