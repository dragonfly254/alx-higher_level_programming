#!/usr/bin/python3
"""
add_attribute module.
"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object.

    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when the attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
