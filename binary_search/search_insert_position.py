def search_insert_position(arr: list[int], target: int) -> int:
    """
    >>> print(search_insert_position([1, 3, 5, 6], 5))
    2
    >>> print(search_insert_position([1, 3, 5, 6], 2))
    1
    >>> print(search_insert_position([1, 3, 5, 6], 7))
    4
    >>> print(search_insert_position([1, 3, 5, 6, 9], 4))
    2
    >>> print(search_insert_position([1, 3, 5, 6, 9], 7))
    4
    >>> print(search_insert_position([1, 3, 5, 6, 9], 2))
    1
    >>> print(search_insert_position([0, 2, 4, 6, 7, 9, 13], 1))
    1
    >>> print(search_insert_position([0, 2, 4, 6, 7, 9, 13], 3))
    2
    >>> print(search_insert_position([0, 2, 4, 6, 7, 9, 13], 4))
    2
    >>> print(search_insert_position([0, 2, 4, 6, 7, 9, 13], 5))
    3
    >>> print(search_insert_position([0, 2, 4, 6, 7, 9, 13], 32))
    7
    """

    lower: int = 0
    upper: int = len(arr) + 1

    try:
        while lower < upper:
            mid: int = (lower + upper) // 2

            # handle case when the target is not in the lower end of the array

            if upper == lower + 1:
                return upper

            if arr[mid] == target:
                return mid
            
            if target > arr[mid]:
                lower = mid 
            else:
                upper = mid

    except IndexError:
        return upper - 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
