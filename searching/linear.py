def linear_search(arr,target):
    """
    >>> Simple searching algortihm that runs on O(n) space is O(1)
    """
    for i,j in enumerate(arr):
        if j==target:
            return i
    return -1