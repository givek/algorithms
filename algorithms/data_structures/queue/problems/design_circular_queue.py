# Link: https://leetcode.com/problems/design-circular-queue/


class CircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k  # initialize list with size `k`(`max_size`).
        self.size = 0  # number of elements present in the queue.
        self.max_size = k
        self.front = self.rear = -1

    def enqueue(self, value: int) -> bool:
        if self.is_empty():  # As the queue is empty, front = rear = -1.
            self.front = (
                self.rear
            ) = 0  # set front = rear = 0, as there will be only 1 element in the queue.
            self.queue[self.rear] = value
            self.size += 1
            return True

        if (
            self.is_full()
        ):  # As the queue is full we cannot add more elements to the queue.
            return False

        # As this is a circular queue use the mod operator to find the next position to the element.
        # eg. [4, 1, 3, 4, 5]
        #         f        r , where f = front, r = rear
        # next position = (r + 1) % max_size = (4 + 1) % 5 = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def dequeue(self) -> bool:
        if (
            self.is_empty()
        ):  # As the queue is empty we cannot remove elements from the queue.
            return False

        if (
            self.size == 1
        ):  # As the queue contains only 1 element, after remove that element queue will be empty.
            self.front = self.rear = -1  # So, set the front = rear = -1
            self.size -= 1
            return True

        self.front = (self.front + 1) % self.max_size  # refer enqueue.
        self.size -= 1
        return True

    def front(self) -> int:
        if self.is_empty():
            return self.front
        return self.queue[self.front]

    def rear(self) -> int:
        if self.is_empty():
            return self.rear
        return self.queue[self.rear]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.max_size


def main():
    circular_queue = CircularQueue(3)

    print(circular_queue.enqueue(1))
    print(circular_queue.enqueue(2))
    print(circular_queue.is_empty())


if __name__ == "__main__":
    main()
