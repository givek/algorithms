# Link: https://leetcode.com/problems/number-of-recent-calls/
# Time: O(N)
# Space: O(N)


import sys
from collections import deque


class RecentCounter:
    def __init__(self):
        self.request_queue = deque()
        self.interval = 3000  # only store the requests that has happened in the past `interval` milliseconds.

    def ping(self, t: int):
        self.request_queue.append(t)  # enqueue the request time.
        # dequeue all the requests which has happened before the current time `interval`.
        while self.request_queue[0] < (t - self.interval):
            self.request_queue.popleft()
        return len(self.request_queue)  # return length to queue.


def main():
    recent_counter = RecentCounter()
    requests = [642, 1849, 4921, 5936, 5957]
    results = [1, 2, 1, 2, 3]

    for request, result in zip(requests, results):
        if not (result == recent_counter.ping(request)):
            sys.exit("Wrong Answer")
    print("Accepted")


if __name__ == "__main__":
    main()
