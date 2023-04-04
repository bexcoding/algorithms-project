'''
Title: Merge Sort Efficiency Test
Description: Tests speed at which merge sort performs
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


import random
import time
import matplotlib.pyplot as plt
import mergesort as ms


def get_random_num():
    """
    () -> int
    returns random int between 0 and 200 (inclusive)
    """
    
    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return ((random.choice(DIGITS) + random.choice(DIGITS)) 
            * random.choice(DIGITS))


def get_random_list(size):
    """
    int -> list of ints
    returns a list of random integers of a given size
    
    size: size of desired list
    """
    
    random_list = []
    for i in range(size):
        random_list.append(get_random_num())
    return random_list


def run_n_sorts(test_size):
    """
    int -> dict
    returns a dict with pattern (size of list):(time needed to sort in ms)
    runs tests sorting lists by increments of 1000
    
    test_size: number of tests to run
    """
    
    test_dict = {}
    list_length = 0
    while test_size != 0:
        if list_length % 100 == 0:
            print(f"Running test #: {(list_length)}")
        # keep random list outside of timing so that the time to get list
        # does not affect merge sort timing
        random_list = get_random_list(list_length)
        test_start_time = time.time()
        ms.mergesort(random_list)
        test_total_time = (time.time() - test_start_time) * 1000
        test_dict.update({list_length: round(test_total_time, 3)})
        test_size -= 1
        list_length += 1
    return test_dict
        

def run_big_n_sorts(biggest_list):
    """
    int -> dict
    returns a dict with pattern (size of list):(time needed to sort in ms)
    runs tests sorting lists by increments of 1000
    
    biggest_list: the size of the biggest list tested
    """
    
    test_dict = {}
    list_length = 0
    while biggest_list >= 0:
        if list_length % 1000 == 0:
            print(f"Running test #: {(list_length)}")
        # keep random list outside of timing so that the time to get list
        # does not affect merge sort timing
        random_list = get_random_list(list_length)
        test_start_time = time.time()
        ms.mergesort(random_list)
        test_total_time = (time.time() - test_start_time) * 1000
        test_dict.update({list_length: round(test_total_time)})
        biggest_list -= 1000
        list_length += 1000
    return test_dict
        

def plot_results(length_and_time):
    x = list(length_and_time.keys())
    y = list(length_and_time.values())
    plt.plot(x, y)
    plt.grid(visible=True)
    plt.xlabel("Size of List Sorted")
    plt.ylabel("Time Needed to Sort List (in ms)")