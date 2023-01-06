def matrix_mul(m_a, m_b):
    """Multiplies two matrices.
    
    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.
    
    Returns:
        list of lists: The result of multiplying m_a and m_b.
    
    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If one element of m_a or m_b is not an integer or a float.
        TypeError: If m_a or m_b is not a rectangle.
        ValueError: If m_a and m_b can't be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")
    
    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a) else "m_b must be a list of lists")
    
    # Check if m_a and m_b are empty
    if m_a == [] or m_b == [] or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a can't be empty" if m_a == [] or m_a == [[]] else "m_b can't be empty")
    
    # Check if one element of m_a or m_b is not an integer or a float
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats" if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) else "m_b should contain only integers or floats")
    
    # Check if m_a and m_b are rectangles
    row_sizes_a = [len(row) for row in m_a]
    row_sizes_b = [len(row) for row in m_b]
    if not all(size == row_sizes_a[0] for size in row_sizes_a) or not all(size == row_sizes_b[0] for size in row_sizes_b):
        raise TypeError("each row of m_a must be of the same size" if not all(size == row_sizes_a[0] for size in row_sizes_a) else "each row of m_b must be of the same size")
    
    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Initialize the result matrix with zeros
    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    
    # Multiply the matrices
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
