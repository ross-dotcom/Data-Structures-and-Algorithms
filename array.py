from array import *
import numpy as np
import random

def largest(array):
    mx = array[0]
    for i in range(1, len(array)):
        if array[i] > mx:
            mx = array[i]
    return mx

def smallest(array):
    mn = array[0]
    for i in range(1, len(array)):
        if array[i] < mn:
            mn = array[i]
    return mn

def find_dups(array):
    idx = 0
    dups = []
    while idx < len(array):
        if array[idx] in array[idx+1:]:
            dups.append(array[idx])
        idx+=1
    return set(dups)

my_list = np.random.choice(10, 10, replace=True)
array1 = array('i', my_list) # Declare array and insert my_list.
print(array1)
print('The largest element in the array is: %s' % (largest(array1)))
print('The smallest element in the array is: %s' % (smallest(array1)))
print('The following duplicates were found: %s' % (find_dups(array1)))