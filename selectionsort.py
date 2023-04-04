'''
Title: Selection Sort
Description: Sort a list by checking each item to see if it is the minimum
Last Updated: March 26, 2023
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


def selection_sort(list_to_sort):
    """
    list -> list
    returns a sorted list
    
    list_to_sort: list of items to sort
    
    assumes: list items are all of same type
    """
    
    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        for i in range(len(list_to_sort) - 1):
            current_min = i
            for j in range((i + 1), len(list_to_sort)):
                if list_to_sort[j] < list_to_sort[current_min]:
                    current_min = j
            if current_min != i:
                list_to_sort[i], list_to_sort[current_min] = list_to_sort[current_min], list_to_sort[i]
    return list_to_sort