#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of the characters ., ?, and :.
    
    Args:
        text (str): The text to be printed.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Split the text into a list of words
    words = text.split()
    
    # Iterate over the list of words and print each word
    # with 2 new lines after ., ?, and :
    for i, word in enumerate(words):
        print(word, end=" ")
        if word[-1] in [".", "?", ":"]:
            print("\n" * 2)
        elif i == len(words) - 1:
            print()  # Print a new line after the last word
