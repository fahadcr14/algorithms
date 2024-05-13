def insertion(arr):
    """
    >>> Uses insetion mechanism 
    >>> In place sorting means 7A ,6 ,7-B will be 6,7A,7B maintaing position
    >>> Do sort on O(n^2) time 

    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr