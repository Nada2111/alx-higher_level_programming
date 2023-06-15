#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for ii in range(len(new_list)):
        if new_list[ii] == search:
            new_list[ii] = replace
    return new_list
