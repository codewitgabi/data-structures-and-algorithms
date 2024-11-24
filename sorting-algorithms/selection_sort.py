def selection_sort(arr: list) -> list:  # O(n ^ 2)
    """
    Takes a list of numbers and sorts them by taking the smallest number to the beginning of the list continuously.

    Algorithm:
        This is different from bubble_sort algorithm in that it does not compare adjacent elements but rather keeps a pointer at a specific index and compares other elements with it. If a number is found to be less than it, it is swapped with the element at that pointer. The pointer then moves and keeps comparing with elements after it. This runs at O(n^2) time complexity.

    args:
        arr: a list of numbers

    returns: a list of sorted numbers

    tests:

    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> selection_sort([3, 8, 2, 5, 8, 0, 4])
    [0, 2, 3, 4, 5, 8, 8]
    """

    for i in range(len(arr) - 1):  # O(n)
        for j in range(i + 1, len(arr)):  # O(n -1) =>  O(n)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
