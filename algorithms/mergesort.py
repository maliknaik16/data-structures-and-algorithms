
def merge(arr, low, mid, high):
    """
    Perform 2-way merging on the array/list.

    Time Complexity: O(m + n) ~= O(high - low + 1)
        Where, m = No. of elements in the list 1 ("mid - low" in this case).
               n = No. of elements in the list 2 ("high - mid + 1" in this case).
    """

    # Initialize start indexes for the two lists.
    i, j = low, mid + 1

    # Create a temporary list to store the merged elements.
    c = [0] * (high - low + 1)

    # Initialize k.
    k = 0

    while i <= mid and j <= high:

        # Add the minimum/smallest element from both the lists into the new list.
        if arr[i] <= arr[j]:
            c[k] = arr[i]
            i += 1
        else:
            c[k] = arr[j]
            j += 1

        k += 1

    # Add the remaining elements to the new list (if any).
    while i <= mid:

        c[k] = arr[i]
        i += 1
        k += 1

    # Add the remaining elements to the new list (if any).
    while j <= high:

        c[k] = arr[j]
        j += 1
        k += 1

    # Finally, add the merged elements to the original list/array.
    k = low

    while k <= high:
        # Get the original position of the correct index of the element by k - low.
        arr[k] = c[k - low]
        k += 1


def mergesort(arr, low, high):
    """
    Performs merge sort recursively on the given array/list.

    Time Complexity: O(n)
        Where, n = number of elements in the array/list.
    """

    if low < high:

        # Get the middle/center index.
        mid = (low + high) // 2

        # Merge the left array/list.
        mergesort(arr, low, mid)

        # Merge the right array/list.
        mergesort(arr, mid + 1, high)

        # Finally, merge the left and right array/list.
        merge(arr, low, mid, high)

if __name__ == '__main__':

    arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

    print('Before Sorting:', arr)
    mergesort(arr, 0, len(arr) - 1)
    print('After Sorting:', arr)
