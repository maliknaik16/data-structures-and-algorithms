
def unique_element(arr):
    """
    Returns whether the elements in the given list/array are unique or not.

    Time Complexity: O(n^2)
    """

    # Get the length of the list/array.
    n = len(arr)

    for i in range(n - 1):

        for j in range(i + 1, n):

            if arr[i] == arr[j]:
                return False

    return True

def unique_element_optimized(arr):
    """
    Optimized version of the above implementation.

    Time Complexity: O(nlogn)
    """

    # Sort the array first.
    arr.sort()

    for i in range(1, len(arr)):

        if arr[i - 1] == arr[i]:
            return False

    return True


if __name__ == '__main__':

    arr1 = [1, 3, 6, 9, 5, 2, 4]
    arr2 = [7, 1, 8, 1, 8, 5,]

    if unique_element(arr1):
        print('Elements are unique:', arr1)
    else:
        print('There are duplicates:', arr1)

    if unique_element_optimized(arr2):
        print('Elements are unique:', arr2)
    else:
        print('There are duplicates:', arr2)

# Result:
# ---
#
# Elements are unique: [1, 3, 6, 9, 5, 2, 4]
# There are duplicates: [1, 1, 5, 7, 8, 8]
