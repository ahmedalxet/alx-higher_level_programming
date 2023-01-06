#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    
    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix by.
    
    Returns:
        list of lists: A new matrix with all elements divided by div.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If any row of the matrix is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix is the same size
    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    divided_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    
    return divided_matrix
