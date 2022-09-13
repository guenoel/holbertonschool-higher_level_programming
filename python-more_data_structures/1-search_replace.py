#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    #return list(map(lambda x: x.replace(search, replace), my_new_list)) only for strings
    for i in range(len(my_new_list)):
        if my_new_list[i] == search:
            my_new_list[i] = replace
    return my_new_list
