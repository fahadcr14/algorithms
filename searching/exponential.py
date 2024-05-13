

def exponential_search(arr,target):
    """
    >>> Uses exponent behaviour to search 
    >>> Takes any size of array but if arr[0] has target return 0 
    >>> Doubles the value of i then uses binary search to find
    """

    if arr[0]==target:
        return 0
    i=1
    while i<len(arr) and arr[i]<=target:
        i*=2
    start=i//2
    end=min(i,len(arr)-1)
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid 
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1 