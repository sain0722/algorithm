# 반복문 사용
def binary_search(arr, target):

    start = 0
    end = len(arr)-1

    while start < end:

        middle = (start + end) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] > target:
            start = middle + 1

        else:
            end = middle - 1

    return middle


arr = [2, 3, 5, 7, 11, 13, 17]
target = 7
target_idx = binary_search(arr, target)
print(target_idx, arr.index(target))


# recursive binary search
def binary_search_recur(arr, target, start, end):

    middle = (start + end) // 2

    if arr[middle] == target:
        return middle

    elif arr[middle] > target:
        return binary_search_recur(arr, target, middle+1, end)

    else:
        return binary_search_recur(arr, target, start, middle-1)


target_idx = binary_search_recur(arr, target, 0, len(arr)-1)
print(target_idx, arr.index(target))
