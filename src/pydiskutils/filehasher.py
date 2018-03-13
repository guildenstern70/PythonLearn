"""
     FileHasher.py v.0.2
     Usage: python FileHasher.py [file_path]

     Python 3.3 and superior

"""

import sys
import hashlib


def setalgo(algorithm):
    if algorithm.lower() == "-sha1":
        algo = hashlib.sha1()
    else:
        algo = hashlib.md5()
    return algo


def printusage():
    print("""
Usage: python FileHasher.py [-algorithm] filename
where algorithm can be:
    md5
    sha1
if algorithm is not set, then md5 is used.
""")


def hash_file(filename, hash_name):
    f = open(filename, 'rb')
    print("\nReading %s \n" % f.name)
    m = setalgo(hash_name)
    read_bytes = 1024  # read 1024 bytes per time
    total_bytes = 0
    while read_bytes:
        read_string = f.read(read_bytes)
        m.update(read_string)
        read_bytes = len(read_string)
        total_bytes += read_bytes
        print("#"),
    f.close()
    print()
    print("\nTotal bytes: %d" % total_bytes)
    print("%s: %s" % (hash_name, m.hexdigest()))
    print()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1].find("-") == 0:
            hash_file(sys.argv[2], sys.argv[1])
        else:
            printusage()
    elif len(sys.argv) == 2:
        hash_file(sys.argv[1], '-md5')
    else:
        printusage()

