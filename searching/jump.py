import math
def jump_search(arr, target):
    """
    >>> complexity:
        Time: O(√n), where n is the numer of elements in the arr.
        Space: O(1) takes constant space in memory.
    >>> uses linear search but on splited arrays using slicing

    """
    n=len(arr)
    jump_size = int(math.sqrt(n))
    prev=0
    curr=int(jump_size)
    while curr<n:
        if arr[curr]>target:
            for i,ele in enumerate(arr[prev:curr]):
                if ele==target:
                    return prev+i
        elif arr[curr]<=target:
            prev=curr
            curr = min(curr + jump_size, n)
    return -1
import random
def generate_random_array(size):
    return [random.randint(1, 1000000) for _ in range(size)]