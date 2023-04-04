'''
Title: Linear Search
Description: Searches for a specific element in a list from left to right
Last Updated: March 31, 2023
Developer: Alexander Beck
Email: beckhv2@gmail.com
Github: https://github.com/bexcoding

.....//\\......//\\......//\\......//\\......//\\......//\\......//\\....../
....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//  \\....//
\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..// /\ \\..//
\\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /  \ \\// /
 || | <> | || | <> |                                     > | || | <> | || |
 || | <> | || | <> | ||                          ||   // > | || | <> | || |
 /\  \  /  /\  \  /  ||                          ||  //   /  /\  \  /  /\  \
/  \  \/  /  \  \/   ||____       ___      ___   || //   /  /  \  \/  /  \
 <> | || | <> | ||   ||    \\   //   \\  //   \\ ||||    | | <> | || | <> |
 <> | || | <> | ||   ||     || ||____|| ||       || \\   | | <> | || | <> |
\  /  ||  \  /  ||   ||     || ||       ||       ||  \\  |  \  /  ||  \  /
 \/  //\\  \/  //\\  ||____//   \\___//  \\___// ||   \\ \\  \/  //\\  \/  /
    //..\\    //..\\                                      \\    //..\\    //
\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //....\\  //.
\\//......\\//......\\//......\\//......\\//......\\//......\\//......\\//..
'''


import random


def linear_search(list_to_search, element_to_find):
    """
    Description
    ----------
    Searches a list for an item
    
    Return
    ----------
    If element_to_find is present, returns index of the element.
    If element_to_find not present, returns False.

    Parameters
    ----------
    list_to_search: list
        List of values that the algorithm will search through. Can be sorted
        or unsorted. Can be empty   
    element_to_find: any type
        Element that the algorithm will attempt to find in list_to_search.
        Can be any type because Python lists can hold multiple types.
    """
    
    for i in range(len(list_to_search)):
        if list_to_search[i] == element_to_find:
            return i
    return False


def linear_search_verbose(list_to_search, element_to_find):
    """
    Description
    ----------
    Searches a list for an item and prints feedback as list is searched
    
    Return
    ----------
    If element_to_find is present, returns index of the element.
    If element_to_find not present, returns False.

    Parameters
    ----------
    list_to_search: list
        List of values that the algorithm will search through. Can be sorted
        or unsorted. Can be empty   
    element_to_find: any type
        Element that the algorithm will attempt to find in list_to_search.
        Can be any type because Python lists can hold multiple types.
    """
    
    count = 0
    for i in range(len(list_to_search)):
        count += 1
        print(f"Searching for {element_to_find} at index {i}: ...")
        if list_to_search[i] == element_to_find:
            print(f"Found {element_to_find} at index {i}.")
            print(f"Search took {count} searches to find the element.")
            return i
    print(f"Did not find {element_to_find} in this list.")
    return False


def get_list_of_rand_nums(desired_length):
    """
    Description
    ----------
    Creates a list of random numbers
    
    Return
    ----------
    Returns a list of random numbers of variable length. Each number in the
    list is an int in the range [0,1000).
    
    Parameters
    ----------
    desired_length: int
        Number of random numbers in the resulting list  
    
    Assumptions
    ----------
    desired_length is of type int
    """
    
    return [(round(random.random() * 1000)) for i in range(desired_length)]


