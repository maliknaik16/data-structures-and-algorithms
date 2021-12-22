
def heaps_algorithm(arr, n, permutations):
    """
    Generates all possible permutations.

    Heap's algorithm generates all possible permutations of n objects.

    Reference:
      - https://www.cs.uni.edu/~wallingf/teaching/cs3530/sessions/session15.html

    Time Complexity: O(n!)
    """

    if n == 0:
        permutations.append(list(arr))
    else:

        for i in range(n):

            # Generate permutations with nth unaltered.
            heaps_algorithm(arr, n - 1, permutations)

            # Swap based on the n value.
            if n % 2 == 1:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
            else:
                arr[i], arr[n - 1] = arr[n - 1], arr[i]


if __name__ == '__main__':

    arr = ['a', 'b', 'c', 'd']

    permutations = []

    # Generate all the permuations and store in the permutations list.
    heaps_algorithm(list(arr), len(arr), permutations)

    print('For', arr, 'Found', len(permutations), '(' + str(len(arr)) + '!)' + ' permutations')

    for p in permutations:

        print(''.join(p))


# Result:
# ---
#
# For ['a', 'b', 'c', 'd'] Found 24 (4!) permutations
# abcd
# bacd
# cabd
# acbd
# bcad
# cbad
# dbca
# bdca
# cdba
# dcba
# bcda
# cbda
# dacb
# adcb
# cdab
# dcab
# acdb
# cadb
# dabc
# adbc
# bdac
# dbac
# abdc
# badc
