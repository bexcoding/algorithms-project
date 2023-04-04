'''
Title: Divide and Conquer Search
Description: Searches for a specific element in a list by splitting the search
    area in half on each search.
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


def divide_and_conquer_search(list_to_search, element_to_find):
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
        
    Assumptions
    ----------
    List will be sorted before using the divide and conquer search.
    """
    
    lo = 0
    hi = (len(list_to_search) - 1)
    while lo <= hi:
        # test middle element between lo and hi
        current_index = (lo + hi) // 2
        if list_to_search[current_index] == element_to_find:
            return current_index
        else:
            # update value of hi or lo
            if list_to_search[current_index] < element_to_find:
                lo = (current_index + 1)
            else:
                hi = (current_index - 1)
    return False
        

def divide_and_conquer_verbose(list_to_search, element_to_find):
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
        
    Assumptions
    ----------
    List will be sorted before using the divide and conquer search.
    """
    
    count = 0
    lo = 0
    hi = (len(list_to_search) - 1)
    while lo <= hi:
        count += 1
        # test middle element between lo and hi
        current_index = (lo + hi) // 2
        print(f"Searching for {element_to_find} at index {current_index}: ...")
        if list_to_search[current_index] == element_to_find:
            print(f"Found {element_to_find} at index {current_index}.")
            print(f"Search took {count} searches to find the element.")
            return current_index
        else:
            # update value of hi or lo
            if list_to_search[current_index] < element_to_find:
                lo = (current_index + 1)
            else:
                hi = (current_index - 1)
    print(f"Did not find {element_to_find} in this list.")
    return False