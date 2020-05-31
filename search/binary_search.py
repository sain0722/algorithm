def binary_search(arr, target):

    start = 0
    end = len(arr)

    while start < end:

        middle = (start + end) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] > middle:
            start = middle + 1

        else:
            end = middle - 1

    return middle


arr = [2, 3, 5, 7, 11, 13, 17]
target = 7
target_idx = binary_search(arr, target)
print(target_idx, arr.index(target))
