#coding challenges from the Hackbright list

#1. Add to Zero.
def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True
    >>> add_to_zero([0, 1, 2])
    True
    """
    for i in nums:
        for j in nums:
            if i + j == 0:
                return True
    return False

#2. Concatenate Lists
def concat_lists(list1, list2):
    """Combine lists.
    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
    """
    return list1 + list2
