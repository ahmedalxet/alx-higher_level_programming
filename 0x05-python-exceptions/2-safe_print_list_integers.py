#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end=' ')
            integers_printed += 1
        print()
    except (ValueError, IndexError):
        pass
    return integers_printed
