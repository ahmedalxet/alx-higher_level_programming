def matrix_mul(m_a, m_b):
    # ...
    
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
