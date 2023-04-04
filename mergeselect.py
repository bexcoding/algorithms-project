'''
Title: Merge-Select Sort
Description: Uses merge sort for some cases and selection sort for others
Last Updated: March 30, 2023
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

    for i in range(len(list_to_sort) - 1):
        current_min = i
        for j in range((i + 1), len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[current_min]:
                current_min = j
        if current_min != i:
            list_to_sort[i], list_to_sort[current_min] = list_to_sort[current_min], list_to_sort[i]
    return list_to_sort


def combine(list1, list2):
    """
    list, list -> list
    combines two sorted lists into one larger sorted list

    list1: list of numbers
    list2: list of numbers

    assumes list1 and list2 are already sorted and of same type
    """

    first_counter = 0
    second_counter = 0
    combined_list = []
    # check for smallest or largest item at start of each list
    while first_counter < len(list1) and second_counter < len(list2):
        if list1[first_counter] < list2[second_counter]:
            combined_list.append(list1[first_counter])
            first_counter += 1
        else:
            combined_list.append(list2[second_counter])
            second_counter += 1
    # when only one list remains, add the rest of its components
    while first_counter < len(list1):
        combined_list.append(list1[first_counter])
        first_counter += 1
    while second_counter < len(list2):
        combined_list.append(list2[second_counter])
        second_counter += 1
    return combined_list


def mergesort(list_to_sort):
    """
    list -> list
    returns a sorted list

    list_to_sort: list of items to sort

    assumes: list items are all of same type
    """

    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        half = len(list_to_sort) // 2
        # split list in half recursively
        return combine(mergesort(list_to_sort[:half]),
                       mergesort(list_to_sort[half:]))


def mergeselect(list_to_sort):
    """
    list -> list
    runs selection sort on small lists and merge sort on large lists

    list_to_sort: list of items to sort

    assumes: list items are all of same type
    """

    if len(list_to_sort) <= 1:
        return list_to_sort
    elif len(list_to_sort) <= 60:
        return selection_sort(list_to_sort)
    else:
        return mergesort(list_to_sort)
