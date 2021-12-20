
def binary_search_iterative(arr, low, high, key):
    """
    Iteratively finds the given key in the array/list.

    Time Complexity: O(log n)
    """

    while low <= high:

        # Get the index of the middle element.
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binary_search(arr, low, high, key):
    """
    Recursively finds the given key in the array, list.
    """

    # Get the index of the middle element.
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key > arr[mid]:

        return binary_search(arr, mid + 1, high, key)

    return binary_search(arr, low, mid - 1, key)

if __name__ == '__main__':

    arr = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
    n = len(arr)

    print('Binary Search (Using recursive method)')
    print('---')
    for i in range(n):
        idx = binary_search(arr, 0, n - 1, arr[i])

        if idx == -1:
            print('Key not found')
        else:
            print('Key (%s) found at index %d' % (arr[i], idx))

    print('\n')
    print('Binary Search (Using Iterative method)')
    print('---')
    for i in range(3, 10):
        idx = binary_search_iterative(arr, 0, n - 1, arr[i])

        if idx == -1:
            print('Key not found')
        else:
            print('Key (%s) found at index %d' % (arr[i], idx))

# Result:
# ---
#
# Binary Search (Using recursive method)
# ---
# Key (3) found at index 0
# Key (6) found at index 1
# Key (8) found at index 2
# Key (12) found at index 3
# Key (14) found at index 4
# Key (17) found at index 5
# Key (25) found at index 6
# Key (29) found at index 7
# Key (31) found at index 8
# Key (36) found at index 9
# Key (42) found at index 10
# Key (47) found at index 11
# Key (53) found at index 12
# Key (55) found at index 13
# Key (62) found at index 14
#
#
# Binary Search (Using Iterative method)
# ---
# Key (12) found at index 3
# Key (14) found at index 4
# Key (17) found at index 5
# Key (25) found at index 6
# Key (29) found at index 7
# Key (31) found at index 8
# Key (36) found at index 9
