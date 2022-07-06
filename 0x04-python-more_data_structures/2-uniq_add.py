#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for i in range(len(my_list)):
        if my_list[i].count == 1:
            add += i
    return add
