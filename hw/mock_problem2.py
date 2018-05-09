"""
h index ==> check file h_index.py

largest k that there are at least k elements >= k in the given array

{5, 2, 4, 4}

k = 3 , {4, 5, 4}, 3 elements,  yes for k = 3
k = 4, only{4, 4, 5}, 3 elements, not 4 elements, NO for k = 4

{} => 0 ?

{2, 4, 4, 5}



"""

def largestKofKElements(nums):
    if not nums:
        return 0
    l = 0
    r = len(nums)