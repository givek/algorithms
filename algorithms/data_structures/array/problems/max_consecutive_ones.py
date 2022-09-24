# Link: https://leetcode.com/problems/max-consecutive-ones/
# Time: O(N)
# Space: O(1)


from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    curr_consecutive_one_count = max_consecutive_one_count = 0

    for num in nums:

        if num == 1:
            curr_consecutive_one_count += 1
        else:
            curr_consecutive_one_count = 0

        max_consecutive_one_count = max(
            max_consecutive_one_count, curr_consecutive_one_count
        )

    return max_consecutive_one_count


def main():
    nums = [1, 1, 0, 1, 1, 1]
    print(find_max_consecutive_ones(nums))


if __name__ == "__main__":
    main()
