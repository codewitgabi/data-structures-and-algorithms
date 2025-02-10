def monotonic_array(array):
    """
    >>> print(monotonic_array([]))
    True

    >>> print(monotonic_array([1, 2, 4, 20]))
    False

    >>> print(monotonic_array([1, 2, 3, 4, 5]))
    True

    >>> print(monotonic_array([1]))
    True

    >>> print(monotonic_array([6, 5, 4, 3, 2, 1]))
    True
    """

    for i in range(0, len(array) - 1):
        left_pointer = array[i]
        right_pointer = array[i + 1]

        # Check if current position equals next position

        if left_pointer == right_pointer:
            return False

        # Check for monotone decreasing

        if (left_pointer - 1) == right_pointer:
            continue

        # Check for monotone increasing

        elif (left_pointer + 1) == right_pointer:
            continue

        else:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
