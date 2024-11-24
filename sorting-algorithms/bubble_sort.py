def bubble_sort(arr: list) -> list:
    """
    Takes a list of numbers and sorts them by taking the largest number to the end of the list continuously.

    Algorithm:
        This compares adjacent numbers. A pointer is kept at a particular index and is compared against the element at the next index. This keeps on going until the last index is reached. The same thing happens again and stops at n - i - 1 just so it doesn't unnecessary comparisons.

    args:
        arr: a list of numbers

    returns:
        a list of sorted numbers

    tests:

    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([9, 6, 2, 7, 1])
    [1, 2, 6, 7, 9]
    """

    # [5, 4, 3, 2, 1] => 6

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
