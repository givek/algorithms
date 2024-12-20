# Link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/submissions/
# Time: O(N)
# Space: O(N)


from typing import List


def even_sum(nums: List[int]):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total


def sum_of_even_nums_after_queries(
    nums: List[int], queries: List[List[int]]
) -> List[int]:
    # Compute even sum of the original list.
    even_total = even_sum(nums)

    ans = []
    for val, i in queries:

        # If the current number is even, subtract it from the even_total, as this number will be replaced by new value.
        # If the number is not even don't subtract as it was not the part of the even_total.
        if nums[i] % 2 == 0:
            even_total -= nums[i]

        nums[i] += val

        # If the new val is even add it to the even_total.
        if nums[i] % 2 == 0:
            even_total += nums[i]

        ans.append(even_total)

    return ans


def main():
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sum_of_even_nums_after_queries(nums, queries))


if __name__ == "__main__":
    main()
