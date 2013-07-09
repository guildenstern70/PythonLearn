'''
PythonLearn
Classes in Pyhton
@author: Alessio Saltarin

'''

def output():
    bc = BasicClass.fromXY(3,4)
    bc.x = 9
    print 'Basic Class 9,4'
    print 'Sum = ' + str(bc.sum)

class BasicClass(object):
    '''
    Sample class with basic accessors and properties.
    '''
    
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
    
    @classmethod   
    def fromXY(self, x, y):
        "Initialize Basic Class with x and y values. This is a static method"
        return BasicClass(x, y)


    def __init__(self, xval=10, yval=10):
        " Constructor "
        self._x = xval
        self._y = yval
        