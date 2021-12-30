
class Queue:

    def __init__(self) -> None:
        """
        Initializes the queue.
        """

        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, data) -> None:
        """
        Inserts an element onto the rear/back of the queue.
        """

        self.queue.append(data)
        self.rear += 1

    def front_element(self):
        """
        Returns the front element of the queue.
        """

        return self.queue[0]

    def rear_element(self):
        """
        Returns the rear element of the queue.
        """

        return self.queue[len(self.queue) - 1]

    def dequeue(self):
        """
        Removes the front element from the queue.
        """

        if not self.is_empty():
            elm = self.queue.pop(0)

            return elm
        else:
            print('Queue is empty')

    def is_empty(self) -> bool:
        """
        Returns whether the queue is empty or not.
        """

        return len(self.queue) == 0

    def get_stack(self) -> list:
        """
        Returns the complete queue.
        """

        return self.queue

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
