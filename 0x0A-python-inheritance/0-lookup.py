#!/usr/bin/python3
def lookup(obj):
    # Get a list of all attributes and methods of the object
    attributes_and_methods = dir(obj)
    # Filter out special attributes and methods
    attributes_and_methods = [attr for attr in attributes_and_methods if not attr.startswith('__')]
    return attributes_and_methods
