
class Node:

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self):
        """
        Initializes the stack.
        """

        self.top = None

    def is_empty(self):
        """
        Returns whether the stack is empty or not.
        """

        return self.top == None

    def push(self, data):
        """
        Pushes an element onto the stack.
        """

        node = Node(data)

        if self.top:
            node.next = self.top

        self.top = node

    def pop(self):
        """
        Pops the top element from the stack.
        """

        if self.is_empty():
            print('Stack is empty')
        else:
            data = self.top.data
            self.top = self.top.next

    def get_stack(self):
        """
        Returns the complete stack.
        """

        root = self.top
        stack = []

        while root != None:
            stack.append(root.data)
            root = root.next

        return stack

    def peek(self):
        """
        Returns the top of the stack element.
        """

        if self.is_empty():
            return None

        return self.top.data

if __name__ == '__main__':

    stack = Stack()

    print('Pushing 2 onto the stack...')
    stack.push(2)
    print('Pushing 3 onto the stack...')
    stack.push(3)
    print('Stack Contents:', stack.get_stack())
    print('Top of the stack:', stack.peek())
    print('Popping top element...')
    stack.pop()
    print('Stack Contents:', stack.get_stack())
    print('Pushing 1 onto the stack...')
    stack.push(1)
    print('Stack Contents:', stack.get_stack())

# Result:
# ---
#
# Pushing 2 onto the stack...
# Pushing 3 onto the stack...
# Stack Contents: [3, 2]
# Top of the stack: 3
# Popping top element...
# Stack Contents: [2]
# Pushing 1 onto the stack...
# Stack Contents: [1, 2]
