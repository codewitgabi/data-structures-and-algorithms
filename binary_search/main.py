from typing import List


def check_left_location(arr, target, mid):
    if arr[mid - 1] != target:
        return mid
    return check_left_location(arr, target, mid - 1)


def check_right_location(arr, target, mid):
    try:
        if arr[mid + 1] != target:
            return mid
    except IndexError:
        mid = len(arr) - 1
        return mid
    return check_right_location(arr, target, mid + 1)


def binary_search(arr: List[int], target: int) -> int:
    lower: int = 0
    upper: int = len(arr) + 1

    if len(arr) == 0:
        return -1

    while lower < upper:
        mid: int = (lower + upper) // 2

        if arr[mid] == target:
            mid = check_left_location(arr, target, mid)
            return mid

        if arr[mid] < target:
            lower = mid
        else:
            upper = mid

    return -1


# Given an array of integer numbers sorted in ascending order, find the starting and ending position of a given number

def find_position(arr: List[int], target: int) -> int:
    lower = 0
    upper = len(arr) + 1

    while lower < upper:
        mid = (lower + upper) // 2

        if arr[mid] == target:
            starting_position: int = check_left_location(arr, target, mid)
            ending_position: int = check_right_location(arr, target, mid)

            return starting_position, ending_position
        if arr[mid] < target:
            lower = mid
        else:
            upper = mid

    return -1


def min_list_rotation(arr: List[int]) -> int:
    # using linear search

    count: int = 0
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i+1]:
            count += 1
        else:
            count += 1
            break

    print(count)


min_list_rotation([5, 6, 9, 0, 2, 3, 4])
min_list_rotation([3, 2, 4, 1])
min_list_rotation([1, 2, 3, 4])
