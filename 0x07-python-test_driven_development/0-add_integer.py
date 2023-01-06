#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers.
    
    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer. Defaults to 98.
    
    Returns:
        int: The sum of a and b.
    
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    
    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return a + b
