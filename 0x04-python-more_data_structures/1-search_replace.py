#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for elm in my_list:
        if elm == search:
            return elm
        else:
            return replace
