# 1. Name:
#      Elijah Harrison
# 2. Assignment Name:
#      Lab 12 : Segregation Sort Program
# 3. Assignment Description:
#      Perform a segregation sort on a list passed as parameter
# 4. What was the hardest part? Be as specific as possible.
#      I simply implemented the program as-is from the pseudocode made in the 
#      design. It wouldn't work in the first place.
# 5. How long did it take for you to complete the assignment?
#      30 min. thus far..

def segregation_sort(list_instance:list):
    """
    performs a segregation sort on a list by calling 
    segregation_sort_recursive

    no return, list_instance is edited by reference
    """
    segregation_sort_recursive(list_instance, 0, len(list_instance)-1)
    return list_instance

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

    i_up = i_start
    i_down = i_end
    i_pivot = average_int_value_of(i_up, i_down)
    pivot_val = list_instance[i_pivot]

    while i_up <= i_end and pivot_val > list_instance[i_up]:
        i_up += 1
    while i_down >= 0 and list_instance[i_down] > pivot_val:
        i_down -= 1

    if i_up <= i_down:
        list_swap_index(list_instance, i_up, i_down)
        i_up += 1
        i_down -= 1

    # sort lower part
    segregation_sort_recursive(list_instance, i_start, i_up-1)

    # sort upper part
    segregation_sort_recursive(list_instance, i_up, i_end) 

    # by this point, the list (either sublist or whole list) 
    # should be sorted

def list_swap_value(list_x:list, val_1, val_2):
    i1 = list_x.index(val_1)
    i2 = list_x.index(val_2)
    list_swap_index(list_x, i1, i2)

def list_swap_index(list_x:list, i1:int, i2:int):
    list_x[i1], list_x[i2] = (list_x[i2], list_x[i1])

def average_int_value_of(val1:int, val2:int) -> int:
    return int((val1 + val2)/2)

print(segregation_sort([5, 7, 2, 3, 6, 1]))
