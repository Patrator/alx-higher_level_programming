#!/usr/bin/python3
def max_integer(my_list=[]):
    
    if not my_list:
        return None

    h = my_list[0]
    for integer in my_list:
        h = integer if (integer > h) else h
    return h
