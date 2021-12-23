
class Node:

    def __init__(self, data=0, left=None, right=None):
        """
        Initializes the node.
        """

        self.data = data
        self.left = left
        self.right = right

def isSorted(arr):
    """
    Returns whether the array is sorted or not.

    Time Complexity: O(n)
    """

    for i in range(1, len(arr)):

        if arr[i] < arr[i - 1]:
            return False

    return True

def build_balanced_tree(arr):
    """
    Builds the balanced binary search tree from the sorted array.

    Time Complexity: O(n)
    """

    # Return None/NULL when there are no elements in the array..
    if arr == None or len(arr) == 0:
        return None

    # Get the median index of the list.
    mid = len(arr) // 2

    # Set the node.
    root = Node(arr[mid])

    # Get the left node.
    root.left = build_balanced_tree(arr[:mid])

    # Get the right node.
    root.right = build_balanced_tree(arr[mid + 1:])

    return root

def inorder_traversal(root):
    """
    Traverses the binary tree with left-root-right order.

    Time Complexity: O(n)
    """

    if not root:
        return

    inorder_traversal(root.left)
    print(root.data, end=' ')
    inorder_traversal(root.right)

def preorder_traversal(root):
    """
    Traverses the binary tree with root-left-right order.

    Time Complexity: O(n)
    """

    if not root:
        return

    print(root.data, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    """
    Traverses the binary tree with left-right-root order.

    Time Complexity: O(n)
    """

    if not root:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=' ')

if __name__ == '__main__':

    # Initialize the array.
    # arr = [1, 8, 3, 3, 6, 0, 2]
    arr = [1, 2, 3, 4, 5, 8, 9, 10, 11]

    # Get the length of the list.
    n = len(arr)

    # Sort the array if not sorted.
    if not isSorted(arr):
        print('List not sorted. Sorting list...')

        # Sort the array.
        arr.sort()
    else:
        print('List is already sorted...')

    print('Building the balanced binary search tree...')
    root = build_balanced_tree(arr)

    # Prints the In-order traversal of the tree.
    print('In-order traversal:')
    inorder_traversal(root)
    print('')

    # Prints the Pre-order traversal of the tree.
    print('Pre-order traversal:')
    preorder_traversal(root)
    print('')

    # Prints the Post-order traversal of the tree.
    print('Post-order traversal:')
    postorder_traversal(root)
    print('')

# Result:
# ---
#
# List is already sorted...
# Building the balanced binary search tree...
# In-order traversal:
# 1 2 3 4 5 8 9 10 11
# Pre-order traversal:
# 5 3 2 1 4 10 9 8 11
# Post-order traversal:
# 1 2 4 3 8 9 11 10 5
