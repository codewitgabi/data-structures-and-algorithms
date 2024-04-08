def search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return mid 
        
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(search([1, 3, 4, 5], 8))