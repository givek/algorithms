# Link: https://leetcode.com/contest/biweekly-contest-72/problems/count-equal-and-divisible-pairs-in-an-array/
# Time: O(N^2)
# Space: O(1)
# Score: 3


from typing import List


# Brute force


def count_pairs(nums: List[int], k: int) -> int:
    count = 0
    for i in range(0, len(nums), 1):
        for j in range(i + 1, len(nums), 1):
            if nums[i] == nums[j] and i * j % k == 0:
                count += 1
    return count
