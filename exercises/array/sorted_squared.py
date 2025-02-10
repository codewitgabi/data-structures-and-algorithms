# Best case scenario for sorting is O(log n)


def sorted_squared(arr):
    """
    Given an array of integers arr, return a new array sorted in ascending order of the squares of the original array elements.
    """

    squared_arr = sorted(list(map(lambda x: x**2, arr)))

    return squared_arr


print(sorted_squared([-4, -2, 1, 4]))  # Output: [1, 4, 9, 25]
print(sorted_squared([]))  # Output: [1, 4, 9, 25]


def updated_sorted_square(arr: list[int]) -> list[int]:
    """
    >>> updated_sorted_square([])
    []
    >>> updated_sorted_square([1, 2, 3, 4])
    [1, 4, 9, 16]
    >>> updated_sorted_square([-5, -3, 0, 2, 3, 4])
    [0, 4, 9, 9, 16, 25]
    """

    # Space complexity is O(n) because we assigned a new array with the same length as the original array
    # Time complexity is O(n) because we are iterating over the original array and this iteration depends on the length of the given array.
    # We sort directly as we iterate over the original array to prevent extra step of sorting which then affects the time complexity of the  whole algorithm. This is why this solution is best.

    left_pointer = 0
    right_pointer = len(arr) - 1
    new_array = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        left_square = arr[left_pointer] ** 2
        right_square = arr[right_pointer] ** 2

        if left_square >= right_square:
            new_array[i] = left_square
            left_pointer += 1

        else:
            new_array[i] = right_square
            right_pointer -= 1

    return new_array


if __name__ == "__main__":
    import doctest

    doctest.testmod()
