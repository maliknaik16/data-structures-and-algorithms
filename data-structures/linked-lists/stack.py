
class Stack:

    def __init__(self) -> None:
        """
        Initializes the stack.
        """

        self.stack = []
        self.top = -1

    def push(self, data) -> None:
        """
        Pushes an element onto the stack.
        """

        self.stack.append(data)
        self.top += 1

    def peek(self):
        """
        Returns the top of the stack element.
        """

        return self.stack[self.top]

    def pop(self):
        """
        Pops the top element from the stack.
        """

        if not self.is_empty():
            elm = self.stack.pop()
            self.top -= 1

            return elm
        else:
            print('Stack is empty')

    def is_empty(self) -> bool:
        """
        Returns whether the stack is empty or not.
        """

        return self.top < 0

    def get_stack(self) -> list:
        """
        Returns the complete stack.
        """

        return self.stack

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
# Stack Contents: [2, 3]
# Top of the stack: 3
# Popping top element...
# Stack Contents: [2]
# Pushing 1 onto the stack...
# Stack Contents: [2, 1]
