
def segregation_sort(list_instance:list):
    """
    performs a segregation sort on a list by calling 
    segregation_sort_recursive

    no return, list_instance is edited by reference
    """
    segregation_sort_recursive(list_instance, 0, len(list_instance)-1)

def segregation_sort_recursive(list_instance:list, i_start:int, i_end:int):
    """
    performs a segregation sort using recursion

    PARAM: list_instance (passed by reference) : list
    PARAM: i_start : int : the start index of the sublist we are sorting
    PARAM: i_end : int : the end index of the sublist we are sorting

    no return, list_instance is edited by reference
    """

    # recursive end condition
    if i_end - i_start < 1: return # quick exit

    # define
    i_up = i_start # upward bound counter, starts at the beginning and moves up
    i_down = i_end # lower bound counter, starts at the end and moves down
    i_pivot = int((i_start+i_end)*.5)
    pivot_val = list_instance[i_pivot]

    # find val index in lower part of list that is greater than pivot
    for i in range(i_start, i_pivot):
        i_up = i # update swap index...
        if list_instance[i] > pivot_val: break

    # find val index in upper part of list that is less than pivot
    for i in range(i_end, i_pivot): # note: this will go in reverse order
        i_up = i # update swap index...
        if list_instance[i] > pivot_val: break
    
    list_swap_index(list_instance, i_up, i_down)

    # handle pivot index if it was swapped 
    if i_up   == i_pivot: i_pivot = i_down
    if i_down == i_pivot: i_pivot = i_up

    # sort lower part
    segregation_sort_recursive(list_instance, i_up, i_pivot - 1)

    # sort upper part
    segregation_sort_recursive(list_instance, i_pivot, i_down) 

    # by this point, the list (either sublist or whole list) 
    # should be sorted

def list_swap_value(list_x:list, val_1, val_2):
    i1 = list_x.index(val_1)
    i2 = list_x.index(val_2)
    list_swap_index(list_x, i1, i2)

def list_swap_index(list_x:list, i1:int, i2:int):
    list_x[i1], list_x[i2] = (list_x[i2], list_x[i1])

print(segregation_sort([5, 7, 2, 3, 6, 1]))
