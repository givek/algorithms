# Link: https://leetcode.com/contest/biweekly-contest-72/problems/maximum-split-of-positive-even-integers/
# Time: O(M), where M is maximum number of unique positive even integers.
# Space: O(1)
# Score: 0


from typing import List


# if `final_sum` is odd, return [] (an odd number cannot be represented as sum of even numbers).

# Now if `final_sum` is even, to split it into a sum of maximum number of unique positive even integers, we create a
# list and keep appending multiples of 2 to the list, we stop appending when sum of list <= `final_sum`.

# Now if sum of list == final_sum, return the list as it is.
# if sum of list is < final_sum, add the difference of `final_sum` and sum of list to the last element of the list.

# eg: `final_sum` = 14
# we keep appending multiples to 2 to the list until sum of list <= `final_sum`, [2, 4, 6] = 12
# but we want sum of list be equal to `fina_sum`.
# so, [2, 4, 6 + (14 - 12)] = [2, 4, 8].
# Therefore sum of list = 14.


def maximum_even_split(final_sum: int) -> List[int]:
    if final_sum % 2 != 0:
        return []

    curr_sum, ans = 0, []
    i = 2
    while curr_sum + i <= final_sum:
        ans.append(i)
        curr_sum += i
        i += 2

    ans[-1] += final_sum - curr_sum
    return ans
