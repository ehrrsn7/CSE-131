"""***************************************
1. Name:
    Elijah Harrison
2. Assignment Name:
    Lab 09 : Fancy Sort Program
3. Assignment Description:
    Perform a sorting algorithm (merge sort) on a list.
4. What was the hardest part? Be as specific as possible.
    I hit an expected roadbump, which was getting the simple_sort portion of the algorithm to work. 
    I put that algorithm in a file called test.py and worked through the algorithm by tracing and eventually edited the algorithm until it worked.
    Planning this program really helped with the time consumption.
5. How long did it take for you to complete the assignment?
    1 hour
***************************************"""

def main():
    list, filename = get_list()
    if list == False: return # exit mechanism
    sorted_list = sort(list, filename)

# import/define
import json
import os.path
from colorama import Style, Back, Fore # advice: in terminal, type: 'pip install colorama'

''' HELPER METHODS '''
def get_list():
    print("Please enter a filename for a .json file with a list: ")
    print("To exit, press enter.")
    filename = input("> ")

    if "" == filename or "exit" == filename.lower():
        return False

    elif "auto" == filename.lower():
        display_files()
        print(">> Do you have the above files in the directory containing this program? (y/n)")
        x = input("> ")
        print(x, yes, x in yes)
        if x.lower() in yes:
            automate_tests()
            return False
        else:
            print("Cancelling auto test.")
            return get_list() # recursive black magic        

    elif ".json" not in filename:
        print("Invalid file type! Must be .json")
        return get_list() # some recursive black magic

    else:
        new_list = json_file_to_list(filename)
        if new_list == False: return get_list() # recursive black magic
        print("Getting list from .json file contents...")
        return new_list, filename

def json_file_to_list(filename):
    if not os.path.exists(filename):
        print("File not found. Please enter a different file name.")
        return False

    with open(filename, 'r') as file:
        contents = json.load(file)
        return contents["array"]

files = [
    "json/ten_numbers.json"
]
def display_files():
    for filename in files:
        print(filename)

yes = ["yes", 'y']

# display row
# color
def printf(text): print(text, end='')
def row1_color(row):
    printf(Fore.RED)
    printf(row)
    printf(Style.RESET_ALL)
def row2_color(row):
    printf(Fore.BLUE)
    printf(row)
    printf(Style.RESET_ALL)
def row3_color(row):
    printf(Fore.YELLOW)
    printf(row)
    printf(Style.RESET_ALL)
def row4_color(row):
    printf(Fore.GREEN)
    printf(row)
    printf(Style.RESET_ALL)
def header_color(list, filename):
    print("\nlist:", Fore.GREEN, list, Style.RESET_ALL, "(original)")
    print(f"\nSorting...{filename}\n")
    print(Fore.RED,   "  (left list)   ", end="")
    print(Fore.GREEN, "  (right list): ", Style.RESET_ALL)
# no color
def row(row):
    printf(row)
    print()
def header(list, filename):
    print("list:", list, "(original)")
    print(f"\nSorting...{filename}\n")
    print("  (left list)   ", end="")
    print("  (right list): ")


def display_subsets(subsets):
    for i, subset in enumerate(subsets):
        if   i == 0: row1_color(subset)
        elif i == 1: row2_color(subset)
        elif i == 2: row3_color(subset)
        elif i == 3: row4_color(subset)


# swap
def swap(a, b): return b, a

# automate tests
def automate_tests():
    for filename in files:
        sort(json_file_to_list(filename), filename)
        input("Press enter to continue...")

''' SORT '''

def simple_sort(subset):
    
    i_pivot = 0

    while i_pivot < (len(subset) - 1):
        for i in range(i_pivot, len(subset)):

            x_i = len(subset) - 1   # index of last item in subset[]
            x   = subset[x_i]       # item which is out of order (last item in subset[])

            for i in range(len(subset)):
                item = subset[i]
                if x < item:
                    subset[i], subset[x_i] = subset[x_i], subset[i] # swap

        i_pivot += 1

    return subset # (sorted)


