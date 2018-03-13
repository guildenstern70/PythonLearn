"""
    PythonLearn

    @author: Alessio Saltarin
"""

import pythonlearn.collections as collections
import pythonlearn.basic_class as basic_class
import pythonlearn.dictionary as dictionary
import pythonlearn.forloops as forloops
import pythonlearn.inheritance as inheritance
import pythonlearn.switch as switch
import pythonlearn.comprehension as comprehension

if __name__ == '__main__':
    
    # Collections
    coll = collections.Collections()
    baseclass = basic_class.BasicClass()
    dictry = dictionary.Dictionaries()
    forloops = forloops.ForLoops()
    inh_baseclass = inheritance.BaseClass('pippo')
    inh_extclass = inheritance.ExtendedClass('pippo')
    switch = switch.Switch()
    comprehension = comprehension.Comprehensions()
    
    # Test 
    objects_to_test = (coll,
                       baseclass,
                       dictry,
                       forloops,
                       inh_baseclass,
                       inh_extclass,
                       switch,
                       comprehension)
    for obj in objects_to_test:
        obj.output()
