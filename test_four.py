'''
Title: Test Four
Description: Tests performance of four different sorting algorithms
Last Updated: March 29, 2023
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
import mergesort as mrgs
import insertionsort as inss
import selectionsort as slts
import bubblesort as bbls


MERGESORT_RESULTS = {}
INSERTION_RESULTS = {}
SELECTION_RESULTS = {}
BUBBLE_RESULTS = {}


def get_list_of_rand_nums(desired_length):
    """
    int -> list
    
    returns a list of random numbers of variable length. each number in the
    list is an int [0,1000)
    
    desired_length: number of random numbers in the resulting list
    
    assumes: desired_length is of type int
    """
    
    return [(round(random.random() * 1000)) for i in range(desired_length)]


def test_once(algorithm, unsorted_list):
    """
    function, list -> float
    
    returns the time needed to run a single test on a list
    
    algorithm: the sorting algorithm used in the test
    unsorted_list: list of integers in random order
    
    assumes: algorithm is an algorithm that takes one argument and sorts it
    assumes: each item in unsorted_list is of same type
    """
    
    test_start_time = time.time()
    algorithm(unsorted_list)
    return round(((time.time() - test_start_time)* 1000), 5) 


def run_test(test_high, test_interval):
    """
    int, int -> ()
    
    runs a series of timed sorting tests on four different sorting algorithms
    
    test_high: highest list length to test
    test_interval: amount to increase list length by on each loop
    
    assumes: test_high and test_interval are of type int
    assumes: test_interval < test_high
    """
    
    overall_start = time.time()
    current_test = 0
    current_list_length = 0
    while current_test <= test_high:
        if current_test % (test_high * 0.1) == 0:
            print(f"Running test {current_test}")
        # test merge sort
        MERGESORT_RESULTS.update({current_list_length: test_once(
            mrgs.mergesort, get_list_of_rand_nums(current_list_length))})
        # test insertion sort
        INSERTION_RESULTS.update({current_list_length: test_once(
            inss.insertion_sort, get_list_of_rand_nums(current_list_length))})
        # test selection sort
        SELECTION_RESULTS.update({current_list_length: test_once(
            slts.selection_sort, get_list_of_rand_nums(current_list_length))})
        # test bubble sort
        BUBBLE_RESULTS.update({current_list_length: test_once(
            bbls.bubble_sort, get_list_of_rand_nums(current_list_length))})
        current_list_length += test_interval
        current_test += test_interval
    overall_end = round((time.time() - overall_start), 4)
    print(f"Total testing time: {overall_end} seconds")
    
    
def test_hundred():
    """
    runs timed tests and updates results libraries
    each list is 1 item longer than previous loop
    longest list length is 100 items long
    """
    
    run_test(100, 1)


def test_thousand():
    """
    runs timed tests and updates results libraries
    each list is 100 items longer than previous loop
    longest list length is 1000 items long
    """
    
    run_test(1000, 100)
    
    
def test_ten_thousand():
    """
    runs timed tests and updates results libraries
    each list is 1_000 items longer than previous loop
    longest list length is 10_000 items long
    """
    
    run_test(10_000, 1_000)


def plot_results():
    # x1,y1 for merge sort
    x1 = list(MERGESORT_RESULTS.keys())
    y1 = list(MERGESORT_RESULTS.values())
    # x2,y2 for insertion sort
    x2 = list(INSERTION_RESULTS.keys())
    y2 = list(INSERTION_RESULTS.values())
    # x3,y3 for selection sort
    x3 = list(SELECTION_RESULTS.keys())
    y3 = list(SELECTION_RESULTS.values())
    # x4,y4 for bubble sort
    x4 = list(BUBBLE_RESULTS.keys())
    y4 = list(BUBBLE_RESULTS.values())
    plt.plot(x1, y1, label="Merge Sort")
    plt.plot(x2, y2, label="Insertion Sort")
    plt.plot(x3, y3, label="Selection Sort")
    plt.plot(x4, y4, label="Bubble Sort")
    plt.grid(visible=True)
    plt.xlabel("Size of List Sorted")
    plt.ylabel("Time Needed to Sort List (in ms)")
    plt.legend()