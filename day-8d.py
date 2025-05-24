# while importing, python searches several libraries to find the modules
# how do python seacrh subdirectories of this current folder to find the module
# it should think the sub directory as package folder, then it can search the sub directory to find the imported module
# for this, define another module names __init__.py, then python will consider this sb directory as python package folder

# and then update the import statement as below
# import subdirectory-name.module-name

import calc
import sys
# import ecommerce.arithmetic
# ecommerce.arithmetic.divide()
# or
from ecommerce.arithmetic import divide, sum
# now we can execute the function directly as below

divide()

print(sys.path)


# a subdirectory can have sub folders and for python to search modules there, we must create __init__.py file in all sub directories
# import ecommerce.subfolder.arithmetic


# intra package import
# we can use dot notation to find the directories as below, but not recommended by pep8

# from ...Azure Practice import *
