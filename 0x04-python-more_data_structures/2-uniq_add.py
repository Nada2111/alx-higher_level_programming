#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for ii in set(my_list):
        add += ii
    return add
