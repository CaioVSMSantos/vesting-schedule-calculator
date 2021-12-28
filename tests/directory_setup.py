""" This is a support script to be used in tests so they can access
the src directory and it's classes

The method 'tests_setup_confirm()' os a sanity check that can be called
from the tests main() method.

"""
import inspect
import os
import sys

# Adding the top level directory to path in order to use the packages
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


def tests_setup_confirm():
    print("Tests Directory Setup success")
