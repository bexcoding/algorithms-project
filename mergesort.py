'''
Title: Merge Sort
Description: A sorting solution based on divide and conquer recursion
Last Updated: March 23, 2023
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


def combine(list1, list2, mode="standard"):
    """
    list, list -> list
    combines two sorted lists into one larger sorted list

    list1: list of numbers
    list2: list of numbers
    mode: standard is sorted in ascending order; reverse is sorted descending

    assumes list1 and list2 are already sorted and of same type
    """

    first_counter = 0
    second_counter = 0
    combined_list = []
    # check for smallest or largest item at start of each list
    while first_counter < len(list1) and second_counter < len(list2):
        if mode == "standard":
            if list1[first_counter] < list2[second_counter]:
                combined_list.append(list1[first_counter])
                first_counter += 1
            else:
                combined_list.append(list2[second_counter])
                second_counter += 1
        if mode == "reverse":
            if list1[first_counter] > list2[second_counter]:
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


def mergesort(unsorted_list, mode="standard"):
    """
    list -> list
    returns a sorted list

    unsorted_list: list of random ints, floats, or strings
    mode: standard is sorted in ascending order; reverse is sorted descending
    """

    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        half = len(unsorted_list) // 2
        return combine(mergesort(unsorted_list[:half], mode),
                       mergesort(unsorted_list[half:], mode), mode)


def reverse_mergesort(unsorted_list):
    """
    list -> list
    returns a reverse sorted list

    unsorted_list: list of random ints, floats, or strings
    """

    return mergesort(unsorted_list, "reverse")
