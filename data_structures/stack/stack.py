class Stack:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return f"{[element for element in reversed(self.elements)]}"

    def __repr__(self):
        return f"{[element for element in reversed(self.elements)]}"

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0


def main():
    temp_stack = Stack()

    temp_stack.push(5)
    temp_stack.push(4)
    temp_stack.push(9)
    temp_stack.push(3)
    temp_stack.push(2)

    print(temp_stack)

    temp_stack.pop_mid(temp_stack.size())

    print(temp_stack)


if __name__ == "__main__":
    main()
