# Link: https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Time: O(NLogN)
# Space: O(N)


from collections import deque
from typing import List


# To arrange the elements is the desired ordering, we need to perform both the given operations in reverse:
#   1. put the last element of the queue to the front.
#   2. enqueue the last element of the sorted deck into the front of queue.


def deck_revealed_increasing(deck: List[int]) -> List[int]:
    q = deque()
    deck.sort()
    for card in reversed(deck):  # access the deck from back.
        if q:  # if there are elements present in the queue,
            q.appendleft(q.pop())  # put the last element of the queue to the front.
        q.appendleft(card)  # enqueue elements from the deck into the queue.
    return list(q)


def main():
    deck = [17, 13, 11, 2, 3, 5, 7]
    print(deck_revealed_increasing(deck))


if __name__ == "__main__":
    main()
