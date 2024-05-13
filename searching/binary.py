def binary_search(arr,target):
    """
    >>> Takes array of any size and target (the element to search)
    >>> performs search with complexity of O(logn) where n is len(arr) 
    >>> uses low and high and check till low <= high to find element
    """
    low=0
    high=int(len(arr)-1)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid 
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1