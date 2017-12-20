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

#3. Days in month
def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month, given a string with month and the year as ints?

    >>> days_in_month("02 2015")
    28
    """
    month, year = date.split()
    month = int(month)
    year = int(year)
    is_leap = is_leap_year(year)
    if is_leap is True and month == 2:
        return 29
    else:
        if month == 2:
            return 28
        elif month % 2 == 1:
            return 31
        else:
            return 30


#4. Find lucky numbers
def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive). If more than one
        number is asked for, there should be no repeats in nums returned.
    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
    import random
    choices = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    lucky_nums = []
    if n > 0:
        for i in range(n):
            lucky_num = random.sample(choices, 1)
            choices = choices - set(lucky_num)
            lucky_nums.append(lucky_num[0])
    return lucky_nums

