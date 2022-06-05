#!/usr/bin/python3
def element_at(my_list, idx):

    if idx < 0:
        return None
    if idx >= len(my_list):
        return None

    for index, lis in enumerate(my_list):
        if index == idx:
            return lis
