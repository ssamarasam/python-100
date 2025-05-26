# command line arguments

import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python day11-d.py <password>")
else:
    print("Password: ", sys.argv[1])
