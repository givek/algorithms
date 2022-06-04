# Link: https://leetcode.com/problems/sort-colors/
# Time: O(N)
# Space: O(1)


def sort_colors(nums):
    # All the elements before the low pointer should be the low elements.
    # mid-pointer always points to the first unknown value.
    low = mid = 0

    # All the elements after the high pointer should be the high elements.
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]

            low += 1

            # Here, we increase mid as the mid-pointer should always point to the first unknown element.
            mid += 1

        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

        elif nums[mid] == 1:
            mid += 1


def main():
    nums = [1, 2, 1, 0, 0, 1, 2, 2, 0]

    sort_colors(nums)

    print(nums)


if __name__ == "__main__":
    main()
