#!/usr/bin/python3
"""
This is a lookup module.
"""


def lookup(obj):
    """lookup func - list of available attributes and methods
                     of an object.

    Args:
        obj (object): input object

    Returns: list of available attributes and methods of an object
    """
    return dir(obj)
