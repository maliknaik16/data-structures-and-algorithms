
def partition(arr, low, high):
    """
    Hoare's Partition with leftmost element as pivot.
    """

    # Get the leftmost element as pivot.
    pivot = arr[low]

    # Initialize the two pointers pointing to the first and last element.
    i, j = low, high - 1

    while i < j:

        # Finds the index that is greater than the pivot.
        while arr[i] <= pivot:
            i += 1

        # Finds the index that is smaller than the pivot.
        while arr[j] > pivot:
            j -= 1

        # Swap the found element if their index doesn't crossover.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Finally swap the pivot with the element smaller than the pivot to place
    # the pivot in it's sorted position.
    arr[j], arr[low] = arr[low], arr[j]

    return j


def quicksort(arr, low, high):

    if low < high:

        # Get the index of the pivot's sorted position.
        j = partition(arr, low, high)

        # Divide and Conquer/sort the array.
        quicksort(arr, low, j)
        quicksort(arr, j + 1, high)

if __name__ == '__main__':

    arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

    print('Before Sorting:', arr)
    quicksort(arr, 0, len(arr))
    print('After Sorting:', arr)

# Result:
# ---
# Before Sorting: [10, 16, 8, 12, 15, 6, 3, 9, 5]
# After Sorting: [3, 5, 6, 8, 9, 10, 12, 15, 16]
