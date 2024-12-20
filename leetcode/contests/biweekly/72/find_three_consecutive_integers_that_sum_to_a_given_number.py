# Link: https://leetcode.com/contest/biweekly-contest-72/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
# Time: O(1)
# Space: O(1)
# Score: 4

from typing import List


# def sum_of_three(num: int) -> List[int]:
#     mid = num // 3
#
#     if (mid - 1) + mid + (mid + 1) == num:
#         return [mid - 1, mid, mid + 1]
#     elif (mid - 1) + mid + (mid + 1) < num:
#         mid += 1
#         if (mid - 1) + mid + (mid + 1) == num:
#             return [mid - 1, mid, mid + 1]
#     else:
#         mid -= 1
#         if (mid - 1) + mid + (mid + 1) == num:
#             return [mid - 1, mid, mid + 1]
#     return []


# Better Approach:

# consider three consecutive integers that sum to the given number:
# (x - 1) + x + (x + 1) = 3x = num
# Therefore for a number to be represented as sum of three consecutive number it must be divisible by three.


def sum_of_three(num: int) -> List[int]:
    if num % 3 != 0:
        return []
    x = num // 3
    return [x - 1, x, x + 1]
