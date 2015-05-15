"""
PythonLearn
LearnObject Util Class
@author: Alessio Saltarin

"""

class LearnObject(object):
    """
    A class to wrap the various code samples outputs in the package
    """
    
    def printcollection(self, title, collection):
        self._printdetails(title, collection)
        for item in collection:
            print item, 
       
    def printdictionary(self, title, xdict):
        self._printdetails(title, xdict)
        for k,v in xdict.items():
            print '['+k+': '+str(v)+']'
            
    def _printdetails(self, title, collection):
        print '\n=== ' + title + ' ==='
        print 'There are', len(collection), 'objects in the collection.'
        
    def printdetail(self, title, detail):
        print '\n=== ' + title + ' ==='
        print detail
        
    def output(self):
        raise NotImplementedError("Please Implement this method")

        