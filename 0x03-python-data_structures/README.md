# 0x03-python-data_structures

## In summary:

Lists: 
 - Are mutable ordered collections of objects. 
 - Can be indexed, sliced and mutated. 
 - Have common methods like append(), insert(), remove(), pop(), index(), count(), sort(), reverse(), etc. 
 - Can be used as stacks and queues using methods like push(), pop(), enqueue(), dequeue(). 
 - Can be created using list comprehensions like [x for x in range(10) if x % 2 == 0]. 

Tuples: 
 - Are immutable ordered collections of objects. 
 - Similar to lists but cannot be changed once created. 
 - Used when order is important but immutability is desired. 
 - Created using parentheses () instead of square brackets []. 

Differences from strings: 
 - Lists are ordered and mutable, strings are ordered and immutable. 
 - List elements can be of any data type, strings can only contain characters. 
 - List elements can be changed, string characters cannot be changed. 
 - List slicing works differently than string slicing. 

Sequences: 
 - An ordered collection of objects. 
 - Includes lists, tuples, strings. 
 - Can be indexed and sliced. 

Unpacking: 
 - Allows extracting multiple values from an iterable (like a list or tuple) into multiple variables. Done using *. 
 - Used for tuple packing and sequence unpacking. 

The del statement: 
 - Can be used to delete elements from a list by index. 
 - Has the syntax del list[index].
