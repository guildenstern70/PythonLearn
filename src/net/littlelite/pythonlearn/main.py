'''
PythonLearn

@author: Alessio Saltarin
'''

import net.littlelite.pythonlearn.collections as collections
import net.littlelite.pythonlearn.basic_class as basic_class
import net.littlelite.pythonlearn.dictionary as dictionary
import net.littlelite.pythonlearn.forloops as forloops

if __name__ == '__main__':
    
    # Collections
    coll = collections.Collections()
    baseclass = basic_class.BasicClass()
    dictry = dictionary.Dictionaries()
    forloops = forloops.ForLoops()
    
    # Test 
    objects_to_test = (
                       coll,
                       baseclass,
                       dictry,
                       forloops )   
    for obj in objects_to_test:
        obj.output()
    