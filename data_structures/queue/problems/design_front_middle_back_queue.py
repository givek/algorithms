# Link: https://leetcode.com/problems/design-front-middle-back-queue/


import math
from collections import deque


class FrontMiddleBackQueue:
    def __init__(self):
        self.first = deque()

    def push_front(self, val: int) -> None:
        self.first.appendleft(val)

    def push_middle(self, val: int) -> None:
        queue_size = len(self.first)
        middle_pos = queue_size // 2
        num_remaining_elements = queue_size - middle_pos

        while middle_pos:
            self.first.append(self.first.popleft())
            middle_pos -= 1

        self.first.append(val)

        while num_remaining_elements:
            self.first.append(self.first.popleft())
            num_remaining_elements -= 1

    def push_back(self, val: int) -> None:
        self.first.append(val)

    def pop_front(self) -> int:
        if len(self.first) == 0:
            return -1
        return self.first.popleft()

    def pop_middle(self) -> int:
        if len(self.first) == 0:
            return -1
        queue_size = len(self.first)
        middle_pos = math.ceil(queue_size / 2)
        num_remaining_elements = queue_size - middle_pos

        while middle_pos - 1:
            self.first.append(self.first.popleft())
            middle_pos -= 1

        popped_element = self.first.popleft()

        while num_remaining_elements:
            self.first.append(self.first.popleft())
            num_remaining_elements -= 1
        return popped_element

    def pop_back(self) -> int:
        if len(self.first) == 0:
            return -1
        return self.first.pop()


def main():
    fmb_queue = FrontMiddleBackQueue()

    fmb_queue.push_back(1)
    fmb_queue.push_back(2)
    fmb_queue.push_back(4)
    fmb_queue.push_back(5)
    # fmb_queue.push_back(6)

    fmb_queue.push_middle(3)
    fmb_queue.pop_middle()

    while not (len(fmb_queue.first) == 0):
        print(fmb_queue.pop_front())


if __name__ == "__main__":
    main()
