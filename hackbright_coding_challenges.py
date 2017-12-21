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

#4. Days in Month
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


#5. Find lucky numbers
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

#6. Find range
def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple.
    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)
    >>> find_range([])
    (None, None)
    >>> find_range([7])
    (7, 7)
    """
    if nums == []:
        return (None, None)
    elif len(nums) == 1:
        return (nums[0], nums[0])
    else:
        sorted_nums = sorted(nums)
        return (sorted_nums[0], sorted_nums[-1])

#7. Fizzbuzz
def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.
    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    """
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i

#8. Has more vowels
def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?
    >>> has_more_vowels("moose")
    True
    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False
    >>> has_more_vowels("yay")
    False
    >>> has_more_vowels("Aal")
    True
    """
    vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    consts = []
    vowels = []

    for letter in word:
        if letter in vowel_set:
            vowels.append(letter)
        else:
            consts.append(letter)

    if len(vowels) > len(consts):
        return True
    else:
        return False

#9. Has Unique Characters
def has_unique_chars(word):
    """Does word contains unique set of characters?
    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True
    >>> has_unique_chars("Bob")
    True
    """
    letter_counts = {}
    for letter in word:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for key, value in letter_counts.items():
        if value > 1:
            return False

    return True

#10. Is a number prime?
def is_prime(num):
    """Is a number a prime number?
    >>> is_prime(0)
    False

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True

    >>> is_prime(999)
    False
    """
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
    #I seem to recall there being a more efficient way to do this with only 
    #range up to the square root of num, but I can't seem to get that version to 
    #work).

#11. Is a word a Palindrome?
def is_palindrome(word):
    """Return True/False if this word is a palindrome.
    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False
    >>> is_palindrome("Racecar")
    False
    """
    index = 0
    for letter in word:
        index += 1
        if letter != word[- index]:
            return False
    return True

#12. Largest smaller than
def find_largest_smaller_than(nums, xnumber):
    """Return the index of largest number in sorted list that is smaller than given number.
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    2
    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True
    """
    result = None
    index = -1
    if xnumber > nums[-1]:
        return len(nums) - 1

    if xnumber < nums[0]:
        return None

    for num in nums:
        index += 1
        if num > xnumber:
            result = index - 1
            break

    return result

#13. Turn into Leet speak
def translate_leet(phrase):
    """Translates input into "leet-speak".

    Letter  Becomes
        a   @
        o   0
        e   3
        l   1
        s   5
        t   7
    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'

    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'
        """
    translated = ""

    leet_speak = {
        'a': '@',
        'o': '0',
        'e': '3',
        'l': '1',
        's': '5',
        't': '7',
    }

    for char in phrase:
        translated += leet_speak.get(char.lower(), char)

    return translated
    #my first solutiong involved a lot of if elif statements for each character.
    #but this acted very strangely in practice.  Ended up looking at the solution.


