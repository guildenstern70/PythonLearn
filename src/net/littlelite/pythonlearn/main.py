'''
PythonLearn

@author: Alessio Saltarin
'''

import net.littlelite.pythonlearn.collections as collections
import net.littlelite.pythonlearn.basic_class as basic_class
import net.littlelite.pythonlearn.dictionary as dictionary
import net.littlelite.pythonlearn.forloops as forloops
import net.littlelite.pythonlearn.inheritance as inheritance
import net.littlelite.pythonlearn.switch as switch

if __name__ == '__main__':
    
    # Collections
    coll = collections.Collections()
    baseclass = basic_class.BasicClass()
    dictry = dictionary.Dictionaries()
    forloops = forloops.ForLoops()
    inh_baseclass = inheritance.BaseClass('pippo')
    inh_extclass = inheritance.ExtendedClass('pippo')
    switch = switch.Switch()
    
    # Test 
    objects_to_test = (
                       coll,
                       baseclass,
                       dictry,
                       forloops,
                       inh_baseclass,
                       inh_extclass,
                       switch )   
    for obj in objects_to_test:
        obj.output()
    