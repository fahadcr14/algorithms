def selection(arr):

    """
         
    >>> Complexity
        Time: O(n^2) n is len(arr)
        Space: O(1) takes constant memory
        
    >>> Working
        iterates over array find smallest and swaps with first and do so 
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr