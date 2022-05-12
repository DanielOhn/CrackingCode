"""
A magic delivery is an array A[0...n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
"""
import math 

def magicIndex(lst, start, end):
    if (end < start):
        return -1
    
    mid = math.floor((start + end) / 2)

    if (lst[mid] == mid):
        return mid
    elif (lst[mid] > mid):
        return magicIndex(lst, start, mid-1)
    else:
        return magicIndex(lst, mid+1, end)

a = [-1, 0, 2, 8, 19, 142]

m = magicIndex(a, 0, len(a)-1)

print(m)