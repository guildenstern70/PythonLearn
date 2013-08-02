'''
PythonLearn

@author: Alessio Saltarin
'''

import net.littlelite.pythonlearn.collections as collections
import net.littlelite.pythonlearn.basic_class as basic_class
import net.littlelite.pythonlearn.dictionary as dictionary

if __name__ == '__main__':
    
    # Collections
    coll = collections.Collections()
    baseclass = basic_class.BasicClass()
    dictry = dictionary.Dictionaries()
    
    # Test 
    objects_to_test = (
                       coll,
                       baseclass,
                       dictry )   
    for obj in objects_to_test:
        obj.output()
    