#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list

    new_list = []
    for index, item in enumerate(my_list):
        if index == idx:
            new_list.append(element)
            continue
        new_list.append(item)
    return new_list
