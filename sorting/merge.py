def merge_sort(arr):
    """
    >>> Breaks the array till 1 and form the array again from broken pieces
    >>> Then compare when forming (merging )
    >>> Better then insetion bubble as It takes O(nlog(n)) where n is len of (arr)
    
    """

    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[0:mid]
    right_half=arr[mid:]
    left_sorted=merge_sort(left_half)
    right_sorted=merge_sort(right_half)
    merge=[]
    left_index=0
    right_index=0
    while left_index<len(left_sorted) and right_index<len(right_sorted):
        if left_sorted[left_index]<=right_sorted[right_index]:
            merge.append(left_sorted[left_index])
            left_index+=1
        else:
            merge.append(right_sorted[right_index])
            right_index+=1
    merge.extend(left_sorted[left_index:])
    merge.extend(right_sorted[right_index:])
    return merge
