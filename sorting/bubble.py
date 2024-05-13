def bubble(arr):
    """
    >>> Worst ever sorting algortihm
    >>> it will be worthless using on larger dataset to sort
    >>> Complexity of n^2 will take  lifetime to sort on bigger arrays of billions 
    
    """

    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

