class Queue:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return f"{[element for element in self.elements]}"

    def __repr__(self):
        return f"{[element for element in self.elements]}"

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.pop(0)

    def front(self):
        return self.elements[0]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0


def main():
    temp_queue = Queue()

    print(temp_queue.is_empty())

    temp_queue.enqueue(5)
    temp_queue.enqueue(4)
    temp_queue.enqueue(3)
    temp_queue.enqueue(2)

    print(temp_queue)

    print(temp_queue.front())

    temp_queue.dequeue()
    print(temp_queue.dequeue())

    print(temp_queue)

    print(temp_queue.is_empty())


if __name__ == "__main__":
    main()
