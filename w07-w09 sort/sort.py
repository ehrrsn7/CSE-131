"""
sort module
contains function called fancy_sort

created by Elijah Harrison on Jun 04 2021

Lab 09 - fancy sort program

What was the hardest part? Be as specific as possible.
    Unexpected behavior came about when implementing the code 
    from my design. 
    I mitigated this roadblock by implementing the old TDD.

How long did it take for you to complete the assignment?
    3 hours
"""

import time

def sublist_sort(original_list:list) -> list:
    """
    FUNCTION: sublist sort
    
    Perform a sub-list sort on a list.
    Takes parameter list and returns new list which is 
    the same as the original list but sorted.
    Original list will not be edited.
    
    PARAM: original_list: list
    RETURN: sorted list: list
    """

    sublists = organize_into_sublists(original_list)

    return merge_sublists(sublists)


def organize_into_sublists(original_list:list) -> list:
    """
    FUNCTION organize_into_sublists(original_list):

    Takes parameter list and organizes it into sublists,
    where each sublist is each already-sorted portion 
    of the original list, and returns a list containing 
    these sublists.

    PARAM: original_list: list
    RETURN: sublists: list of lists
    """

    my_list = original_list.copy()

    sublists = [] # of type list

    while len(my_list) > 0:

        for index, current in enumerate(my_list):

            # current < previous
            if len(my_list) <= 0: break
            previous = my_list[index-1]

            if not index == 0 and current < previous:

                # slice values from original list up to 
                # current value in list into new sublist
                sublist = my_list[:index]
                sublists.append(sublist)

                # slice sublist values from list
                my_list = my_list[index:]

                # break to restart the process, this will prevent index bugs
                break
            
            # prevent bugs

            # if list is already in order, we get stuck
            if len(original_list) == index:
                # we've looped through the whole thing
                # and nothing was done, this means that
                # the list is already in order

                return [ original_list.copy() ] # quick exit

            # if what's left of the list is only 1 value long, 
            # if will compare against itself and we we'll get stuck
            if len(my_list) == 1:
                # what's left of the list is only 1 value long

                # this should take care of the while loop condition
                # make a sublist containing last val in my_list
                sublists.append([ my_list.pop() ])
            
    for sublist in sublists: assert isinstance(sublist, list)
    return sublists


def merge_sublists(sublists:list) -> list:
    """
    FUNCTION merge_sublists(sublists):

    This function takes sublists and merges them, one sublist at a 
    time, into a new list called destination[].
    The merging process involves removing the first value from
    the instance sublist and placing it in destination[] in order.

    PARAM: sublists: list of lists
    RETURN: sorted list: list
    """

    destination = []

    while len(sublists) > 0:
        
        # get first value and remove to iterate
        sublist = sublists.pop(0)

        destination_previous = destination[:] # deep copy
        destination.clear()

        # merge sublist[] values with previous destination[] values
        while len(sublist) > 0:

            # add destination_previousp[] values in if they are 
            # smaller than next sublist[] value
            while len(destination_previous) > 0:
                if destination_previous[0] < sublist[0]:
                    destination.append(destination_previous.pop(0))
                else: break
            
            # add in sublist[] value, they are smaller than next (if any) 
            # destination_previous[] values
            destination.append(sublist.pop(0))

            # loop will end when no values are left in sublist[]
        
        # if there are any destination_previous[] values left, 
        # dump them in
        while len(destination_previous) > 0:
            destination.append(destination_previous.pop(0))
            

    return destination
