# Problem: Given a sorted array in which all elements
# appear twice (one after one) and one element
# appears only once. Find that element
# Constraints: in O(log n) complexity.
def searchUnique(arr, low, high):
    # Base Cases
    # 1. low is greater than high
    # 2. Array with single element
    if low > high:
        return None
    if low == high:
        return arr[low]
    # Find the middle element
    mid = low + (high - low) // 2
    if mid % 2 != 0:
        return (
            searchUnique(arr, mid + 1, high)
            if arr[mid - 1] == arr[mid]
            else searchUnique(arr, low, mid - 1)
        )

    if arr[mid] == arr[mid + 1]:
        return searchUnique(arr, mid + 2, high)
    else:
        return searchUnique(arr, low, mid)


array = [1, 1, 2, 4, 4, 5, 5, 6, 6]
result = searchUnique(array, 0, len(array) - 1)
print(result)
# Result: 2
