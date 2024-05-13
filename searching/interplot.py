def interplot_search(arr,target):
    """
    >>> Efficent version of binary search 
    >>> arr is number of arrays e.g[2,43,4,5,5]
    >>> target to find the element like 43
    >>> return index of targeted element
    """
    low=0
    high=int(len(arr)-1)
    while low<=high:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos]==target:
            return pos
        elif arr[pos]<target:
            low=pos+1
        else:
            high=pos-1
    return -1
        
