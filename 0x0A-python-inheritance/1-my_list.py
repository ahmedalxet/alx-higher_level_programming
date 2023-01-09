class MyList(list):
    """
    A subclass of the built-in list type with a added method for printing the list in sorted order.
    
    The elements of the list must be of type int.
    """
    
    def print_sorted(self):
        """
        Print the list in sorted (ascending) order.
        
        The list is sorted in place and the original list is not modified.
        """
        # Create a copy of the list and sort it
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
