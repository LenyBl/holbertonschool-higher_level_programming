#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_print = 0
    try:
        for i in my_list:
            print("{:d}".format(i))
            number_print += number_print
    except (ValueError, TypeError):
        pass
    return number_print
