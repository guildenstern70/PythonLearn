"""
     DirDeleter.py
     Usage: python dirdeleter.py [initial_directory] [string]

     Walks over all sub-directories starting from
     [initial_directory] and deletes every directory that has
     its name equal to [string] or containing [string]

"""

from stat import ST_MODE, S_ISDIR, S_ISREG
import os
import sys


def walktree(curdir, initdir):
    """
        Scan directory to find directories to delete
    """
    for scanfile in os.listdir(curdir):
        pathname = r'%s\%s' % (curdir, scanfile)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            walktree(pathname, initdir)
            deletedir(pathname, initdir)
        elif S_ISREG(mode):
            pass
        else:
            print('Attention: unknown %s' % pathname)


def deletedir(nome, init):
    """ Deletes a directory """
    if nome.rfind(init) > 0:
        prunefiles(nome)
        os.rmdir(nome)
        print('deleted: %s' % nome)
    else:
        print('visited: %s' % nome)


def prunefiles(nome):
    """ Deletes all files inside a directory """
    for scanfile in os.listdir(nome):
        path = r'%s\%s' % (nome, scanfile)
        os.remove(path)
        print(' --- deleted ' + path)


def printusage():
    """ Print help """
    print("""
Usage: python dirdeleter.py initial_dir string
where
    initial_dir:
            Initial directory to search for subdirectories to delete.
    string:
            The subdirectory containing 'string' in its name, or with a
            name equals to 'string' will be deleted.
""")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        walktree(sys.argv[1], sys.argv[2])
    else:
        printusage()

