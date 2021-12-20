
# Heaps:
#
# Array representation (0-indexed) of the heap has the following properties:
#     - If node is at index "i" then,
#         - It's left child is at index 2*i + 1
#         - It's right child is at index 2*i + 2
#         - It's parent is at i // 2

class Heap:

    def __init__(self, arr=[], max_heap=True):
        """
        Initialize the Heap class.
        """

        self.heap = arr
        self.max_heap = max_heap
        self.heapify()

    def heappush(self, element):
        """
        Push the element onto the heap.

        Time Complexity: O(logn)
        """

        self.heap.append(element)
        self.heapify()

    def heappop(self):
        """
        Pops the root element from the heap i.e; min or max element.

        Time Complexity: O(logn)
        """

        self.heap.pop(0)
        self.heapify()

    def compare(self, i, j):

        if self.max_heap:

            return self.heap[i] > self.heap[j]

        return self.heap[i] < self.heap[j]

    def _heapify(self, i, n):
        """
        Perform the heapify until root.

        Time Complexity: O(logn)
        """

        # Initialize the index of root, left, and right element.
        target = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.compare(left, i):
            target = left

        if right < len(self.heap) and self.compare(right, target):
            target = right

        if target != i:

            # Swap the largest/smallest element.
            self.heap[i], self.heap[target] = self.heap[target], self.heap[i]

            self._heapify(target, n)

    def heapify(self):
        """
        Performs the heapify operation on the heap.

        Time Complexity: O(nlogn)
        """

        # Get the index of the last parent.
        last_parent_index = len(self.heap) // 2 - 1

        # Do heapify on each parent until root.
        for i in range(last_parent_index, -1, -1):
            self._heapify(i, len(self.heap))

    def heappeek(self):
        """
        Returns the minimum/maximum element from the heap.

        Time Complexity: O(1)
        """

        return self.heap[0]

    def get_heap(self):
        """
        Returns the heap.
        """

        return self.heap

if __name__ == '__main__':

    arr = [10, 20, 5, 30, 6, 7, 1, 69, 33]

    heap = Heap(arr, max_heap=False)

    # Print the heap.
    print('Heap:', heap.get_heap())

    # Push 3 in the heap
    print('Pushing 3 in the heap...')
    heap.heappush(3)

    # Print the heap.
    print('Heap:', heap.get_heap())

    # Push 78 in the heap.
    print('Pushing 78 in the heap...')
    heap.heappush(78)

    # Print the heap.
    print('Heap:', heap.get_heap())

    # Pop minimum element from the heap.
    print('Popping minimum element(', heap.heappeek(), ') from the heap...')
    heap.heappop()

    # Print heap.
    print('Heap:', heap.get_heap())

    # Pop 5 smallest elements from the heap.
    print('Popping 5 elements from the heap...')
    heap.heappop()
    heap.heappop()
    heap.heappop()
    heap.heappop()
    heap.heappop()

    # Print the heap.
    print('Heap:', heap.get_heap())

# Result:
# ---
#
# Heap: [1, 6, 5, 30, 20, 7, 10, 69, 33]
# Pushing 3 in the heap...
# Heap: [1, 3, 5, 30, 6, 7, 10, 69, 33, 20]
# Pushing 78 in the heap...
# Heap: [1, 3, 5, 30, 6, 7, 10, 69, 33, 20, 78]
# Popping minimum element( 1 ) from the heap...
# Heap: [3, 5, 10, 6, 7, 30, 69, 33, 20, 78]
# Popping 5 elements from the heap...
# Heap: [20, 30, 33, 69, 78]
