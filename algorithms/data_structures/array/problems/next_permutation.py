# Link: https://leetcode.com/problems/next-permutation/
# Time: O(N)
# Space: O(1)


# To compute the next permutation, we must increase the sequence as little as possible.
# Try to modify the rightmost elements, such that it forms a greater numbers.

# Example:
# -> 0 1 2 5 3 3 0

# find the rightmost element that needs to be changed.

# To identify that element, find the longest suffix that is non-increasing. (5 3 3 0)

# Now, find an element greater than the element to the left of the suffix (2) from the right. (3)

# Swap these two elements. -> 0 1 3 5 3 2 0

# Finally, as we want the suffix to increase as little as possible, we reverse the suffix.

# -> 0 1 3 0 2 3 5, which gives us the next permutation.


def next_permutation(nums):
    # find the longest non-increasing suffix from the right.

    i = len(nums) - 1

    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i <= 0:
        nums.reverse()
        return

    # find the element greater than the element to the left of the suffix.

    j = len(nums) - 1

    while j > 0 and nums[i - 1] >= nums[j]:
        j -= 1

    # swap these two elements

    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # reverse the suffix.

    j = len(nums) - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j -= 1


def main():
    nums = [0, 1, 2, 5, 3, 3, 0]

    next_permutation(nums)

    print(nums)


if __name__ == "__main__":
    main()
