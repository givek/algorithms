# Link: https://leetcode.com/problems/move-zeroes/
# Time: O(N)
# Space: O(1)


def move_zeros(nums):
    if not nums:
        return nums

    # move all the non-zero elements in the array to the front of the array.
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # fill the remaining array with 0's
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


def main():
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    print(nums)


if __name__ == "__main__":
    main()
