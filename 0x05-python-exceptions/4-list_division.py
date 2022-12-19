#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ZeroDivisionError, IndexError):
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                result.append(0)
            elif isinstance(my_list_1[i], (int, float)) or isinstance(my_list_2[i], (int, float)):
                print("wrong type")
            elif isinstance(my_list_2[i], (int, float)) and my_list_2[i] == 0:
                print("division by 0")
            else:
                print("out of range")
    return result
