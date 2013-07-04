'''
PythonLearn
Collections in Pyhton
@author: Alessio Saltarin

'''

# Lists
items = ['apple', 'banana', 'mango']
items.append('cherry')

# Tuples (immutable container: cannot append or delete)
tupleitems = ('apple', 'banana', 'mango')

def printcollection(collection):
    print 'There are', len(collection), 'objects in the collection.'
    for item in collection:
        print item, 
    print '\nItem #2 = ' + items[1]


def output():
    printcollection(items)
    printcollection(tupleitems)
        