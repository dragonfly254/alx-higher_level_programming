#!/usr/bin/python3
"""
this module contains a class that prevents the user
from dynamically creating new instance attributes, except
if the new instance attribute is called first_name.
"""


class LockedClass:
    """ locked class """
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
