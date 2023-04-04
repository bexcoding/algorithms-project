'''
Title: Insertion Sort
Description: Sort a list by moving elements to the left, one index at a time
Last Updated: March 27, 2023
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


def insertion_sort(list_to_sort):
    """
    list -> list
    returns a sorted list

    list_to_sort: unsorted list of items

    assumes: all items in list_to_sort are of same type
    """
    
    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        # current_index tracks which elements have been sorted already
        current_index = 1
        while current_index < len(list_to_sort):
            # swap tracks the current number that is being moved to its spot
            swap = current_index
            while swap != 0 and (list_to_sort[swap] < list_to_sort[(swap - 1)]):
                list_to_sort[swap], list_to_sort[(swap - 1)] = list_to_sort[(swap - 1)], list_to_sort[swap]
                swap -= 1
            current_index += 1
    return list_to_sort