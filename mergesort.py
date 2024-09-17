def merge_sort(arr):
    n = len(arr)
    width = 1
    while width < n:
        left = 0
        while left < n:
            mid = left + width
            right = min(mid + width, n)
            merge(arr, left, mid, right)
            left += width
        width *= 2
    return arr

def merge(arr, left, mid, right):
    left_arr = arr[left:mid]
    right_arr = arr[mid:right]
    i, j, k = 0, 0, left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
arr = merge_sort(arr)
print(arr)  # [1, 2, 3, 4, 5, 6, 8]
