
def less_count(arr, i, target):
    """
    Returns the no. of elements less than the target.
    """

    count = 0

    for j in range(i, len(arr)):

        if arr[j] < target:
            count += 1

    return count

def cyclesort(arr, n):
    """
    Cycle sorting on the given array/list.

    Time Complexity: O(n^2)
    """

    i = 0

    while i < n:

        # Get the current element.
        element = arr[i]

        # Get the number of elements less than the current element.
        count = less_count(arr, i + 1, element)

        # Swap the current element in it's final sorted position if there are
        # elements less than the current element. Otherwise, move to the next
        # element.
        if count > 0:

            arr[i + count], arr[i] = arr[i], arr[i + count]
        else:

            i += 1



if __name__ == '__main__':

    arr = [2, 6, 4, 3, 1, 5]

    print('Before Sorting:', arr)
    cyclesort(arr, len(arr))
    print('After Sorting:', arr)

# Result:
# ---
#
# Before Sorting: [2, 6, 4, 3, 1, 5]
# After Sorting: [1, 2, 3, 4, 5, 6]

