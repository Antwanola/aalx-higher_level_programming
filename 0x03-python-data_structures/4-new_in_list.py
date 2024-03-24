#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if idx < 0 or idx >= my_list:
        print("{}".format(list_copy))
