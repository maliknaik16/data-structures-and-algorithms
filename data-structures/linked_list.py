
class Node:

    def __init__(self, data: int = 0, next: 'Node' = None) -> None:

        self.data = data
        self.next = next

class LinkedList:

    def __init__(self) -> None:
        """
        Initializes the LinkedList class.
        """

        self.head = None
        self.current = None

    def get_current(self) -> Node:
        """
        Returns the current node pointer.
        """

        return self.current

    def get_head(self) -> Node:
        """
        Returns the head/root of the linked list.
        """

        return self.head

    def add(self, data: int) -> None:
        """
        Adds an element to the linked list.
        """

        if self.current is None:
            self.current = Node(data)
            self.head = self.current
        else:
            self.current.next = Node(data)
            self.current = self.current.next

    def traverse(self) -> None:
        """
        Traverses the LinkedList and print the list.
        """

        root = self.get_head()

        while root != None:
            print(root.data, end='')
            root = root.next

            if root:
                print(' -> ', end='')
            else:
                print(' -> NULL ', end='')

        print('')

if __name__ == '__main__':

    nums = [5, 3, 1, 0, 8, 2]

    ll = LinkedList()

    for num in nums:
        ll.add(num)

    ll.traverse()


