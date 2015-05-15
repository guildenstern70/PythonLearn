"""
     FilesDeleter.py
     Usage: python FilesDeleter.py [initial_dir] [string]

     Walks every subdirectory starting from
     [initial_dir] and deletes every file in it that
     contains in its file name 'string'

         Example: python FilesDeleter.py . .class
         Deletes every .class file in all subdirs starting from current.

"""

import os
import sys


def deletefiles(dst, extension):
    for root, dirs, files in os.walk(dst):
        for name in files:
            # If name ends with 'extension' kill it
            if name.rfind(extension)>0:
                print 'deleting', os.path.join(root, name)
                try:
                    os.remove(os.path.join(root, name))
                except WindowsError:
                    print "Access Denied: leaving it alone..."


if __name__ == "__main__":
    print "FilesDeleter v.0.2"
    if len(sys.argv)>1:
        deletefiles(sys.argv[1],sys.argv[2])
    else:
        print """
     FilesDeleter.py
     Usage: python FilesDeleter.py [initial_dir] [string]

     Walks every subdirectory starting from
     [initial_dir] and deletes every file in it that
     contains in its file name 'string'
         
         Example: python FilesDeleter.py . .class
         Deletes every .class file in all subdirs starting from current.

"""