def sort_color(list, filename):
    # display header
    header_color(list, filename)

    subsets = []
    subset  = []

    smallest_item = list[0]

    for item, i in enumerate(list):
        if i == 0: continue # (skip first iteration)
    
        display_subsets(subsets)
        
        if item > smallest_item:
            subset.append(item)

        else:
            subsets.append(subset)
            subset = [] # reset ith subset


    # (result: nearly-sorted 'subsets' of list within list 
    #  represented as lists[] in subsets[])

    # sort subsets
    
    for subset in subsets:
        sorted_subset = simple_sort(subset)

    # subsets are sorted
    # merge subsets

    merged_list = []

    print("x")

    while len(subsets) > 0:
        # do the following while there are subsets remaining:

        # merge current 'merged list' with another subset
        for item in subsets[0]:

            merged_list.append(item)

            # we no longer need the old subset since it is now merged
            # REMOVE subset[0] from subsets[][] // (subset length -== 1)
            del subsets[0]
            # trace
            print(len(subsets))
        
        # merged list has new contents, perform insertion sort again
        # merged_list = simple_sort(merged_list)

    
    # END RESULT
    # when 'while' loop ends, 'merged_list' should be the sorted list.
    sorted_list = merged_list
    return sorted_list


    # # handle empty list
    # length_original = len(list)
    # if length_original <= 0: return list

    # # divide list into left and right about i_pivot (initially list n - 1)
    # list_right  = [list.pop()]
    # list_left   = list

    # # start loop
    # while True:
    #     condition = len(list_left) > 0 # exit condition
    #     if not condition: break

    #     # display progress
    #     row_color(list_left, list_right)

    #     # compare max value in left list to first value in right list
    #     i_max_l = list.index(max(list))

    #     # swap lists
    #     if  list_left[i_max_l] > list_right[0]:
    #         list_left[i_max_l] , list_right[0] = swap(
    #         list_left[i_max_l] , list_right[0])

    #     # move i_pivot (represented here by two distinct lists)
    #     list_right.insert(0, list_left.pop())

    # # final result
    # print("\nfinal result:", Fore.GREEN, list_right, Style.RESET_ALL)

    # # assert length size didn't change
    # length_final = len(list_right)
    # if length_original != length_final:
    #     print("sort fail\n")
    #     return list

    # print(Fore.YELLOW, "Assert original_length == end_length:", length_original == length_final, Style.RESET_ALL, "\n")

    # # return sorted list
    # return list_right

def sort_no_color(list, filename):
    # display header
    header(list, filename)

    # handle empty list
    length_original = len(list)
    if length_original < 0: return list

    # divide list into left and right about i_pivot (initially list n - 1)
    list_right  = [list.pop()]
    list_left   = list

    # start loop
    while True:
        condition = len(list_left) > 0 # exit condition
        if not condition: break

        # display progress
        row(list_left, list_right)

        # compare max value in left list to first value in right list
        i_max_l = list.index(max(list))

        # swap lists
        if  list_left[i_max_l] > list_right[0]:
            list_left[i_max_l] , list_right[0] = swap(
            list_left[i_max_l] , list_right[0])

        # move i_pivot (represented here by two distinct lists)
        list_right.insert(0, list_left.pop())

    # final result
    print("\nfinal result:", list_right)

    # assert length size didn't change
    length_final = len(list_right)
    if length_original != length_final:
        print("sort fail\n")
        return list

    print("Assert original_length == end_length:", length_original == length_final, "\n")

    # return sorted list
    return list_right

def sort(list, filename):
    if list == False:
        print("File not found...")
        return
    color = True # (for my sake) applying colors to the program output: t/f
    if color: return sort_color(list, filename)
    else: return sort_no_color(list, filename)

if __name__ == "__main__": main()
print("Exiting program.")