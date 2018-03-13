"""
     FileCopier.py v.0.1
     Usage: python FileCopier.py [file_path]

     Python 3.3 and superior

"""

import os
import sys
import shutil


def printusage():
    print("""
Usage: python FileCopier.py [initialdir] [destdir]
""")


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def copyfiles(dst, destdir):
    for root, dirs, files in os.walk(dst):
        print('examining ', root)
        for name in files:
            filename = os.path.join(root, name)
            filedest = os.path.join(destdir, name)
            print('copying', filename, '... ')
            print('.')
            try:
                shutil.copyfile(filename, filedest)
            except WindowsError:
                print("Access Denied: leaving it alone...")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        ensure_dir(sys.argv[2])
        copyfiles(sys.argv[1], sys.argv[2])
    else:
        printusage()

