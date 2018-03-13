"""
PythonLearn
LearnObject Util Class
@author: Alessio Saltarin

"""


class LearnObject(object):
    """
    A class to wrap the various code samples outputs in the package
    """
    
    @staticmethod
    def print_collection(title, collection):
        LearnObject._print_details(title, collection)
        for item in collection:
            print(item),
       
    @staticmethod
    def print_dictionary(title, xdict):
        LearnObject._print_details(title, xdict)
        for k,v in xdict.items():
            print('['+k+': '+str(v)+']')
            
    @staticmethod
    def _print_details(title, collection):
        print('\n=== ' + title + ' ===')
        print('There are', len(collection), 'objects in the collection.')
        
    @staticmethod
    def print_detail(title, detail):
        print('\n=== ' + title + ' ===')
        print(detail)
        
    def output(self):
        raise NotImplementedError("Please Implement this method")
