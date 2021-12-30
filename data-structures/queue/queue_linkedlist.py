
class Node:

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Queue:

    def __init__(self) -> None:
        """
        Initializes the queue.
        """

        self.front = None
        self.rear = None

    def enqueue(self, data) -> None:
        """
        Inserts an element onto the back of the queue.
        """

        node = Node(data)

        if self.rear:
            self.rear.next = node

        if not self.front:
            self.front = node

        self.rear = node

    def front_element(self):
        """
        Returns the front element of the queue.
        """

        if self.is_empty():
            return None

        return self.front.data

    def rear_element(self):
        """
        Returns the rear element of the queue.
        """

        if self.is_empty():
            return None

        return self.rear.data

    def dequeue(self):
        """
        Dequeues the front element from the queue.
        """

        if self.is_empty():
            print('Queue is empty')

            return None

        else:
            data = self.front.data
            self.front = self.front.next

            return data

    def is_empty(self) -> bool:
        """
        Returns whether the queue is empty or not.
        """

        return self.front == None

    def get_stack(self) -> list:
        """
        Returns the complete queue.
        """

        q = []

        root = self.front

        while root != None:
            q.append(root.data)
            root = root.next

        return q
if __name__ == '__main__':

    queue = Queue()

    print('Enqueuing 2 onto the queue...')
    queue.enqueue(2)
    print('Enqueuing 3 onto the queue...')
    queue.enqueue(3)
    print('Enqueuing 5 onto the queue...')
    queue.enqueue(5)
    print('Queue Contents:', queue.get_stack())
    print('Front of the queue:', queue.front_element())
    print('Rear of the queue:', queue.rear_element())
    print('Dequeuing...')
    queue.dequeue()
    print('Queue Contents:', queue.get_stack())
    print('Front of the queue:', queue.front_element())
    print('Rear of the queue:', queue.rear_element())
    print('Enqueuing 1 onto the stack...')
    queue.enqueue(1)
    print('Queue Contents:', queue.get_stack())
    print('Front of the queue:', queue.front_element())
    print('Rear of the queue:', queue.rear_element())

# Result:
# ---
#
# Enqueuing 2 onto the queue...
# Enqueuing 3 onto the queue...
# Enqueuing 5 onto the queue...
# Queue Contents: [2, 3, 5]
# Front of the queue: 2
# Rear of the queue: 5
# Dequeuing...
# Queue Contents: [3, 5]
# Front of the queue: 3
# Rear of the queue: 5
# Enqueuing 1 onto the stack...
# Queue Contents: [3, 5, 1]
# Front of the queue: 3
# Rear of the queue: 1
