"""
perform a "__" sort on a list. (insert name when revealed after lab is done)
original list will not be edited.
param: list_instance : list : this is the list we want sorted
return: list : this is the sorted list
"""

import time
import numbers

start = time.time()
list_instance = [2, 4, 6, 14, 8, 10, 12]
original_list = list_instance.copy()


sublists = [] # of type list

while len(list_instance) > 0:

    list_min = list_instance[0]

    for i, n in enumerate(list_instance):

        if n < list_min:

            # make sublist
            sublist = list_instance[0:i+1]
            sublists.append(sublist)

            # slice sublist values from list
            list_instance = list_instance[i+1:]

            # prevent adding any empty sublists 
            if not len(list_instance) > 0: break
        
        # prevents bug where if first number is list_min, algorithm doesn't run
        if i in range(len(list_instance)): list_min = list_instance[i - 1]

# sort each sublist
for i, sublist in enumerate(sublists):

    if i == len(sublist) and sublist[0] < sublist[-1]:
        continue # last sublist is already in order, skip it
    
    # put it in order (last val will always be min value)
    sublist.insert(0, sublist.pop())
    
    # apply changes
    sublists[i] = sublist

# merge sublists into original list in pairs
destination = []
while len(sublists) > 0:
    
    sublist = sublists.pop(0) # get first value and remove to iterate

    while len(sublist) > 0:

        sub_num = sublist.pop(0) # get first value and remove to iterate
        dest_n = 0 # this will be the index at which we insert sub_num in destination

        for dest_num in destination:
            
            if sub_num < dest_num: # we found the position where sub_num needs to be
                break # we have the dest index we need

            dest_n += 1 # update our tracker index

        # insert sub_num @ position dest_n in dest
        destination.insert(dest_n, sub_num)

list_instance = destination
print("Result:", list_instance)
assert(sorted(original_list) == list_instance)
print((time.time() - start)*1000, "ms")
