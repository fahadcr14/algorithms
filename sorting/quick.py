def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] < pivot:
            
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  

def quick_sort(arr, low, high):
    """
    >>> This function recursive divides the arr into smaller sub-arrs using the partition function, 
        and then sorts these sub-arrs.
    >>> complexity of this is linear which O(log(n)) but if pivot is smallest or largest means start or end then 
        worst case will be achieved and that makes it O(n*2) the same as bubble sort time 
    >>> but takes memory of O(log(n)) cuz of recursion depth tree 
    """
    if low < high:
        pivot_ind = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_ind - 1) 
        quick_sort(arr, pivot_ind + 1, high)

    return arr