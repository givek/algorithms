# Link: https://leetcode.com/problems/rotate-array/
# Time: O(N)
# Space: O(1)


# Given an array of numbers: [1, 2, 3, 4, 5] and k = 3

# 1. reverse the entire array
#   - [5, 4, 3, 2, 1]
#
# 2. reverse from 0 to k - 1
#   - [3, 4, 5, 2, 1]
#
# 3. reverse from k to len(arr) - 1
#   - [3, 4, 5, 1, 2]


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums)


if __name__ == "__main__":
    main()
