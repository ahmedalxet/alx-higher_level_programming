class MyList(list):
    """
    A subclass of the built-in list type with a method for printing the list in sorted order.
    
    This class overrides the default initialization method to allow creating instances of the class without any arguments.
    """
    
    def __init__(self):
        """
        Initialize the list object.
        
        This method overrides the default initialization method of the list class to allow creating instances of the
        MyList class without any arguments.
        """
        super().__init__()
    
    def print_sorted(self):
        """
        Print the list in sorted (ascending) order.
        
        The list is sorted in place and the original list is not modified.
        """
        print(sorted(self))
